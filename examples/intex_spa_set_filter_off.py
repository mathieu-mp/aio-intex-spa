"""Usage example: Set spa filter off"""
import os
import logging
import asyncio

from aio_intex_spa import IntexSpa

SPA_ADDRESS = os.getenv("SPA_ADDRESS") or "SPA_DEVICE"

logging.basicConfig(level=logging.DEBUG)


async def set_spa_filter_off():
    """Set spa filter off"""
    spa = IntexSpa(SPA_ADDRESS)

    print(await spa.async_set_filter(False))


asyncio.run(set_spa_filter_off())
