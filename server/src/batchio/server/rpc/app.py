import aiohttp.web as web
import json
import logging
from .. import scheduler


logger = logging.getLogger(__name__)


async def get_jobs(request):
    jobs = scheduler.scheduler.get_jobs(jobstore=None, pending=None)
    result = []
    for j in jobs:
        job = {
            'job_id': j.id,
            'args': j.args,
            'next_run_time': j.next_run_time.isoformat()
        }
        result.append(job)
    return web.Response(text=json.dumps(result))


async def get_job(request):
    job = scheduler.scheduler.get_job(job_id=request.match_info['job_id'])
    return web.Response(text=json.dumps({
        'job_id': job.id,
        'args': job.args,
        'next_run_time': job.next_run_time.isoformat()
    }))


async def create_job(request):
    data = await request.json()

    scheduler.scheduler.add_job(
        func=scheduler.noop,
        trigger=data['trigger']['type'],
        kwargs={'command': data['command'], 'env': data.get('env_vars', {})},
        id=data['id'],
        **data.get('trigger', {}).get('args', {}))

    return web.Response(text=json.dumps(data))


def create_app(loop=None):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/jobs', get_jobs)
    app.router.add_route('GET', '/jobs/{job_id}', get_job)
    app.router.add_route('POST', '/jobs', create_job)
    return app
