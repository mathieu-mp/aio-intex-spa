"""Usage example: Get spa info"""
import os
import logging
import asyncio

from aio_intex_spa import IntexSpa

SPA_ADDRESS = os.getenv("SPA_ADDRESS") or "SPA_DEVICE"

logging.basicConfig(level=logging.DEBUG)


async def get_spa_info():
    """Get spa info"""
    spa = IntexSpa(SPA_ADDRESS)

    print(await spa.async_update_info())


asyncio.run(get_spa_info())
