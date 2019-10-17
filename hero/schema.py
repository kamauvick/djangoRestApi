import graphene
from graphene_django import DjangoObjectType

from .models import Hero, City


class CityType(DjangoObjectType):
    class Meta:
        model = City

    


class HeroType(DjangoObjectType):
    city = graphene.List(CityType)

    class Meta:
        model = Hero


class Query(graphene.ObjectType):
    heroes = graphene.List(HeroType)

    def resolve_heroes(self, info, **kwargs):
        return Hero.objects.all()
    
    def resolve_cities(self, info, **kwargs):
        return City.objects.all()


schema = graphene.Schema(query=Query, subscription=Query)
