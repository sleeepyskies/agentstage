from sqlalchemy import Column, Integer, String

from db.base import Base


class Video(Base):
    """
    Video Model.
    Videos are stored on disk and not within SQLite. Therefore, the table only holds a filepath and not a blob.
    """
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True)
    """Primary key for Video Model."""
    description = Column(String(4096), nullable=False)
    """User defined description of the video."""
    label=Column(String(512), nullable=False)
    """User defined name of the video."""
    filename=Column(String(36), nullable=False)
    """Backend UUID of the video."""
