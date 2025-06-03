from fastapi import APIRouter, HTTPException, status

from ..schemas import user as user_schemas

# Create a new APIRouter instance
# We can define a prefix and tags for all routes in this router
router = APIRouter(
    prefix="/auth",  # All routes in this router will start with /auth
    tags=["authentication"],  # Tag for OpenAPI documentation
    responses={404: {"description": "Not found"}}, # Default response for not found
)

# In-memory "database" for storing users during development (temporary)
fake_users_db = {}

# Example endpoint for login (we will implement this later)
@router.post("/login")
async def login_for_access_token():
    # This is just a placeholder for now
    # Actual login logic will be implemented later
    return {"message": "Login endpoint placeholder"}

# Updated registration endpoint
@router.post("/register", response_model=user_schemas.User)
async def register_user(new_user: user_schemas.UserCreate):
    """
    Register a new user.
    - Receives user data (username, email, password).
    - For now, it simulates user creation and returns user data (without password).
    - TODO: Implement password hashing and database storage.
    """
    user_id_counter = len(fake_users_db) + 1
    # Check if username or email already exists (in our fake DB)
    for user_in_db in fake_users_db.values():
        if user_in_db["username"] == new_user.username:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already registered"
            )
        if user_in_db["email"] == new_user.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
    # Simulate storing the user (we're not hashing password yet)
    fake_users_db[user_id_counter] = {
        "id": user_id_counter,
        "username": new_user.username,
        "email": new_user.email,
        "hashed_password": f"fake_hashed_{new_user.password}",
        "is_active": True
    }
    # Return the created user data (without password, as per User schema)
    return user_schemas.User(
        id=user_id_counter,
        username=new_user.username,
        email=new_user.email,
        is_active=True
    )
