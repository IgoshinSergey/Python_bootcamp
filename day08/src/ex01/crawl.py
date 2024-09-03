from aiohttp import ClientSession
import argparse
import asyncio
from typing import List, Dict


async def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument("urls", type=str, nargs="+")

    return parser.parse_args()


async def main() -> None:
    url: str = "http://localhost:8888/api/v1/tasks/"
    args: argparse.Namespace = await parse_arguments()
    urls: List[Dict[str, str]] = [{"url": url} for url in args.urls]
    async with ClientSession() as session:
        async with session.post(url, json=urls) as response:
            if response.status == 200:
                task = await response.json()
                uuid = task["id"]
            else:
                print("Error: Incorrect URL")
                return
        url_task = f"{url}{uuid}"
        while True:
            async with session.get(url_task) as response:
                task = await response.json()
                if task["status"] == "ready":
                    break
                await asyncio.sleep(0.5)
        for res in task["result"]:
            status_code = res["status_code"]
            url = res["url"]
            print(f"{status_code}\t{url}")


if __name__ == "__main__":
    asyncio.run(main())
