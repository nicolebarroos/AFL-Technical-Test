from datetime import datetime
from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSON
from src.infrastructure.database import Base
from sqlalchemy.ext.mutable import MutableDict
class Contract(Base):
    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True, index=True)
    validity_date = Column(DateTime, nullable=False)
    signing_date = Column(DateTime, nullable=False)
    fee = Column(Float, nullable=False)
    services = Column(
        MutableDict.as_mutable(JSON),
        default=lambda: {
            "Department A": ["COMPRA", "VENDA", "TROCA"],
            "Department B": ["COMPRA", "VENDA", "TROCA"],
        },
    )
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    company = relationship("Company", back_populates="contracts")

    def __init__(
        self,
        validity_date: str,
        signing_date: str,
        fee: float,
        company: "Company" = None,
        services: dict = None
    ):
        try:
            self.validity_date = datetime.strptime(validity_date, "%d-%m-%Y")
            self.signing_date = datetime.strptime(signing_date, "%d-%m-%Y")
        except ValueError as e:
            raise ValueError(f"Invalid date format: {e}")

        if fee < 0:
            raise ValueError("Fee cannot be negative")

        self.fee = fee
        self.services = services or {
            "Department A": [],
            "Department B": []
        }
        if company:
            self.company = company