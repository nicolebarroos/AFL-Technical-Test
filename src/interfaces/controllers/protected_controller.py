from fastapi import APIRouter, Depends
from infrastructure.dependencies import get_current_user
from domain.entities.user import User

router = APIRouter()

@router.get("/protected")
async def protected_route(current_user: User = Depends(get_current_user)):
    return {"message": f"Hello {current_user.email}"}