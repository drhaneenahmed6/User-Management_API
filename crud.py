from sqlalchemy.orm import Session
from models import User 
from schemas import UserCreate
from fastapi import HTTPException




def create_user(db: Session, user: UserCreate):
    
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    new_user = User(
        name=user.name,
        email=user.email,
        age=user.age
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_users(db: Session):
    users = db.query(User).all()
    return users


def get_user(db: Session, user_id: int):

    existing_user = db.query(User).filter(User.id == user_id).first()

    if not existing_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return existing_user


def update_user(db: Session, user_id, user: UserCreate):

    existing_user = db.query(User).filter(User.id == user_id).first()

    if not existing_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    

    existing_email = db.query(User).filter(User.email == user.email).first()

    if existing_email and existing_email.id != user_id:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    existing_user.name = user.name
    existing_user.email = user.email
    existing_user.age = user.age

    db.commit()
    db.refresh(existing_user)

    return existing_user




def delete_user(db: Session ,user_id:int):
    existing_user= db.query(User).filter(User.id == user_id).first()

    if not existing_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    
    db.delete(existing_user)

    db.commit()

    return {
        "message": "User deleted successfully"
    }
