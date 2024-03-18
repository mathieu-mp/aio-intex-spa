"""Usage example: Set spa bubbles off."""

import os
import logging
import asyncio

from aio_intex_spa import IntexSpa

SPA_ADDRESS = os.getenv("SPA_ADDRESS") or "SPA_DEVICE"

logging.basicConfig(level=logging.DEBUG)


async def set_spa_bubbles_off():
    """Set spa bubbles off."""
    spa = IntexSpa(SPA_ADDRESS)

    print(await spa.async_set_bubbles(False))


asyncio.run(set_spa_bubbles_off())
