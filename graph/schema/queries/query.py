from graphene import ObjectType, String
from graph.schema.state import data

class Query(ObjectType):
    hello = String()

    def resolve_hello(root, _):
        name = data.get('name')
        if name:
            return f'Hello {name}'
        else:
            return 'What is your name?'