from fastapi import FastAPI
from datetime import datetime, timedelta
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ResponseModel(BaseModel):
    slack_name: str
    current_day: str
    utc_time: str
    track: str
    github_file_url: str
    github_repo_url: str
    status_code: int
    

@app.get("/my_info/", response_model=ResponseModel)
async def get_info(
    slack_name: str, track: str
):
    
    current_time = datetime.utcnow()

    # Get the current day of the week
    current_day_of_week = current_time.strftime("%A")

    # Format the current time as a string
    current_utc_time = current_time.strftime("%Y-%m-%dT%H:%M:%SZ")

    return ResponseModel(
        slack_name = slack_name, 
        current_day = current_day_of_week, 
        utc_time = current_utc_time,
        track = track,
        github_file_url = "https://github.com/algamawiy/hngx_backend_stage1_task/blob/feature1/main.py",
        github_repo_url = "https://github.com/algamawiy/hngx_backend_stage1_task",
        status_code = 200
        )
