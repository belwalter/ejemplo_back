from graphene import (
    ObjectType,
    # String,
    # relay,
    # # Field,
    List,
    # Int
)

# from .funko import Funko as FunkoModel
# from .objects import (
#     Funko,
#     User,
# )
from .objects import Persona

class Query(ObjectType):
    personas = List(lambda: Persona)
    # funkos = List(lambda: Funko, collection=String(), name=String())
    # users = List(lambda: User)

    # def resolve_funkos(self, info, collection=None, name=None):
    #     query = Funko.get_query(info=info)
    #     if collection:
    #         query = query.filter(FunkoModel.collection == collection)
    #     if name:
    #         query = query.filter(FunkoModel.name == name)
    #     return query.all()

    def resolve_personas(self, info):
        query = Persona.get_query(info=info)
        return query.all()