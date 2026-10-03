from pydantic import BaseModel


class UserCreate(BaseModel):

    # Create account
    name: str
    email: str
    password: str


class UserLogin(BaseModel):

    # Login account
    email: str
    password: str


class ForgotPassword(BaseModel):

    # Forgot password
    email: str

class ResetPassword(BaseModel):

    # Reset password
    email: str
    new_password: str    