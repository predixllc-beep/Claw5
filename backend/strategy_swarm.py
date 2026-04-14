import asyncio
import json
import random
from redis_client import redis_client

async def scalper_agent(features):
    return {"agent": "scalper", "action": "BUY" if random.random() > 0.5 else "SELL", "confidence": random.random(), "expected_return": random.uniform(0.001, 0.01), "latency_score": random.random()}

async def start_strategy_swarm():
    pubsub = redis_client.pubsub()
    await pubsub.subscribe("features")
    
    async for message in pubsub.listen():
        if message["type"] == "message":
            features = json.loads(message["data"])
            proposal = await scalper_agent(features)
            await redis_client.publish("proposals", json.dumps(proposal))
