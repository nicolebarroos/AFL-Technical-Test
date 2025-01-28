import pytest
from unittest.mock import MagicMock
from fastapi.testclient import TestClient
from src.main import app
from src.infrastructure.dependencies import get_company_use_case
from src.application.use_cases.company_use_case import CompanyUseCase
from src.infrastructure.auth import create_access_token


@pytest.fixture
def mock_company_repository():
    """Mocka o repositório de empresas."""
    mock_repo = MagicMock()
    mock_repo.create_company.return_value = {
        "id": 1,
        "nickname": "EmpresaX",
        "trade_name": "Empresa X Soluções",
        "legal_name": "Empresa X Soluções LTDA",
        "cnpj": "1234567890123",
        "uf": "CE",
        "city": "Fortaleza",
        "logo": "empresaX.png",
        "created_at": "2025-01-01T00:00:00"
    }
    return mock_repo


@pytest.fixture
def mock_company_use_case(mock_company_repository):
    """Mocka o caso de uso de empresas."""
    return CompanyUseCase(company_repository=mock_company_repository)


@pytest.fixture
def mock_auth_token():
    """Simula login e retorna um token de autenticação mockado."""
    token = create_access_token(data={"sub": "test@example.com"})
    return token


@pytest.fixture
def client(mock_company_use_case):
    """Configura o cliente de teste com dependências mockadas."""
    app.dependency_overrides[get_company_use_case] = lambda: mock_company_use_case
    return TestClient(app)


def test_create_company_success(client, mock_auth_token, mock_company_repository):
    """Testa a criação de uma empresa com sucesso usando mocks."""
    response = client.post(
        "/companies/create_company",
        json={
            "nickname": "EmpresaX",
            "trade_name": "Empresa X Soluções",
            "legal_name": "Empresa X Soluções LTDA",
            "cnpj": "1234567890123",
            "uf": "CE",
            "city": "Fortaleza",
            "logo": "empresaX.png"
        },
        headers={"Authorization": f"Bearer {mock_auth_token}"}
    )

    assert response.status_code == 200, f"Falha: {response.json()}"
    data = response.json()
    assert data["nickname"] == "EmpresaX"
    assert data["cnpj"] == "1234567890123"

    call_args = mock_company_repository.create_company.call_args
    print("Argumentos recebidos:", call_args)

    args, _ = call_args
    received_data = args[0]

    assert received_data.nickname == "EmpresaX"
    assert received_data.trade_name == "Empresa X Soluções"
    assert received_data.legal_name == "Empresa X Soluções LTDA"
    assert received_data.cnpj == "1234567890123"
    assert received_data.uf == "CE"
    assert received_data.city == "Fortaleza"
    assert received_data.logo == "empresaX.png"
    
def test_list_companies_success(client, mock_auth_token, mock_company_repository):
    """Testa a listagem de empresas com sucesso."""
    mock_company_repository.get_companies.return_value = [
        MagicMock(
            id=1,
            nickname="EmpresaX",
            trade_name="Empresa X Soluções",
            legal_name="Empresa X Soluções LTDA",
            cnpj="1234567890123",
            uf="CE",
            city="Fortaleza",
            logo="empresaX.png",
            created_at="2025-01-01T00:00:00"
        ),
        MagicMock(
            id=2,
            nickname="EmpresaY",
            trade_name="Empresa Y Soluções",
            legal_name="Empresa Y Soluções LTDA",
            cnpj="4567890123456",
            uf="SP",
            city="São Paulo",
            logo="empresaY.png",
            created_at="2025-01-02T00:00:00"
        )
    ]

    response = client.get(
        "/companies/list_companies",
        headers={"Authorization": f"Bearer {mock_auth_token}"}
    )

    assert response.status_code == 200, f"Falha: {response.json()}"
    data = response.json()
    assert len(data) == 2
    assert data[0]["nickname"] == "EmpresaX"
    assert data[1]["nickname"] == "EmpresaY"


def test_delete_company_success(client, mock_auth_token, mock_company_repository):
    """Testa a exclusão de uma empresa com sucesso."""
    mock_company_repository.delete_company.return_value = True

    response = client.delete(
        "/companies/delete_company/1",
        headers={"Authorization": f"Bearer {mock_auth_token}"}
    )

    assert response.status_code == 200, f"Falha: {response.json()}"
    data = response.json()
    assert data["message"] == "Company deleted"

    mock_company_repository.delete_company.assert_called_once_with(1)


def test_delete_company_not_found(client, mock_auth_token, mock_company_repository):
    """Testa a tentativa de exclusão de uma empresa inexistente."""
    mock_company_repository.delete_company.return_value = False

    response = client.delete(
        "/companies/delete_company/999",
        headers={"Authorization": f"Bearer {mock_auth_token}"}
    )

    assert response.status_code == 404, f"Falha: {response.json()}"
    data = response.json()
    assert data["detail"] == "Company not found"

    mock_company_repository.delete_company.assert_called_once_with(999)

