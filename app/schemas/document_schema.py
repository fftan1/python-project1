from pydantic import BaseModel


class BaseRequest(BaseModel):
    title: str
    content: str
    category: str
    status: str
    updated_at: str


class BaseResponse(BaseModel):
    title: str
    content: str
    category: str
    status: str
    created_at: str
    updated_at: str
