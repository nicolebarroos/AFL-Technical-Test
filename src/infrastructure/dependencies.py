from fastapi import Depends
from src.application.use_cases.contract_use_case import ContractUseCase
from src.domain.interfaces.i_contract_repository import IContractRepository
from src.infrastructure.repositories.contract_repository import ContractRepository
from src.application.use_cases.company_use_case import CompanyUseCase
from src.domain.interfaces.i_company_repository import ICompanyRepository
from src.infrastructure.repositories.company_repository import CompanyRepository
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

def get_company_repository() -> ICompanyRepository:
    return CompanyRepository()

def get_company_use_case(
    repo: ICompanyRepository = Depends(get_company_repository)
) -> CompanyUseCase:
    return CompanyUseCase(repo)

def get_contract_repository() -> IContractRepository:
    return ContractRepository()

def get_company_repository() -> ICompanyRepository:
    return CompanyRepository()

def get_contract_use_case(
    contract_repo: IContractRepository = Depends(get_contract_repository),
    company_repo: ICompanyRepository = Depends(get_company_repository)
) -> ContractUseCase:
    return ContractUseCase(contract_repo, company_repo)