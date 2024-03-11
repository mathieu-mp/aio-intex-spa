"""Usage example: Set spa preset temp to 34°C"""
import os
import logging
import asyncio

from aio_intex_spa import IntexSpa

SPA_ADDRESS = os.getenv("SPA_ADDRESS") or "SPA_DEVICE"

logging.basicConfig(level=logging.DEBUG)


async def set_spa_preset_temp_34():
    """Set spa preset temp to 34°C"""
    spa = IntexSpa(SPA_ADDRESS)

    print(await spa.async_set_preset_temp(34))


asyncio.run(set_spa_preset_temp_34())
