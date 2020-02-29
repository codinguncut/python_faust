import logging

import faust
from ..common import app
from ..models import result_topic, Result


@app.agent(result_topic, on_leader=True)
async def store_agent(results: faust.Stream[Result]) -> None:
    with open('tweets.jl', 'wb') as fhandle:
        async for res in results:
            fhandle.write(res.dumps() + b'\n')
