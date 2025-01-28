from sqlalchemy.orm import Session
from sqlalchemy import func
from src.domain.entities.contract import Contract
from src.domain.entities.company import Company
from src.domain.interfaces.i_metrics_repository import IMetricsRepository

class MetricsRepository(IMetricsRepository):
    def get_total_value_in_millions(self, db: Session) -> float:
        return db.query(func.sum(Contract.fee) / 1_000_000).scalar() or 0.0

    def get_total_active_contracts(self, db: Session) -> int:
        return db.query(func.count(Contract.id)).scalar() or 0

    def get_average_fee_per_company(self, db: Session):
        result = db.query(Company.nickname, func.avg(Contract.fee)).join(Contract).group_by(Company.id).all()
        return [{"nickname": row[0], "average_fee": float(row[1])} for row in result]

    def get_contracts_by_state(self, db: Session):
        result = db.query(Company.uf, func.count(Contract.id)).join(Contract).group_by(Company.uf).all()
        return [{"state": row[0], "contract_count": row[1]} for row in result]

