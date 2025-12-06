from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
from agent import AgentController
from storage import Storage

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

agent = AgentController()
storage = Storage()

class TaskRequest(BaseModel):
    task: str

class TaskResponse(BaseModel):
    task: str
    result: str
    tool_used: str
    steps: List[str]
    timestamp: str
    tool_details: Dict[str, Any]

@app.post("/api/execute", response_model=TaskResponse)
async def execute_task(request: TaskRequest):
    result = agent.execute_task(request.task)
    storage.save_task(result)
    return result

@app.get("/api/history", response_model=List[TaskResponse])
async def get_history():
    return storage.get_all_tasks()

@app.delete("/api/history")
async def clear_history():
    storage.clear_history()
    return {"message": "History cleared"}

@app.get("/")
async def root():
    return {"message": "API is running"}