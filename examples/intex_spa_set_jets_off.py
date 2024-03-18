"""Usage example: Set spa jets off."""

import os
import logging
import asyncio

from aio_intex_spa import IntexSpa

SPA_ADDRESS = os.getenv("SPA_ADDRESS") or "SPA_DEVICE"

logging.basicConfig(level=logging.DEBUG)


async def set_spa_jets_off():
    """Set spa jets off."""
    spa = IntexSpa(SPA_ADDRESS)

    print(await spa.async_set_jets(False))


asyncio.run(set_spa_jets_off())
