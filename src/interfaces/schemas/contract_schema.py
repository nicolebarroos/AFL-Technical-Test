from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional, Dict, List

class ContractCreate(BaseModel):
    validity_date: str
    signing_date: str
    fee: float
    company_id: int
    services: Optional[Dict[str, List[str]]] = Field(default=None)

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "validity_date": "2025-01-01",
                    "signing_date": "2025-01-06",
                    "fee": 100.0,
                    "company_id": 1,
                    "services": {
                        "Department A": ["COMPRA", "VENDA"],
                        "Department B": ["TROCA"]
                    },
                }
            ]
        }
    )

class ContractResponse(BaseModel):
    validity_date: datetime
    signing_date: datetime
    fee: float
    company_id: int
    services: Optional[Dict[str, List[str]]] = Field(default=None)

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "validity_date": "2025-01-01T00:00:00",
                    "signing_date": "2025-06-01T00:00:00",
                    "fee": 5.0,
                    "company_id": 1,
                    "services": {
                        "Department A": ["COMPRA"],
                        "Department B": ["VENDA", "TROCA"]
                    },
                }
            ]
        }
    )