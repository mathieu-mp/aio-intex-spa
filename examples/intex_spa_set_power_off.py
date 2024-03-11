"""Usage example: Set spa power off"""
import os
import logging
import asyncio

from aio_intex_spa import IntexSpa

SPA_ADDRESS = os.getenv("SPA_ADDRESS") or "SPA_DEVICE"

logging.basicConfig(level=logging.DEBUG)


async def set_spa_power_off():
    """Set spa power off"""
    spa = IntexSpa(SPA_ADDRESS)

    print(await spa.async_set_power(False))


asyncio.run(set_spa_power_off())
