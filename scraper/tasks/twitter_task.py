import logging

from ..common import app
from ..models import Tweet, twitter_topic
from ..ingestion.twitter import get_tweets


@app.task(on_leader=True)
async def twitter_task() -> None:
    for tweet in get_tweets():
        await twitter_topic.send(
            key=None,
            value=Tweet(content=tweet)
        )
