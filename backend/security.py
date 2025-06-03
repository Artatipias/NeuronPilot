from passlib.context import CryptContext

# Configure the CryptContext for password hashing
# We will use bcrypt as the hashing algorithm
# schemes=["bcrypt"] specifies the default and only scheme
# deprecated="auto" will automatically mark older schemes as deprecated if we add more later
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies a plain password against a stored hashed password.
    """
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """
    Hashes a plain password using bcrypt.
    """
    return pwd_context.hash(password)
