import logging

import json
import faust
from ..common import app
from ..models import result_topic, Result


@app.agent(result_topic, on_leader=True)
async def store_agent(results: faust.Stream[Result]) -> None:
    with open('tweets.jl', 'wt') as fhandle:
        async for res in results:
            logging.warning('got res')
            print(json.dumps(res), file=fhandle)
