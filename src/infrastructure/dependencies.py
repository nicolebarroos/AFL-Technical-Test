from fastapi import Depends
from src.application.use_cases.auth_use_case import AuthUseCase
from src.domain.interfaces.i_user_repository import UserRepository
from src.infrastructure.repositories.user_repository import UserRepositoryImpl

def get_user_repository() -> UserRepositoryImpl:
    return UserRepositoryImpl()

def get_auth_use_case(user_repository: UserRepositoryImpl = Depends(get_user_repository)) -> AuthUseCase:
    return AuthUseCase(user_repository)

def get_user_repository() -> UserRepository:
    return UserRepositoryImpl()

def get_auth_use_case(user_repository: UserRepository = Depends(get_user_repository)) -> AuthUseCase:
    return AuthUseCase(user_repository)