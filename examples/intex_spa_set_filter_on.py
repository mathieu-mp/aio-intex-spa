"""Usage example: Set spa filter on."""

import os
import logging
import asyncio

from aio_intex_spa import IntexSpa

SPA_ADDRESS = os.getenv("SPA_ADDRESS") or "SPA_DEVICE"

logging.basicConfig(level=logging.DEBUG)


async def set_spa_filter_on():
    """Set spa filter on."""
    spa = IntexSpa(SPA_ADDRESS)

    print(await spa.async_set_filter())


asyncio.run(set_spa_filter_on())
