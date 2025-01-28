from fastapi import APIRouter, Depends, HTTPException, Query
from src.infrastructure.database import db_instance
from src.infrastructure.auth import get_current_user
from src.application.use_cases.contract_use_case import ContractUseCase
from src.infrastructure.dependencies import get_contract_use_case
from src.interfaces.schemas.contract_schema import ContractCreate, ContractResponse
from sqlalchemy.orm import Session

router = APIRouter(dependencies=[Depends(get_current_user)])

@router.post("/create_contract", response_model=ContractResponse)
def create_contract(request: ContractCreate, use_case: ContractUseCase = Depends(get_contract_use_case)):
    contract = use_case.create_contract(
        validity_date=request.validity_date,
        signing_date=request.signing_date,
        fee=request.fee,
        company_id=request.company_id,
        services=request.services
    )
    if not contract:
        raise HTTPException(status_code=400, detail="Could not create contract (company might not exist)")
    return contract

@router.get("/list_contracts", summary="List contracts with pagination and sorting")
def list_contracts(
        page: int = Query(1, ge=1, description="Page number"),
        page_size: int = Query(10, ge=1, le=100, description="Page size"),
        sort_by: str = Query("signing_date", description="Column to sort by"),
        order: str = Query("asc", regex="^(asc|desc)$", description="Sort order (asc or desc)"),
        use_case: ContractUseCase = Depends(get_contract_use_case),
        db: Session = Depends(db_instance.get_session)
    ):
    try:
        result = use_case.list_contracts(db, page, page_size, sort_by, order)
        return result
    except ValueError as e:
        return {"error": str(e)}

