from sqlalchemy import Column, Integer, String

from db.base import Base


class Video(Base):
    """
    Video Model.
    Videos are stored on disk and not within SQLite. Therefore, the table only holds a filepath and not a blob.
    """
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True)
    description = Column(String(4096), nullable=False)
    filename=Column(String(36), nullable=False) # we store filename as random UUID string
