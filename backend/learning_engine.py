import asyncio
import json
from redis_client import redis_client

async def start_learning_engine():
    pubsub = redis_client.pubsub()
    await pubsub.subscribe("trade_results")
    
    async for message in pubsub.listen():
        if message["type"] == "message":
            result = json.loads(message["data"])
            # Update agent weights based on PnL
            print(f"Learning from result: {result}")
