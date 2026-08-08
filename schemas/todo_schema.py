from typing import Annotated
from pydantic import BaseModel,Field

class TodoItems(BaseModel):
    title:Annotated[str,Field(...,max_length=200,description="title of the todo...")]