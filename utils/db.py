from sqlalchemy.orm import Session

from database import models


def get_user(db: Session, user_id: int) -> models.User:
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_nickname(db: Session, nickname: str) -> models.User:
    return db.query(models.User).filter(models.User.nickname == nickname).first()
