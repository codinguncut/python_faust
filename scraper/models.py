import faust
from .common import app


class Tweet(faust.Record):
    content: dict


class Content(faust.Record):
    text: str


class Result(faust.Record):
    text: str
    entities: str
    # sentiment: float
    # language: str


twitter_topic = app.topic(
    'twitter',
    value_type=Tweet,
    partitions=4
)

content_topic = app.topic(
    'content',
    value_type=Content,
    partitions=4
)

result_topic = app.topic(
    'result',
    value_type=Result,
    partitions=4
)
