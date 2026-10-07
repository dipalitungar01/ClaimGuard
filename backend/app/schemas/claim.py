from pydantic import BaseModel, ConfigDict, Field


class ClaimCreate(BaseModel):
    claim_number: str = Field(
        min_length=3,
        max_length=50
    )
    claim_amount: float = Field(
        gt=0
    )


class ClaimResponse(BaseModel):
    id: int
    claim_number: str
    claim_amount: float
    status: str
    fraud_score: float
    risk_level: str

    model_config = ConfigDict(from_attributes=True)