from pydantic import BaseModel,Field
from typing import Any,Dict,Annotated

class Createresume(BaseModel):
    title:Annotated[str,Field(...,description="title is required...")]
    template:Annotated[str,Field(...,description="template is req")]
    resume_data:Annotated[Dict[str,Any],Field(...,description="resume data")]

class getresume(BaseModel):
    title:Annotated[str,Field(...,description="title is required...")]
    template:Annotated[str,Field(...,description="template is req")]
    resume_data:Annotated[Dict[str,Any],Field(...,description="resume data")]