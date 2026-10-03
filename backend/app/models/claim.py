from sqlalchemy import Column, Integer, String, Float
from app.database import Base


class Claim(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True, index=True)
    claim_number = Column(String(50), unique=True, nullable=False)
    claim_amount = Column(Float, nullable=False)
    status = Column(String(50), default="pending")
    fraud_score = Column(Float, default=0.0)
