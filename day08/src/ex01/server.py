from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from uuid import UUID, uuid4
from asyncio import gather
import uvicorn
import aiohttp


class Url(BaseModel):
    url: HttpUrl


class Result(BaseModel):
    url: str
    status_code: int


class Task(BaseModel):
    id: UUID
    status: str
    result: Optional[List[Result]] = []


app: FastAPI = FastAPI()
tasks: List[Task] = []


async def requests_status_codes(task: Task, urls: List[Url]) -> None:
    async with aiohttp.ClientSession() as session:
        async_tasks: List = []
        for url in urls:
            async_tasks.append(fetch_status_code(session, url))
        result = await gather(*async_tasks)
        task.result = [i for i in result if i is not None]
        task.status = "ready"


async def fetch_status_code(session: aiohttp.ClientSession, url: Url) -> Result | None:
    str_url = str(url.url)
    try:
        async with session.get(str_url) as response:
            return Result(url=str_url, status_code=response.status)
    except aiohttp.ClientError:
        return None


@app.post("/api/v1/tasks/")
async def add_new_tasks(urls: List[Url], background_tasks: BackgroundTasks):
    task: Task = Task(
        id=uuid4(),
        status="running",
        result=[]
    )
    tasks.append(task)
    background_tasks.add_task(requests_status_codes, task, urls)
    return task


@app.get("/api/v1/tasks/{received_task_id}")
async def get_task(received_task_id: UUID) -> Task | None:
    if len(tasks) > 0:
        for task in tasks:
            if task.id == received_task_id:
                return task
    return None


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8888)
