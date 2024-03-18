"""Usage example: Get spa status with delay."""

import os
import logging
import asyncio

from aio_intex_spa import IntexSpa

SPA_ADDRESS = os.getenv("SPA_ADDRESS") or "SPA_DEVICE"

logging.basicConfig(level=logging.DEBUG)


async def get_spa_status_with_delay():
    """Get spa status with delay."""
    spa = IntexSpa(SPA_ADDRESS)

    print(await spa.async_update_status())
    await asyncio.sleep(10)
    print(await spa.async_update_status())


asyncio.run(get_spa_status_with_delay())
