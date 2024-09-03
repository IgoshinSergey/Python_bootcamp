from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel, HttpUrl
from urllib.parse import urlparse, ParseResult
from typing import List, Optional
from uuid import UUID, uuid4
from asyncio import gather, sleep
from uvicorn import run
from aiohttp import ClientSession, ClientError
from redis import Redis
import logging
import colorlog


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
redis = Redis(host='localhost', port=6379)
counter_key: str = "counter"
logging.basicConfig(
    format="%(levelname)s:     %(message)s",
    level=logging.INFO
)
colorlog.basicConfig(
    format="%(log_color)s%(levelname)s%(reset)s:     %(message)s",
    level=logging.INFO,
    log_colors={
        "INFO": "green"
    }
)


async def requests_status_codes(task: Task, urls: List[Url]) -> None:
    async with ClientSession() as session:
        async_tasks: List = []
        for url in urls:
            async_tasks.append(fetch_status_code(session, url))
        result = await gather(*async_tasks)
        task.result = [i for i in result if i is not None]
        task.status = "ready"


async def fetch_status_code(session: ClientSession, url: Url) -> Result | None:
    str_url: str = str(url.url)
    parsed_url: ParseResult = urlparse(str_url)
    domain: str = parsed_url.netloc
    status_code_cache = redis.hget("status", str_url)
    increment = redis.incr(f"{counter_key}:{domain}")
    if status_code_cache is not None:
        return Result(url=str_url, status_code=int(status_code_cache))
    else:
        try:
            async with session.get(str_url) as response:
                result = Result(url=str_url, status_code=response.status)
                set_url = redis.hset("status", str_url, str(response.status))
                logging.info(f"URL {str_url} and status code {response.status} added to cache")
                return result
        except ClientError:
            return None


async def clear_cache() -> None:
    await sleep(60)
    flush = redis.flushall()
    logging.info(f"The cache has been cleared")


@app.post("/api/v1/tasks/")
async def add_new_tasks(urls: List[Url], background_tasks: BackgroundTasks):
    task: Task = Task(
        id=uuid4(),
        status="running",
        result=[]
    )
    tasks.append(task)
    background_tasks.add_task(requests_status_codes, task, urls)
    background_tasks.add_task(clear_cache)
    return task


@app.get("/api/v1/tasks/{received_task_id}")
async def get_task(received_task_id: UUID) -> Task | None:
    if len(tasks) > 0:
        for task in tasks:
            if task.id == received_task_id:
                return task
    return None


if __name__ == "__main__":
    run(app, host="localhost", port=8888)
