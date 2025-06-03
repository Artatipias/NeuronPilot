from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserBase(BaseModel):
    """
    Base model for user data, containing common fields.
    """
    email: EmailStr  # Ensures the email is in a valid format
    username: str = Field(..., min_length=3, max_length=50) # Username with length constraints

class UserCreate(UserBase):
    """
    Pydantic model for creating a new user.
    Inherits from UserBase and adds the password field.
    """
    password: str = Field(..., min_length=8) # Password with minimum length

class UserLogin(BaseModel):
    """
    Pydantic model for user login.
    Uses 'username' which can be either the actual username or email.
    """
    username: str # This can be email or username
    password: str

class UserInDBBase(UserBase):
    """
    Base model for user data as stored in the database.
    Includes an ID and potentially other DB-specific fields.
    """
    id: int
    is_active: Optional[bool] = True # Optional field, defaults to True

    class Config:
        # This was orm_mode in Pydantic v1, now from_attributes in Pydantic v2
        # It allows the model to be created from ORM objects (e.g., SQLAlchemy models)
        from_attributes = True

class User(UserInDBBase):
    """
    Pydantic model for representing a user, typically for API responses.
    This model will be returned when fetching user details.
    (Currently same as UserInDBBase, but can be extended)
    """
    pass # For now, it's the same as UserInDBBase

class Token(BaseModel):
    """
    Pydantic model for the JWT access token.
    """
    access_token: str
    token_type: str

class TokenData(BaseModel):
    """
    Pydantic model for data payload within a JWT token.
    """
    username: Optional[str] = None
    # You can add other fields like user_id, roles, etc.
