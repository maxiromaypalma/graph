from graphene import ObjectType, Mutation, String
from graph.schema.state import data

class GetName(Mutation):
    class Arguments:
        name = String(required=True)

    name = String()

    def mutate(root, _, name):
        if name == str(None):
            del data['name']
        else:
            data['name'] = name
        return GetName(name=name)

class Mutation(ObjectType):

    getName = GetName.Field()