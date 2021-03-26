from graphene import relay, ObjectType
import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Category, Ingredient
from graphene.relay.node import from_global_id


# Without Relay
# class CategoryType(DjangoObjectType):
#     class Meta:
#         model = Category
#         fields = ['id', 'name', 'ingredients']
##       exclude= ('id')
##       fields= '__all__'


# class IngredientType(DjangoObjectType):
#     class Meta:
#         model = Ingredient
#         fields = ['id', 'name', 'notes', 'category']
#
##     extra_field = graphene.String()

# def resolve_extra_field(self, info):
# return "hello!"


# class Query(graphene.ObjectType):
#     all_ingredients = graphene.List(IngredientType)
#     category_by_name = graphene.Field(
#         CategoryType, name=graphene.String(required=True))

#     def resolve_all_ingredients(root, info):
#         return Ingredient.objects.select_related('category').all()

#     def resolve_category_by_name(root, info, name):
#         try:
#             return Category.objects.get(name=name)
#         except Category.DoesNotExist:
#             return None


# With Relay
class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name', 'ingredients']
        interfaces = (relay.Node,)


class IngredientNode(DjangoObjectType):
    class Meta:
        model = Ingredient
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'notes': ['exact', 'icontains'],
            'category': ['exact'],
            'category__name': ['exact'],
        }
        interfaces = (relay.Node,)


class CreateIngredient(graphene.relay.ClientIDMutation):
    ingredient = graphene.Field(IngredientNode)

    class Input:
        name = graphene.String()
        notes = graphene.String()
        category = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        ingredient = Ingredient(
            name=input.get('name'),
            notes=input.get('notes'),
            category=Category.objects.get(name=input.get('category')),
        )
        ingredient.save()
        # Notice we return an instance of this mutation
        return CreateIngredient(ingredient=ingredient)


class Mutation(graphene.ObjectType):
    create_ingredient = CreateIngredient.Field()


class Query(ObjectType):
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    ingredient = relay.Node.Field(IngredientNode)
    all_ingredients = DjangoFilterConnectionField(IngredientNode)
