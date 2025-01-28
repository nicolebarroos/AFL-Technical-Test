from pydantic import BaseModel, ConfigDict
from datetime import datetime

class CompanyCreate(BaseModel):
    nickname: str
    trade_name: str
    legal_name: str
    cnpj: str
    uf: str
    city: str
    logo: str

class CompanyResponse(BaseModel):
    id: int
    nickname: str
    trade_name: str
    legal_name: str
    cnpj: str
    uf: str
    city: str
    logo: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)