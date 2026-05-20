from fastapi import APIRouter, status, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette.datastructures import UploadFile

from api.dependencies import database, get_video_service
from schemas.videos import SimpleVideoResponse, CreateVideoRequest, UpdateVideoRequest
from services.video_service import VideoService

router = APIRouter(prefix="/videos", tags=["videos"])


@router.post("/upload", response_model=SimpleVideoResponse)
def upload_video(
        request: CreateVideoRequest,
        file: UploadFile,
        video_service: VideoService = Depends(get_video_service)
):
    return video_service.upload_video(request, file)


@router.get("", response_model=list[SimpleVideoResponse])
def list_videos(video_service: VideoService = Depends(get_video_service)):
    return video_service.list_videos()


@router.get("{video_id}", response_model=SimpleVideoResponse)
def get_video(video_id: int, db: Session = Depends(database)):
    video = VideoService.get_video(db, video_id)
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    return video


@router.patch("/{video_id}", response_model=SimpleVideoResponse | None)
def update_video(video_id: int, request: UpdateVideoRequest, db: Session = Depends(database)):
    video = VideoService.update_video(db, video_id, request)
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    return video


@router.patch("/{video_id}")
def delete_video(video_id: int, db: Session = Depends(database)):
    video_id = VideoService.delete_video(db, video_id)
    if not video_id:
        raise HTTPException(status_code=404, detail="Video not found")
    return video_id
