from uuid import UUID
from pydantic import BaseModel, Field, field_validator


class NewTaskResponse(BaseModel):
    id: str
    name: str = Field(min_length=3, max_length=25)

    @field_validator('id', mode='before')
    @classmethod
    def serialize_uuid_value(cls, value):
        if isinstance(value, UUID):
            return str(value)
        return value
