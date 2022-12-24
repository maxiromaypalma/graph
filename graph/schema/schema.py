from graphene import Schema
from .queries.query import Query
from .queries.mutation import Mutation
from .queries.subscription import Subscription

schema = Schema(
    query=Query,
    mutation=Mutation,
    subscription=Subscription
)