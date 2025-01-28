from typing import Optional
from src.domain.entities.contract import Contract
from src.domain.entities.company import Company
from src.domain.interfaces.i_contract_repository import IContractRepository
from src.domain.interfaces.i_company_repository import ICompanyRepository
from sqlalchemy.orm import Session
class ContractUseCase:
    def __init__(self, contract_repo: IContractRepository, company_repo: ICompanyRepository):
        self.contract_repo = contract_repo
        self.company_repo = company_repo

    def create_contract(
        self,
        validity_date: str,
        signing_date: str,
        fee: float,
        company_id: int,
        services: Optional[dict] = None
    ) -> Contract:
        company = self.company_repo.get_company_by_id(company_id)
        if not company:
            raise ValueError("Company not found")

        if services is None:
            services = {
                "Department A": ["COMPRA", "VENDA", "TROCA"],
                "Department B": ["COMPRA", "VENDA", "TROCA"]
            }

        contract = Contract(
            validity_date=validity_date,
            signing_date=signing_date,
            fee=fee,
            company=company,
            services=services
        )
        return self.contract_repo.create_contract(contract, company_id)

    def list_contracts(self, db: Session, page: int = 1, page_size: int = 10, sort_by: str = "signing_date", order: str = "asc"):
        return self.contract_repo.list_contracts(
            db, page, page_size, sort_by, order
        )

    def delete_contract(self, contract_id: int) -> bool:
        return self.contract_repo.delete_contract(contract_id)

    def get_contract_by_id(self, contract_id: int) -> Optional[Contract]:
        return self.contract_repo.get_contract_by_id(contract_id)
