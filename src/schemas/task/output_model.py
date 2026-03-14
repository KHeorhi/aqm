from pydantic import BaseModel, Field


class NewTaskResponse(BaseModel):
    task_name: str = Field(min_length=3, max_length=25)
    task_id: str
