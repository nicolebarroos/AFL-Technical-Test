from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Dict, List

class ContractCreate(BaseModel):
    validity_date: str
    signing_date: str
    fee: float
    company_id: int
    services: Optional[Dict[str, List[str]]] = Field(
        default=None,
        example={
            "Department A": ["COMPRA", "VENDA"],
            "Department B": ["TROCA"]
        },
    )

class ContractResponse(BaseModel):
    validity_date: datetime = Field(..., example="2025-01-01T00:00:00")
    signing_date: datetime = Field(..., example="2025-06-01T00:00:00")
    fee: float = Field(..., gt=0, example=5.0)
    company_id: int = Field(..., example=1)
    services: Optional[Dict[str, List[str]]] = Field(
        default={
            "Department A": ["COMPRA", "VENDA", "TROCA"],
            "Department B": ["COMPRA", "VENDA", "TROCA"],
        },
        example={
            "Department A": ["COMPRA"],
            "Department B": ["VENDA", "TROCA"]
        },
    )

    class Config:
        orm_mode = True