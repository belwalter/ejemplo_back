from graphene import (
    ObjectType,
    Mutation,
#     Int,
    String,
    Field,
)
from api_config import (
    db,
)

from .objects import (
    Persona
)
from .persona import Persona as PersonaModel


class createPersona(Mutation):
    class Arguments:
        name = String(required=True)
        last_name = String(required=True)
        email = String(required=False)
    
    persona = Field(lambda: Persona)

    def mutate(self, info, name, last_name, email=None):
        persona = PersonaModel(name=name, last_name=last_name, email=email)

        db.session.add(persona)
        db.session.commit()

        return createPersona(persona=persona)

# class updateFunko(Mutation):
#     class Arguments:
#         funko_id = Int(required=True)
#         collection = String(required=True)

#     funko = Field(lambda: FunkoObject)

#     def mutate(self, info, collection, funko_id):
#         funko = FunkoModel.query.get(funko_id)
#         if funko:
#             funko.collection = collection
#             db.session.add(funko)
#             db.session.commit()

#         return updateFunko(funko=funko)


# class deleteFunko(Mutation):
#     class Arguments:
#         funko_id = Int(required=True)

#     funko = Field(lambda: FunkoObject)

#     def mutate(self, info, funko_id):
#         funko = FunkoModel.query.get(funko_id)
#         if funko:
#             db.session.delete(funko)
#             db.session.commit()

#         return deleteFunko(funko=funko)

class Mutation(ObjectType):
    create_persona = createPersona.Field()
#     update_funko = updateFunko.Field()
#     delete_funko = deleteFunko.Field()