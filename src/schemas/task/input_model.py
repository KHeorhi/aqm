from pydantic import BaseModel, Field


class NewTaskParamsRequest(BaseModel):
    task_name: str = Field(min_length=3, max_length=25)
