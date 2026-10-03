from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate

from app.utils.password import hash_password, verify_password


def create_user(db: Session, user_data: UserCreate):

    # Check whether email already exists
    existing_user = db.query(User).filter(
        User.email == user_data.email
    ).first()

    if existing_user:
        return None

    # Hash the password
    hashed_password = hash_password(
        user_data.password
    )

    # Create new user object
    new_user = User(
        name=user_data.name,
        email=user_data.email,
        password=hashed_password,
        role="customer"
    )

    # Add user to database session
    db.add(new_user)

    # Save changes to MySQL
    db.commit()

    # Get generated ID and other database values
    db.refresh(new_user)

    return new_user


def login_user(db: Session, email: str, password: str):

    # Find user by email
    user = db.query(User).filter(
        User.email == email
    ).first()

    # Check whether email exists
    if user is None:
        return None

    # Check whether password is correct
    if not verify_password(
        password,
        user.password
    ):
        return None

    # Return user if login details are correct
    return user