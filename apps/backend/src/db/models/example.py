from sqlalchemy import Integer, Column, String

from db.base import Base


class Example(Base):
    __tablename__ = "example"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)