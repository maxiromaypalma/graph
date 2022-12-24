import asyncio
from graph.schema.schema import schema
from graph.schema.state import data

def subscribe_to_field(schema, subscription, field):
    async def main(schema):
        result = await schema.subscribe(subscription)
        async for item in result:
            print(item.data[field])
    return asyncio.run(main(schema))

def subscribe_to_time_of_day(schema):
    subscription = "subscription { timeOfDay }"
    return subscribe_to_field(schema, subscription, 'timeOfDay')

def subscribe_to_state(schema):
    subscription = "subscription { state }"
    return subscribe_to_field(schema, subscription, 'state')

def get_name():
    result = schema.execute('query myQuery { hello }')
    return result.data['hello']

def set_name(name):
    result = schema.execute(
        'mutation myMutation($name: String!) { getName(name: $name) { name } }',
        variables = {"name": str(name)}
    )
    out = result.data.get('getName')
    return out.get('name') if out else None

def get_state():
    return str(data)