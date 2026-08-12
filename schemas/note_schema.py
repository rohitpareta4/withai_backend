from pydantic import BaseModel,Field
from typing import Annotated

class CreateNote(BaseModel):
    note: Annotated[
        str,
        Field(..., description="note is required")
    ]