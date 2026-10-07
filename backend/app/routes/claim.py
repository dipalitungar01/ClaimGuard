from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from sqlalchemy.exc import IntegrityError

from app.database import SessionLocal

from app.models.claim import Claim

from app.schemas.claim import ClaimCreate, ClaimResponse


router = APIRouter(
    prefix="/claims",
    tags=["Claims"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# =========================
# CREATE CLAIM
# =========================

@router.post("/", response_model=ClaimResponse)
def create_claim(

    claim_data: ClaimCreate,

    db: Session = Depends(get_db)

):

    # Check if claim number already exists

    existing_claim = db.query(Claim).filter(
        Claim.claim_number == claim_data.claim_number
    ).first()

    if existing_claim:

        raise HTTPException(
            status_code=400,
            detail=f"Claim number {claim_data.claim_number} already exists. Please enter a different claim number."
        )


    # Fraud detection rule

    if claim_data.claim_amount > 50000:

        fraud_score = 70

        risk_level = "High Risk"

    else:

        fraud_score = 10

        risk_level = "Low Risk"


    # Create claim

    new_claim = Claim(

        claim_number=claim_data.claim_number,

        claim_amount=claim_data.claim_amount,

        status="pending",

        fraud_score=fraud_score,

        risk_level=risk_level

    )


    try:

        db.add(new_claim)

        db.commit()

        db.refresh(new_claim)

    except IntegrityError:

        db.rollback()

        raise HTTPException(
            status_code=400,
            detail="Claim number already exists. Please enter a different claim number."
        )


    return new_claim


# =========================
# GET ALL CLAIMS
# =========================

@router.get("/")
def get_claims(

    db: Session = Depends(get_db)

):

    claims = db.query(Claim).all()

    return claims


# =========================
# UPDATE CLAIM STATUS
# =========================

@router.put("/{claim_id}/status")
def update_claim_status(

    claim_id: int,
    new_status: str,
    db: Session = Depends(get_db)

):

    claim = db.query(Claim).filter(
        Claim.id == claim_id
    ).first()


    if not claim:

        raise HTTPException(
            status_code=404,
            detail="Claim not found."
        )


    allowed_statuses = [
        "pending",
        "under review",
        "approved",
        "rejected"
    ]


    if new_status.lower() not in allowed_statuses:

        raise HTTPException(
            status_code=400,
            detail="Invalid claim status."
        )


    claim.status = new_status.lower()

    db.commit()

    db.refresh(claim)

    return claim