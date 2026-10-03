from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database import get_db

from app.models.user import User

from app.schemas.user import UserCreate, UserLogin, ForgotPassword, ResetPassword

from app.services.user_service import create_user, login_user


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# =========================
# REGISTER
# =========================

@router.post("/")
def create_user_api(

    user: UserCreate,

    db: Session = Depends(get_db)

):

    return create_user(db, user)


# =========================
# GET USERS
# =========================

@router.get("/")
def get_users(

    db: Session = Depends(get_db)

):

    users = db.query(User).all()

    return users


# =========================
# LOGIN
# =========================

@router.post("/login")
def login_user_api(

    user: UserLogin,

    db: Session = Depends(get_db)

):

    logged_user = login_user(
        db,
        user.email,
        user.password
    )

    if logged_user is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return {

        "message": "Login successful",

        "user_id": logged_user.id,

        "name": logged_user.name,

        "email": logged_user.email,

        "role": logged_user.role

    }


# =========================
# FORGOT PASSWORD
# =========================

@router.post("/forgot-password")
def forgot_password(

    data: ForgotPassword,

    db: Session = Depends(get_db)

):

    user = db.query(User).filter(
        User.email == data.email
    ).first()

    if user is None:

        raise HTTPException(
            status_code=404,
            detail="Email not found"
        )

    return {
        "message": "Email found. Password reset can be done."
    }

# =========================
# RESET PASSWORD
# =========================

@router.post("/reset-password")
def reset_password(

    data: ResetPassword,

    db: Session = Depends(get_db)

):

    user = db.query(User).filter(
        User.email == data.email
    ).first()

    if user is None:

        raise HTTPException(
            status_code=404,
            detail="Email not found"
        )

    user.password = data.new_password

    db.commit()

    return {
        "message": "Password reset successful"
    }
