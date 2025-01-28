from src.domain.entities.company import Company
from src.domain.entities.contract import Contract
from datetime import datetime

def test_create_contract():
    company = Company(
        nickname="EmpresaTest",
        trade_name="Empresa Test LTDA",
        legal_name="Empresa Test LTDA",
        cnpj="12345678000190",
        uf="SP",
        city="São Paulo",
        logo="test.png"
    )
    contract = Contract(
        validity_date="01-01-2025",
        signing_date="01-06-2025",
        fee=10.0,
        company=company
    )
    assert contract.validity_date.year == 2025
    assert contract.company.nickname == "EmpresaTest"
