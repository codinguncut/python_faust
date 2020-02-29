import logging  # noqa

import faust
from ..common import app
from ..models import result_topic, Result, content_topic, Content
from ..nlp.entities import init, entities


@app.agent(content_topic,
           sink=[result_topic],
           concurrency=4)
async def nlp_agent(contents: faust.Stream[Content]) -> None:
    nlp = init()
    async for content in contents:
        text = content.text
        ents = entities(nlp, text)
        yield Result(
            text=text,
            entities=list(ents)  # list for msgpack
        )
