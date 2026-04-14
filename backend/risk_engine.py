import asyncio
import json
from redis_client import redis_client

async def start_risk_engine():
    pubsub = redis_client.pubsub()
    await pubsub.subscribe("consensus_decisions")
    
    async for message in pubsub.listen():
        if message["type"] == "message":
            decision = json.loads(message["data"])
            # Apply risk rules
            if decision.get("confidence", 0) > 0.8:
                decision["approved"] = True
                await redis_client.publish("execution_queue", json.dumps(decision))
