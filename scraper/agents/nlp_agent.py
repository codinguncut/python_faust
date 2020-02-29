import logging

import faust
from ..common import app
from ..models import result_topic, Result, content_topic, Content
from ..lang_processing.entities import init, entities


@app.agent(content_topic,
           sink=[result_topic],
           concurrency=2)
async def nlp_agent(contents: faust.Stream[Content]) -> None:
    logging.warning('before nlp init')
    nlp = init()
    logging.warning('after nlp init')
    async for content in contents:
        logging.warning('got nlp')
        text = content.text
        ents = entities(nlp, text)
        yield Result(
            text=text,
            entities=list(ents)  # list for msgpack
        )
