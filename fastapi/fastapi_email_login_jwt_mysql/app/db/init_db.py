from sqlalchemy.orm import Session

from app.crud.user import crud_user
from app.schemas.user import UserCreate
from app.core.config import settings


def init_db(db: Session) -> None:
    user = crud_user.get_by_email(db, email=settings.FIRST_SUPERUSER_EMAIL)
    if not user:
        user_in = UserCreate(
            email=settings.FIRST_SUPERUSER_EMAIL,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True
        )
        crud_user.create_superuser(db=db, obj_in=user_in)
