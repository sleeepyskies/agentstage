from pydantic import BaseModel

class ExampleResponse(BaseModel):
    name: str
    id: int

    class Config:
        from_attributes = True

class CreateExampleRequest(BaseModel):
    name: str

class GetExampleRequest(BaseModel):
    id: int

class UpdateExampleRequest(BaseModel):
    name: str
    id: int

class DeleteExampleRequest(BaseModel):
    id: int


