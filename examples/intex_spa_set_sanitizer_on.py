"""Usage example: Set spa sanitizer on."""

import os
import logging
import asyncio

from aio_intex_spa import IntexSpa

SPA_ADDRESS = os.getenv("SPA_ADDRESS") or "SPA_DEVICE"

logging.basicConfig(level=logging.DEBUG)


async def set_spa_sanitizer_on():
    """Set spa sanitizer on."""
    spa = IntexSpa(SPA_ADDRESS)

    print(await spa.async_set_sanitizer())


asyncio.run(set_spa_sanitizer_on())
