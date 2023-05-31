from graphene_sqlalchemy import (
    SQLAlchemyObjectType,
)
from graphene import (
    # Int
    String
)
from models.departamento import Departamento as DepartamentoModel
# from models.user import User as UserModel
from models.persona import Persona as PersonaModel

class Persona(SQLAlchemyObjectType):
    class Meta:
        model = PersonaModel
    name = String(description='representa el nombre de la persona')

class Departamento(SQLAlchemyObjectType):
    class Meta:
        model = DepartamentoModel
        # exclude_fields = ('fk_persona')

# class User(SQLAlchemyObjectType):
#     class Meta:
#         model = UserModel