from typing import Any

from fastapi import APIRouter, Depends, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr

from app.api.depends import get_current_active_user, get_current_active_superuser
from app.models.user import User
from app.schemas.user import UserRead, UserUpdate
from app.api.depends import get_db
from sqlalchemy.orm import Session
from app.crud.user import crud_user

router = APIRouter()


@router.get("/me", response_model=UserRead, response_model_exclude={"password"})
def read_user_me(current_user: User = Depends(get_current_active_user)) -> UserRead:
    return current_user


@router.patch('/me', response_model=UserRead, response_model_exclude={"password"})
def update_user_me(*, db: Session = Depends(get_db), password: str = Body(None), email: EmailStr = Body(None), current_user: User = Depends(get_current_active_user)):
    current_user_data = jsonable_encoder(current_user)
    user_in = UserUpdate(**current_user_data)
    if password:
        user_in.password = password
    else:
        del user_in.password
    if email:
        user_has_same_email = crud_user.get_by_email(db=db, email=email)
        if user_has_same_email:
            raise HTTPException(status_code=400, detail="Email already registered")
        else:
            user_in.email = email
    user = crud_user.update(db, db_obj=current_user, obj_in=user_in)
    return user


@router.get("/{user_id}", response_model=UserRead, response_model_exclude={"password"})
def read_user_by_id(user_id: int, current_user: User = Depends(get_current_active_superuser), db: Session = Depends(get_db)) -> Any:
    user = crud_user.get(db, id=user_id)
    return user


@router.patch("/{user_id}", response_model=UserRead, response_model_exclude={"password"})
def update_user(*, user_id: int, user_in: UserUpdate, current_user: User = Depends(get_current_active_superuser), db: Session = Depends(get_db)) -> Any:
    user = crud_user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this user id does not exist in the system",
        )
    user = crud_user.update(db, db_obj=user, obj_in=user_in)
    return user
