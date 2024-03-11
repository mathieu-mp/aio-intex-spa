"""Usage example: Set spa power on"""
import os
import logging
import asyncio

from aio_intex_spa import IntexSpa

SPA_ADDRESS = os.getenv("SPA_ADDRESS") or "SPA_DEVICE"

logging.basicConfig(level=logging.DEBUG)


async def set_spa_power_on():
    """Set spa power on"""
    spa = IntexSpa(SPA_ADDRESS)

    print(await spa.async_set_power())


asyncio.run(set_spa_power_on())
