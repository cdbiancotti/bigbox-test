import graphene
from cook_ingredients.schema import Query as cook_query, Mutation as cook_mutation


class Query(cook_query, graphene.ObjectType):
    pass


class Mutation(cook_mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
