import asyncio
import json
from redis_client import redis_client

async def start_feature_layer():
    pubsub = redis_client.pubsub()
    await pubsub.subscribe("raw_data")
    
    async for message in pubsub.listen():
        if message["type"] == "message":
            raw = json.loads(message["data"])
            # Normalize and create feature vector
            feature_vector = {"vector": [raw.get("tx_volume", 0) / 10000, raw.get("pool_depth", 0) / 100000]}
            await redis_client.publish("features", json.dumps(feature_vector))
