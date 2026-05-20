from pydantic import BaseModel


class SimpleVideoResponse(BaseModel):
    id: int
    filename: str
    description: str

    class Config:
        from_attributes = True

class VideoResponse(SimpleVideoResponse):
    file_url: str

class CreateVideoRequest(BaseModel):
    filename: str
    description: str

class UpdateVideoRequest(BaseModel):
    description: str | None