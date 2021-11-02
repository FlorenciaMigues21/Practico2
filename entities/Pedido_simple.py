from peewee import ForeignKeyField
from db import BaseModel
from entities.Pedido import Pedido
from entities.Pedido_compuesto import Pedido_compuesto
from entities.Cuenta import Cuenta


class Pedido_simple(BaseModel):

    _id_pedido = ForeignKeyField(Pedido, primary_key=True)
    _asoc_pedido_compuesto = ForeignKeyField(Pedido_compuesto, default=None, null=True)
    _cuenta_asociada = ForeignKeyField(Cuenta)

