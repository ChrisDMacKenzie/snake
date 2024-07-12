from sqlalchemy import Column, String, Integer
from .base import Base, BaseMixin

class Score(Base, BaseMixin):
    __tablename__ = 'scores'

    initials = Column(String(3))
    score = Column(Integer)