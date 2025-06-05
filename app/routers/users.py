from .. import model,schema,utilis
from sqlalchemy.orm import Session
from ..database import get_db
from fastapi import Response, Depends, HTTPException, status, APIRouter

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.post("/", status_code=status.HTTP_201_CREATED,response_model=schema.UserOutput)
def create_user(user: schema.UserCreate,db: Session = Depends(get_db)):
    # Hash the password
    hashed_password = utilis.hash(user.password)
    user.password = hashed_password
    new_user = model.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return  new_user

 
@router.get("/{id}", response_model=schema.UserOutput)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} was not found")
    return user