from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from src.interfaces.schemas.user_schema import UserResponse
from src.infrastructure.dependencies import get_auth_use_case
from src.application.use_cases.auth_use_case import AuthUseCase
from src.domain.entities.user import User

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    
class RegisterRequest(BaseModel):
    email: str
    password: str

@router.post("/register", response_model=UserResponse)
async def register_user(
    request: RegisterRequest,
    use_case: AuthUseCase = Depends(get_auth_use_case)
):
    new_user = use_case.register_user(request.email, request.password)
    if not new_user:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    return new_user

@router.post("/login", response_model=TokenResponse)
async def login(
    request: LoginRequest,
    use_case: AuthUseCase = Depends(get_auth_use_case)
):
    token = use_case.login(request.email, request.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return TokenResponse(access_token=token)
