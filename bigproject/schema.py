import graphene
from cook_ingredients.schema import Query as cook_query


class Query(cook_query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
