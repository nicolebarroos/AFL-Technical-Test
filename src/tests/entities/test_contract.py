from domain.entities.contract import Contract
from datetime import datetime

def test_create_contract():
    contract = Contract(
        validity_date="01-01-2025",
        signing_date="01-12-2024",
        fee=10.5,
        company="Test Company"
    )
    assert contract.validity_date == datetime(2025, 1, 1)
    assert contract.signing_date == datetime(2024, 12, 1)
    assert contract.fee == 10.5
    
    assert "BUY" in contract.services["Department A"]
    assert "SELL" in contract.services["Department B"]
    assert "EXCHANGE" in contract.services["Department A"]

    assert contract.company == "Test Company"
