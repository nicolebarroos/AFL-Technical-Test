from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.infrastructure.auth import get_current_user
from src.application.use_cases.metrics_use_case import MetricsUseCase
from src.infrastructure.dependencies import get_metrics_use_case
from src.infrastructure.database import db_instance

router = APIRouter(dependencies=[Depends(get_current_user)])

@router.get("/total_value")
def get_total_value_in_millions(use_case: MetricsUseCase = Depends(get_metrics_use_case), db: Session = Depends(db_instance.get_session)):
    total_value = use_case.get_total_value_in_millions(db)
    return {"total_value_in_millions": round(total_value, 2)}

@router.get("/total_count")
def get_total_active_contracts(use_case: MetricsUseCase = Depends(get_metrics_use_case), db: Session = Depends(db_instance.get_session)):
    total_contracts = use_case.get_total_active_contracts(db)
    return {"total_active_contracts": total_contracts}

@router.get("/average_fee")
def get_average_fee_per_company(use_case: MetricsUseCase = Depends(get_metrics_use_case), db: Session = Depends(db_instance.get_session)):
    average_fee = use_case.get_average_fee_per_company(db)
    return {"average_fee_per_company": average_fee}

@router.get("/by_state")
def get_contracts_by_state(use_case: MetricsUseCase = Depends(get_metrics_use_case), db: Session = Depends(db_instance.get_session)):
    contracts_by_state = use_case.get_contracts_by_state(db)
    return {"contracts_by_state": contracts_by_state}