from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.entities.company import Company
from src.domain.entities.contract import Contract
from src.domain.interfaces.i_contract_repository import IContractRepository
from src.infrastructure.database import db_instance

class ContractRepository(IContractRepository):
    def __init__(self):
        self.db: Session = db_instance.get_session()

    def create_contract(self, contract: Contract, company_id: int) -> Optional[Contract]:
        try:
            company = self.db.query(Company).filter(Company.id == company_id).first()
            if not company:
                raise ValueError("Company not found")

            contract.company = company

            self.db.add(contract)
            self.db.commit()
            self.db.refresh(contract)
            return contract
        except Exception as e:
            print(f"Erro ao criar contrato: {e}")
            self.db.rollback()
            return None


    def get_contracts(self) -> List[Contract]:
        return self.db.query(Contract).all()

    def delete_contract(self, contract_id: int) -> bool:
        contract = self.get_contract_by_id(contract_id)
        if not contract:
            return False
        self.db.delete(contract)
        self.db.commit()
        return True

    def get_contract_by_id(self, contract_id: int) -> Optional[Contract]:
        return self.db.query(Contract).filter(Contract.id == contract_id).first()
