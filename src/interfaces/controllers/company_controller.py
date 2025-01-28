from fastapi import APIRouter, Depends, HTTPException, File, Form, UploadFile
from typing import List
from src.infrastructure.auth import get_current_user
from src.interfaces.schemas.company_schema import CompanyResponse
from src.application.use_cases.company_use_case import CompanyUseCase
from src.infrastructure.dependencies import get_company_use_case
from sqlalchemy.exc import IntegrityError
import os

router = APIRouter(dependencies=[Depends(get_current_user)])

@router.post("/create_company", response_model=CompanyResponse)
def create_company(
    nickname: str = Form(...),
    trade_name: str = Form(...),
    legal_name: str = Form(...),
    cnpj: str = Form(...),
    uf: str = Form(...),
    city: str = Form(...),
    logo: UploadFile = File(...),
    use_case: CompanyUseCase = Depends(get_company_use_case)
    ):
    if not logo.filename.endswith(".png"):
        raise HTTPException(status_code=400, detail="Logo must be a .png file")

    try:
        upload_dir = "uploaded_images"
        os.makedirs(upload_dir, exist_ok=True)

        file_path = os.path.join(upload_dir, logo.filename)

        logo_content = logo.file.read()

        with open(file_path, "wb") as image_file:
            image_file.write(logo_content)

        company = use_case.create_company(
            nickname=nickname,
            trade_name=trade_name,
            legal_name=legal_name,
            cnpj=cnpj,
            uf=uf,
            city=city,
            logo=file_path
        )
        return company
    except IntegrityError as e:
        if "duplicate key value violates unique constraint" in str(e.orig):
            raise HTTPException(status_code=400, detail="CNPJ já existe no sistema.")
        raise HTTPException(status_code=500, detail="Erro ao processar a solicitação.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro inesperado: {str(e)}")

@router.get("/list_companies", response_model=List[CompanyResponse])
def list_companies(use_case: CompanyUseCase = Depends(get_company_use_case)):
    try:
        return use_case.list_companies()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching companies: {str(e)}")

@router.delete("/delete_company/{company_id}")
def delete_company(company_id: int, use_case: CompanyUseCase = Depends(get_company_use_case)):
    try:
        success = use_case.delete_company(company_id)
        if not success:
            raise HTTPException(status_code=404, detail="Company not found")
        return {"message": "Company deleted"}
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
