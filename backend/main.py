import asyncio
from fastapi import FastAPI
import uvicorn
from redis_client import redis_client
from data_swarm import start_data_swarm
from feature_layer import start_feature_layer
from strategy_swarm import start_strategy_swarm
from risk_engine import start_risk_engine
from execution_engine import start_execution_engine
from learning_engine import start_learning_engine

app = FastAPI(title="NEXUS CLAW V3")

@app.on_event("startup")
async def startup_event():
    # Start all agents as background tasks
    asyncio.create_task(start_data_swarm())
    asyncio.create_task(start_feature_layer())
    asyncio.create_task(start_strategy_swarm())
    asyncio.create_task(start_risk_engine())
    asyncio.create_task(start_execution_engine())
    asyncio.create_task(start_learning_engine())

@app.get("/")
async def root():
    return {"status": "online", "system": "NEXUS CLAW V3"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
