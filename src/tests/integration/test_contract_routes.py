import pytest
from unittest.mock import MagicMock
from fastapi.testclient import TestClient
from src.main import app
from src.infrastructure.dependencies import get_contract_use_case
from src.application.use_cases.contract_use_case import ContractUseCase
from src.infrastructure.auth import create_access_token
from datetime import datetime

@pytest.fixture
def mock_contract_repository():
    """Mocka o repositório de contratos."""
    mock_repo = MagicMock()
    return mock_repo


@pytest.fixture
def mock_company_repository():
    """Mocka o repositório de empresas."""
    mock_repo = MagicMock()
    return mock_repo


@pytest.fixture
def mock_contract_use_case(mock_contract_repository, mock_company_repository):
    """Mocka o caso de uso de contratos."""
    return ContractUseCase(
        contract_repo=mock_contract_repository,
        company_repo=mock_company_repository
    )


@pytest.fixture
def mock_auth_token():
    """Simula login e retorna um token de autenticação mockado."""
    token = create_access_token(data={"sub": "test@example.com"})
    return token


@pytest.fixture
def client(mock_contract_use_case):
    """Configura o cliente de teste com dependências mockadas."""
    app.dependency_overrides[get_contract_use_case] = lambda: mock_contract_use_case
    return TestClient(app)


def test_create_contract_success(client, mock_auth_token, mock_contract_repository, mock_company_repository):
    """Testa a criação de um contrato com sucesso."""
    mock_company_repository.get_company_by_id.return_value = MagicMock(
        id=1,
        nickname="EmpresaX"
    )

    mock_contract_repository.create_contract.return_value = MagicMock(
        id=1,
        validity_date=datetime.strptime("01-01-2025", "%d-%m-%Y").date(),
        signing_date=datetime.strptime("01-01-2025", "%d-%m-%Y").date(),
        fee=1000.0,
        company=MagicMock(nickname="EmpresaX"),
        services={
            "Department A": ["COMPRA"],
            "Department B": ["VENDA", "TROCA"]
        },
    )

    response = client.post(
        "/contracts/create_contract",
        json={
            "validity_date": "01-01-2025",
            "signing_date": "01-01-2025",
            "fee": 1000.0,
            "company_id": 1,
            "services": {
                "Department A": ["COMPRA"],
                "Department B": ["VENDA", "TROCA"]
            }
        },
        headers={"Authorization": f"Bearer {mock_auth_token}"}
    )

    assert response.status_code == 200, f"Falha: {response.json()}"
    data = response.json()
    assert data["fee"] == 1000.0
    assert data["services"] == {
        "Department A": ["COMPRA"],
        "Department B": ["VENDA", "TROCA"]
    }


def test_create_contract_company_not_found(client, mock_auth_token, mock_contract_repository, mock_company_repository):
    """Testa a criação de contrato quando a empresa não existe."""
    mock_company_repository.get_company_by_id.return_value = None

    response = client.post(
        "/contracts/create_contract",
        json={
            "validity_date": "01-01-2025",
            "signing_date": "01-01-2025",
            "fee": 1000.0,
            "company_id": 999,
            "services": {
                "Department A": ["COMPRA"],
                "Department B": ["VENDA", "TROCA"]
            }
        },
        headers={"Authorization": f"Bearer {mock_auth_token}"}
    )

    assert response.status_code == 400, f"Falha: {response.json()}"
    data = response.json()
    assert data["detail"] == "Company not found"