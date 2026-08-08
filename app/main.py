from fastapi import FastAPI
from core.database import engine,Base
from models.users import User
from fastapi.middleware.cors import CORSMiddleware
from routers import auth_router,resume_router,interview_router,todo_router

Base.metadata.create_all(bind=engine)

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","https://with-ai-x1.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth_router.router)
app.include_router(resume_router.router)
app.include_router(interview_router.router)
app.include_router(todo_router.router)



@app.post('/')
def hey():
    return {"message":"hii"}