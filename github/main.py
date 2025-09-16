from fastapi import FastAPI
from app import run_agent
import asyncio

app = FastAPI()

@app.post("/query/")
async def query_agent(message: str):
    response = await run_agent(message)
    return {"response": response}
