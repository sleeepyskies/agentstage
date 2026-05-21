from typing import Generator, Annotated

from fastapi import Request, Depends
from sqlalchemy.orm import Session

from repositories.video_repository import VideoRepository
from services.video_service import VideoService


def database(request: Request) -> Generator[Session, None, None]:
    """
    Provides a database session per request and handles auto closing the connection.

    :param request: FastAPI request object.
    :return: Database session.
    """
    db = request.app.state.SessionLocal()

    try:
        yield db
    finally:
        db.close()


DBSession = Annotated[Session, Depends(database)]


def get_video_service(db: DBSession) -> VideoService:
    """Provides access to the VideoService."""
    video_repository = VideoRepository(db)
    return VideoService(video_repository)
