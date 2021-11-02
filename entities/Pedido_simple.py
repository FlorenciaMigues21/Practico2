from peewee import ForeignKeyField

from entities.Pedido import Pedido
from entities.Pedido_compuesto import Pedido_compuesto


class Pedido_simple:
    _id_pedido = ForeignKeyField(Pedido, primary_key=True)
    _asoc_pedido_compuesto = ForeignKeyField(Pedido_compuesto, default=None)
