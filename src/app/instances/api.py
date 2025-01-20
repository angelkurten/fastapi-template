"""
!! IMPORTANT !!

DO NOT import this module!
"""

from contextlib import asynccontextmanager

from src.app.application import Application  # nopep8

application = Application()


@asynccontextmanager
async def initializer(_):
    application.init()

    yield

    application.shutdown()


api = application.fastapi(lifespan=initializer)
