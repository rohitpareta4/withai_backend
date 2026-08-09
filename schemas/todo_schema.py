from typing import Annotated
from pydantic import BaseModel,Field

class TodoItems(BaseModel):
    title:Annotated[str,Field(...,max_length=200,description="title of the todo...")]

class getTodoItems(BaseModel):
    title:Annotated[str,Field(...,max_length=200,description="title of the todo...")]

class CompletedUpdateitem(BaseModel):
    completed:Annotated[bool,Field(...,description="completed is req")]    

class titleUpdateitem(BaseModel):
    title:Annotated[str,Field(...,max_length=200,description="title of the todo...")]




    