import asyncio
from datetime import datetime, timedelta
from apscheduler.executors.base import BaseExecutor
from apscheduler.events import (
    JobExecutionEvent, EVENT_JOB_MISSED, EVENT_JOB_ERROR, EVENT_JOB_EXECUTED)
import logging
from pytz import utc
import shlex


logger = logging.getLogger(__name__)


class SubprocessExecutor(BaseExecutor):
    def __init__(self, loop=None):
        super(SubprocessExecutor, self).__init__()
        if not loop:
            loop = asyncio.get_event_loop()
        self._loop = loop

    def start(self, scheduler, alias):
        super(SubprocessExecutor, self).start(scheduler, alias)

    async def _execute_command(self, job, run_time):
        command = shlex.split(job.kwargs['command'])

        logger.info('Running job "%s" (scheduled at %s)', job, run_time)

        process = await asyncio.create_subprocess_exec(
            *command, loop=self._loop)
        logger.debug('PID: %s', process.pid)
        await process.wait()
        logger.debug('Process returned: %s', process.returncode)

        event_code = (EVENT_JOB_EXECUTED if not process.returncode
                      else EVENT_JOB_ERROR)
        event = JobExecutionEvent(event_code, job.id, job._jobstore_alias,
                                  run_time, retval=process.returncode)
        self._run_job_success(job.id, [event])


    @staticmethod
    def _is_missed_job(job, run_time):
        if job.misfire_grace_time is None:
            return False
        difference = datetime.now(utc) - run_time
        grace_time = timedelta(seconds=job.misfire_grace_time)
        return difference > grace_time

    def _do_submit_job(self, job, run_times):
        events = []
        for run_time in run_times:
            if SubprocessExecutor._is_missed_job(job, run_time):
                events.append(JobExecutionEvent(
                    EVENT_JOB_MISSED, job.id, job._jobstore_alias, run_time))
                continue

            self._loop.create_task(self._execute_command(job, run_time))
