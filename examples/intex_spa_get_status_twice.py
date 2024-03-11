"""Usage example: Get spa status twice"""
import os
import logging
import asyncio

from aio_intex_spa import IntexSpa

SPA_ADDRESS = os.getenv("SPA_ADDRESS") or "SPA_DEVICE"

logging.basicConfig(level=logging.DEBUG)


async def get_spa_status_twice():
    """Get spa status twice"""
    spa = IntexSpa(SPA_ADDRESS)

    print(await spa.async_update_status())
    print(await spa.async_update_status())


asyncio.run(get_spa_status_twice())
