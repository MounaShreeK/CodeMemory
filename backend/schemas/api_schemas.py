from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    repository_id: str = Field(..., min_length=3, max_length=200, examples=["owner/repository"])
    question: str = Field(..., min_length=1, max_length=10000)


class ChatResponse(BaseModel):
    answer: str
    context: list[str] = Field(default_factory=list)
    decision: dict = Field(default_factory=dict)


class RepositoryConnectRequest(BaseModel):
    owner: str = Field(..., min_length=1, max_length=100, pattern=r"^[A-Za-z0-9-]+$")
    repo: str = Field(..., min_length=1, max_length=100, pattern=r"^[A-Za-z0-9_.-]+$")


class MemoryRetainRequest(BaseModel):
    repository_id: str = Field(..., min_length=3, max_length=200)
    content: str = Field(..., min_length=1, max_length=50000)


class MemoryQueryRequest(BaseModel):
    repository_id: str = Field(..., min_length=3, max_length=200)
    query: str = Field(..., min_length=1, max_length=10000)
