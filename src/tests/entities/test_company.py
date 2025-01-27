from src.domain.entities.company import Company

def test_create_company():
    company = Company(
        nickname="Test Company",
        trade_name="Test Trade Name",
        legal_name="Test Legal Name",
        cnpj="12.345.678/0001-90",
        uf="CE",
        city="Fortaleza",
        logo="logo.png"
    )
    assert company.nickname == "Test Company"
    assert company.trade_name == "Test Trade Name"
    assert company.legal_name == "Test Legal Name"
    assert company.cnpj == "12.345.678/0001-90"
    assert company.uf == "CE"
    assert company.city == "Fortaleza"
    assert company.logo == "logo.png"
