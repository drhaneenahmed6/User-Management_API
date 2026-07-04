from fastapi import FastAPI,  Depends
from database import engine, SessionLocal
import models
import crud
from sqlalchemy.orm import Session
from schemas import UserCreate, UserResponse


models.Base.metadata.create_all(bind=engine)


app = FastAPI()
models.Base.metadata.create_all( bind=engine)

def get_db():
    db=SessionLocal()

    try:
        yield db

    finally:
        db.close()



@app.post("/users", response_model=UserResponse)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return crud.create_user(db, user)


@app.get("/users", response_model=list[UserResponse])
def get_users(
    db: Session = Depends(get_db)
    ):
    return crud.get_users(db)



@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(
    user_id:int,
    db: Session = Depends(get_db)
    ):
    return crud.get_user(db, user_id)


@app.put("/users/{user_id}", response_model=UserResponse)
def put_user(
    user_id:int,
    user : UserCreate,
    db: Session = Depends(get_db)
    ):
    return crud.update_user(db, user_id, user)



@app.delete("/users/{user_id}")
def delete_user(
    user_id=int,
    db: Session = Depends(get_db)
    ):
    return crud.delete_user(db, user_id)









