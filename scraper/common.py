import faust

import scraper.faust_msgpack  # noqa

app = faust.App(
    'scraper',
    datadir='data/scraper',
    topic_partitions=4,
    autodiscover=True,
    origin='scraper',
    key_serializer='msgpack',
    value_serializer='msgpack'
)
