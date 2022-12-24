import asyncio
import datetime
from graphene import ObjectType, String
from graph.schema.state import data

async def _subscribe_with_timeout(func, timeout):
    passedTime = datetime.datetime.now()
    while True:
        nowTime = datetime.datetime.now()
        if (nowTime - passedTime).total_seconds() > timeout:
            return
        yield func()
        await asyncio.sleep(1)

class Subscription(ObjectType):
    time_of_day = String()
    state = String()

    async def subscribe_time_of_day(parent, _):
        def func():
            return datetime.datetime.now().isoformat()
        return _subscribe_with_timeout(lambda: func(), 5)

    async def subscribe_state(parent, _):
        def func():
            return str(data)
        return _subscribe_with_timeout(lambda: func(), 5)