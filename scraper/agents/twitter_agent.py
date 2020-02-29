import logging  # noqa

import faust
from ..common import app
from ..models import twitter_topic, Tweet, content_topic, Content


@app.agent(twitter_topic, sink=[content_topic])
async def email_agent(tweets: faust.Stream[Tweet]) -> None:
    async for inst in tweets:
        tweet = inst.content
        text = (tweet.get('extended_tweet', {}).get('full_text') or  # noqa
                tweet.get('text'))
        # logging.warning('got tweet %r', text)
        if text:
            yield Content(text=text)
