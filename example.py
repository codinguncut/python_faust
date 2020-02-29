"""
- launch with `faust -A example worker -l info`
- send messages to topic using `faust -A example send @greet "Hello Faust"`
"""
import faust

app = faust.App(
    'hello-world',
    broker='kafka://localhost:9092',
    value_serializer='raw',
)

greetings_topic = app.topic('greetings')


@app.agent(greetings_topic)
async def greet(greetings):
    async for greeting in greetings:
        print(greeting)
