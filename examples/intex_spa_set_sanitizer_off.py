"""Usage example: Set spa sanitizer off"""
import os
import logging
import asyncio

from aio_intex_spa import IntexSpa

SPA_ADDRESS = os.getenv("SPA_ADDRESS") or "SPA_DEVICE"

logging.basicConfig(level=logging.DEBUG)


async def set_spa_sanitizer_off():
    """Set spa sanitizer off"""
    spa = IntexSpa(SPA_ADDRESS)

    print(await spa.async_set_sanitizer(False))


asyncio.run(set_spa_sanitizer_off())
