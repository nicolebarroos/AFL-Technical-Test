from typing import List, Optional
from src.domain.entities.company import Company
from src.domain.interfaces.i_company_repository import ICompanyRepository

class CompanyUseCase:
    def __init__(self, company_repository: ICompanyRepository):
        self.company_repository = company_repository

    def create_company(
        self,
        nickname: str,
        trade_name: str,
        legal_name: str,
        cnpj: str,
        uf: str,
        city: str,
        logo: str
    ) -> Company:
        company = Company(nickname, trade_name, legal_name, cnpj, uf, city, logo)
        return self.company_repository.create_company(company)

    def list_companies(self) -> List[Company]:
        return self.company_repository.get_companies()

    def delete_company(self, company_id: int) -> bool:
        return self.company_repository.delete_company(company_id)
