from fastapi import APIRouter, Depends, HTTPException
from typing import List
from src.infrastructure.auth import get_current_user
from src.application.use_cases.contract_use_case import ContractUseCase
from src.infrastructure.dependencies import get_contract_use_case
from src.interfaces.schemas.contract_schema import ContractCreate, ContractResponse

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

@router.get("/list_contracts", response_model=List[ContractResponse])
def list_contracts(use_case: ContractUseCase = Depends(get_contract_use_case)):
    return use_case.list_contracts()
