from dataclasses import dataclass

from sqlalchemy import select, delete
from sqlalchemy.orm import Session

from db.models.videos import Video


@dataclass
class UpdateVideo:
    """Dataclass props used for updating a video."""
    description: str | None


class VideoRepository:
    """Provides access to the database for any Video related operations."""

    def __init__(self, database: Session) -> None:
        self.database = database

    def create(self, video: Video) -> Video:
        self.database.add(video)
        self.database.commit()
        self.database.refresh(video)
        return video

    def get(self, video_id: int) -> Video | None:
        return self.database.scalars(
            select(Video).where(Video.id == video_id)
        ).first()

    def list(self) -> list[Video]:
        return list(self.database.scalars(select(Video)).all())

    def update(self, video_id: int, new: UpdateVideo) -> Video | None:
        video = self.get(video_id)

        if not video or new.description is None:
            return None

        video.description = new.description

        self.database.commit()
        self.database.refresh(video)
        return video

    def delete(self, video_id: int) -> bool:
        result = self.database.execute(
            delete(Video).where(Video.id == video_id)
        )
        self.database.commit()
        return result.rowcount > 0
