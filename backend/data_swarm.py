import asyncio
import json
import random
from redis_client import redis_client

async def on_chain_scanner():
    while True:
        # Simulate MindSpider ingestion
        data = {"type": "on_chain", "tx_volume": random.uniform(100, 10000), "gas_price": random.uniform(10, 100)}
        await redis_client.publish("raw_data", json.dumps(data))
        await asyncio.sleep(0.1)

async def liquidity_tracker():
    while True:
        data = {"type": "liquidity", "pool_depth": random.uniform(1000, 100000)}
        await redis_client.publish("raw_data", json.dumps(data))
        await asyncio.sleep(0.2)

async def start_data_swarm():
    await asyncio.gather(
        on_chain_scanner(),
        liquidity_tracker()
    )
