import os
import logging
import asyncio

from intex_spa.intex_spa import IntexSpa

SPA_ADDRESS = os.getenv("SPA_ADDRESS") or "SPA_DEVICE"

logging.basicConfig(level=logging.DEBUG)


async def example_intex_spa():
    """Example for intex_spa"""
    intex_spa = IntexSpa(SPA_ADDRESS)

    await intex_spa.async_update_status()
    await asyncio.sleep(10)
    await intex_spa.async_update_status()


asyncio.run(example_intex_spa())
