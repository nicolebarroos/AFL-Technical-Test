from abc import ABC, abstractmethod
from typing import List, Dict, Any
from sqlalchemy.orm import Session

class IMetricsRepository(ABC):
    @abstractmethod
    def get_total_value_in_millions(self, db: Session) -> float:
        """Retorna o valor total dos contratos em milhões."""
        pass

    @abstractmethod
    def get_total_active_contracts(self, db: Session) -> int:
        """Retorna a quantidade total de contratos ativos."""
        pass

    @abstractmethod
    def get_average_fee_per_company(self, db: Session) -> List[Dict[str, Any]]:
        """Retorna a média da taxa por empresa."""
        pass

    @abstractmethod
    def get_contracts_by_state(self, db: Session) -> List[Dict[str, Any]]:
        """Retorna a quantidade de contratos por estado."""
        pass
