import asyncio
from fastapi import FastAPI
import uvicorn

app = FastAPI(title="NEXUS CLAW V3")

@app.get("/")
async def root():
    return {"status": "online", "system": "NEXUS CLAW V3"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
