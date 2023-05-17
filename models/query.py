from graphene import (
    ObjectType,
    String,
    Boolean,
    List,
    Int
)

from .persona import Persona as PersonaModel
from .objects import Persona

class Query(ObjectType):
    personas = List(lambda: Persona, last_name=String(), id=Int(), has_email=Boolean(), order_by_name=Boolean())

    def resolve_personas(self, info, id=None, last_name=None, has_email=None, order_by_name=None):
        query = Persona.get_query(info=info)
        if id:
            query = query.filter(PersonaModel.id==id)
        if last_name:
            query = query.filter(PersonaModel.last_name==last_name)
        if has_email is not None:
            if has_email:
                query = query.filter(PersonaModel.email != None)
            else:
                query = query.filter(PersonaModel.email == None)
        if order_by_name:
            query = query.order_by(PersonaModel.name)
        return query.all()