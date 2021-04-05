from sqlalchemy import Column,  Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = 'Users'
    __tablename__ = {
        'comment' : 'Пользователи'
    }

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        unique=True,
        nullable=True
    )

nickname = Column(String, comment='Никнейм', unique=True)
password = Column(String, comment='Пароль')
role = Column(String, comment='Роли')

def __repr__(self):
    return f'{self.id} {self.nickname} {self.password} {self.role}'
