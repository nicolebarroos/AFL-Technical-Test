from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from src.infrastructure.database import Base

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String, index=True)
    trade_name = Column(String)
    legal_name = Column(String)
    cnpj = Column(String, unique=True, index=True)
    uf = Column(String)
    city = Column(String)
    logo = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    contracts = relationship("Contract", back_populates="company", cascade="all, delete-orphan")

    def __init__(
        self,
        nickname: str,
        trade_name: str,
        legal_name: str,
        cnpj: str,
        uf: str,
        city: str,
        logo: str,
        created_at: datetime = None
    ):
        self.nickname = nickname
        self.trade_name = trade_name
        self.legal_name = legal_name
        self.cnpj = cnpj
        self.uf = uf
        self.city = city
        self.logo = logo
        self.created_at = created_at or datetime.utcnow()

    def add_contract(self, contract):
        self.contracts.append(contract)
