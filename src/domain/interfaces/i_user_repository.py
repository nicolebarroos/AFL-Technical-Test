from abc import ABC, abstractmethod
from src.domain.entities.user import User

class UserRepository(ABC):
    @abstractmethod
    def get_user_by_email(self, email: str) -> User:
        """Obtém um usuário pelo email."""
        pass

    @abstractmethod
    def create_user(self, user: User) -> User:
        """Cria um novo usuário."""
        pass
