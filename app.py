from fastapi import FastAPI
import asyncio
from pipeline import main
import os
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# API endpoint to trigger async task
@app.get("/run-task/")
async def run_task(player: str):
    """
    Run an async task that waits for the specified seconds.
    """
    result = await main(player,openai_api_key)
    return {"message": "Task completed", "result": str(result)}
