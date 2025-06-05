from jose import jwt, JWTError
from datetime import datetime, timedelta
import os 
from dotenv import load_dotenv

load_dotenv()


SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')  # Default to 30 minutes if not set

def create_access_token(data: dict):
    to_encode  = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

