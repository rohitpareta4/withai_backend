from pydantic import BaseModel,Field,HttpUrl
from typing import Annotated,Dict,List

class Interview_create(BaseModel):
    role:Annotated[str,Field(...,max_length=50,description="select role")]
    experience:Annotated[str,Field(...,description="Add Experience")]
    difficulty:Annotated[str,Field(...,description="Interview difficulty")]
    interviewType: Annotated[str,Field(..., description="Technical | HR | Mixed")]
    skills: Annotated[
        List[str],
        Field(..., description="Required skills")
    ]
    questionCount: Annotated[
        int,
        Field(..., gt=0)
    ]


class git_create(BaseModel):
    github_url:Annotated[HttpUrl,Field(...,description="url is req...")]