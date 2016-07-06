import shlex
import logging
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.executors.asyncio import AsyncIOExecutor
from batchio.server.executor import SubprocessExecutor


scheduler = AsyncIOScheduler(executors={'default': SubprocessExecutor()})


def noop(*args, **kwargs):
    pass


async def create_subprocess_callback(future):
    process = future.get_result()
    print('Created PID: ', process.pid)
    await process.wait()
    print('Process PID ', process.pid, 'completed with ', process.returncode)


def create_subprocess(cmd, **kwargs):
    loop = asyncio.get_event_loop()
    logging.debug("Got command: {}".format(shlex.split(cmd)))
    task = loop.create_task(
        asyncio.create_subprocess_exec(shlex.split(cmd), **kwargs))
    task.add_done_callback(create_subprocess_callback)
