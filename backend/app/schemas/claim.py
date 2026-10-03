from pydantic import BaseModel, ConfigDict


class ClaimCreate(BaseModel):
    claim_number: str
    claim_amount: float


class ClaimResponse(BaseModel):
    id: int
    claim_number: str
    claim_amount: float
    status: str
    fraud_score: float

    model_config = ConfigDict(from_attributes=True)
