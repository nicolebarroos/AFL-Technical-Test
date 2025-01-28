from abc import ABC, abstractmethod
from typing import List, Optional, Dict
from src.domain.entities.contract import Contract
from sqlalchemy.orm import Session
class IContractRepository(ABC):
    @abstractmethod
    def create_contract(self, contract: Contract, company_id: int) -> Optional[Contract]:
        """Cria um novo contrato associado a uma determinada empresa."""
        pass

    @abstractmethod
    def list_contracts(self, db: Session, page: int = 1, page_size: int = 10, sort_by: str = "signing_date",order: str = "asc") -> Dict:
        """Lista contratoa com paginação e ordenação."""
        pass

    @abstractmethod
    def delete_contract(self, contract_id: int) -> bool:
        """Exclui um contrato pelo ID. Retorna True se excluiu, ou False se não encontrado."""
        pass

    @abstractmethod
    def get_contract_by_id(self, contract_id: int) -> Optional[Contract]:
        """Retorna um contrato específico pelo ID, ou None se não encontrado."""
        pass
