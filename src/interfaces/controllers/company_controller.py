from fastapi import APIRouter, Depends, HTTPException
from typing import List
from src.interfaces.schemas.company_schema import CompanyCreate, CompanyResponse
from src.application.use_cases.company_use_case import CompanyUseCase
from src.infrastructure.dependencies import get_company_use_case

router = APIRouter()

@router.post("/create_company", response_model=CompanyResponse)
def create_company(
    request: CompanyCreate,
    use_case: CompanyUseCase = Depends(get_company_use_case)
):
    company = use_case.create_company(
        nickname=request.nickname,
        trade_name=request.trade_name,
        legal_name=request.legal_name,
        cnpj=request.cnpj,
        uf=request.uf,
        city=request.city,
        logo=request.logo
    )
    return company

@router.get("/list_companies", response_model=List[CompanyResponse])
def list_companies(use_case: CompanyUseCase = Depends(get_company_use_case)):
    return use_case.list_companies()

@router.delete("/delete_company/{company_id}")
def delete_company(company_id: int, use_case: CompanyUseCase = Depends(get_company_use_case)):
    success = use_case.delete_company(company_id)
    if not success:
        raise HTTPException(status_code=404, detail="Company not found")
    return {"message": "Company deleted"}
