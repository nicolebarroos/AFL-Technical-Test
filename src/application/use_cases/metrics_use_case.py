from sqlalchemy.orm import Session
from src.domain.interfaces.i_metrics_repository import IMetricsRepository

class MetricsUseCase:
    def __init__(self, metrics_repository: IMetricsRepository):
        self.metrics_repository = metrics_repository

    def get_total_value_in_millions(self, db: Session) -> float:
        return self.metrics_repository.get_total_value_in_millions(db)

    def get_total_active_contracts(self, db: Session) -> int:
        return self.metrics_repository.get_total_active_contracts(db)

    def get_average_fee_per_company(self, db: Session):
        return self.metrics_repository.get_average_fee_per_company(db)

    def get_contracts_by_state(self, db: Session):
        return self.metrics_repository.get_contracts_by_state(db)