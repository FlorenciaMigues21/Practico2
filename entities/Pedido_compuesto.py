from peewee import ForeignKeyField
from db import BaseModel
from entities.Pedido import Pedido


class Pedido_compuesto(BaseModel):
    _id_pedido = ForeignKeyField(Pedido, primary_key=True)
    _pedido_asociado = ForeignKeyField(Pedido, default=None)
