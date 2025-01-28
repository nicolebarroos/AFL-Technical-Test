from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.entities.company import Company
from src.domain.interfaces.i_company_repository import ICompanyRepository
from src.infrastructure.database import db_instance

class CompanyRepository(ICompanyRepository):
    def __init__(self):
        self.db: Session = db_instance.get_session()

    def create_company(self, company: Company) -> Company:
        self.db.add(company)
        self.db.commit()
        self.db.refresh(company)
        return company

    def get_companies(self) -> List[Company]:
        return self.db.query(Company).all()

    def get_company_by_id(self, company_id: int) -> Optional[Company]:
        return self.db.query(Company).filter(Company.id == company_id).first()

    def delete_company(self, company_id: int) -> bool:
        company = self.get_company_by_id(company_id)
        if not company:
            return False
        self.db.delete(company)
        self.db.commit()
        return True
