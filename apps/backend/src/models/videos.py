from pydantic import BaseModel


class SimpleVideoResponse(BaseModel):
    id: int
    label: str
    description: str

    class Config:
        from_attributes = True


class VideoResponse(SimpleVideoResponse):
    file_url: str


class CreateVideoRequest(BaseModel):
    label: str
    description: str


class UpdateVideoRequest(BaseModel):
    label: str | None
    description: str | None
