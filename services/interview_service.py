from schemas.interview_schema import Interview_create,git_create
from sqlalchemy.orm import Session
from models.users import User
from models.interview import Interview
from fastapi import HTTPException
from services.gemini_service import generate_questions
import httpx
from urllib.parse import urlparse
from core.config import settings


def interviewcreate_service(body:Interview_create,user:User,db:Session):
    questions = generate_questions(body)
    interview=Interview(
        user_id=user.id,
        role=body.role,
        experience=body.experience,
        difficulty=body.difficulty,
        interviewType=body.interviewType,
        questionCount=body.questionCount,
        questions=questions
    )

    db.add(interview)
    db.commit()
    db.refresh(interview)

    return {
    "message": "Interview created successfully",
    "interviewId": interview.id
    }

def getdetails_service(interview_id:int,user:User,db:Session):

     interview = (
        db.query(Interview)
        .filter(
            Interview.id == interview_id,
            Interview.user_id == user.id
        )
        .first()
    )

    
     if not interview:
        raise HTTPException(status_code=400,detail="user is not found")


     return interview;

def git_service(body: git_create, user: User, db: Session):

    github_url = str(body.github_url).strip()

    parsed_url = urlparse(github_url)

    if parsed_url.netloc not in ["github.com", "www.github.com"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid GitHub URL"
        )

    username = parsed_url.path.strip("/").split("/")[0]

    if not username:
        raise HTTPException(
            status_code=400,
            detail="GitHub username not found"
        )

    github_api_url = f"https://api.github.com/users/{username}"

    repos_api_url = f"https://api.github.com/users/{username}/repos"

    headers = {
        "Authorization": f"Bearer {settings.GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
    }

    with httpx.Client() as client:

        response = client.get(
            github_api_url,
            headers=headers
        )

        repos_response = client.get(
        repos_api_url,
        headers=headers
    )

    if response.status_code == 404:
        raise HTTPException(
            status_code=404,
            detail="GitHub user not found"
        )

    if response.status_code != 200:
        raise HTTPException(
            status_code=500,
            detail="Failed to fetch GitHub data"
        )

    github_data = response.json()
    repos_data = repos_response.json()

    repositories = []

    for repo in repos_data:

     repositories.append({
        "name": repo["name"],
        "description": repo["description"],
        "language": repo["language"],
        "topics": repo["topics"],
        "stars": repo["stargazers_count"],
        "forks": repo["forks_count"],
        "url": repo["html_url"],
    })

    print("github_data", github_data)

    return {
        "username": github_data["login"],
        "name": github_data["name"],
        "avatar_url": github_data["avatar_url"],
        "bio": github_data["bio"],
        "public_repos": github_data["public_repos"],
        "followers": github_data["followers"],
        "following": github_data["following"],
        "location": github_data["location"],
        "company": github_data["company"],
        "profile_url": github_data["html_url"],
        "repositories": repositories,
    }