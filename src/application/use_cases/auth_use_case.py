from src.domain.entities.user import User
from src.domain.interfaces.i_user_repository import UserRepository
from src.infrastructure.auth import create_access_token, authenticate_user

class AuthUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def login(self, email: str, password: str):
        user = authenticate_user(email, password, self.user_repository)
        if user:
            return create_access_token(data={"sub": user.email})
        return None
    
    def register_user(self, email: str, password: str):
        existing_user = self.user_repository.get_user_by_email(email)
        if existing_user:
            return None

        new_user = User(email=email, password=password)
        return self.user_repository.create_user(new_user)