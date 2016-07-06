import json
import asyncio
import aiohttp.web as web


async def get_jobs(request):
    return web.Response(body=json.dumps({'foo': 'bar'}))
