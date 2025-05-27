from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from .. import model, schema, utilis
from ..database import get_db



router = APIRouter(tags=["Authentication"])

@router.post("/login")
def login(user_credentials:schema.UserLogin, db: Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.email == user_credentials.email).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
    
    if not utilis.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
    
    return {"token":"example_token"}

