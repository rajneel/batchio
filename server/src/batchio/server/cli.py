import argparse
import logging
import asyncio
import yaml
import shlex
import subprocess

import aiohttp
import aiohttp.server
from .rpc import app as rpc
from . import scheduler


def config_logging(level=logging.DEBUG):
    root = logging.getLogger()
    for handler in root.handlers:
        root.removeHandler(handler)
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=level)


def main():
    config_logging()

    loop = asyncio.get_event_loop()
    loop.set_debug(True)

    scheduler.scheduler.start()

    http_app = rpc.create_app(loop=loop)
    http_coro = loop.create_server(
        http_app.make_handler(debug=True),
        '0.0.0.0', '8080')
    http_server = loop.run_until_complete(http_coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    http_server.close()
    loop.run_until_complete(http_server.wait_closed())
    loop.close()
