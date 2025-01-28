from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.company import Company

class ICompanyRepository(ABC):
    @abstractmethod
    def create_company(self, company: Company) -> Company:
        """Cadastrar uma nova empresa."""
        pass

    @abstractmethod
    def get_companies(self) -> List[Company]:
        """Listar todas as empresas."""
        pass

    @abstractmethod
    def get_company_by_id(self, company_id: int) -> Optional[Company]:
        """Buscar empresa por ID."""
        pass

    @abstractmethod
    def delete_company(self, company_id: int) -> bool:
        """Excluir uma empresa pelo ID. Retorna True se excluiu, False se não encontrada."""
        pass
