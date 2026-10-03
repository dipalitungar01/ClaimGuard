from sqlalchemy import Column, Integer, String, Float
from app.database import Base


class Policy(Base):
    __tablename__ = "policies"

    id = Column(Integer, primary_key=True, index=True)
    policy_number = Column(String(50), unique=True, nullable=False)
    policy_type = Column(String(50), nullable=False)
    premium = Column(Float, nullable=False)
    coverage_amount = Column(Float, nullable=False)
