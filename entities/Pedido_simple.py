from peewee import ForeignKeyField

from entities.Pedido import Pedido
from entities.Pedido_compuesto import Pedido_compuesto


class Pedido_simple:
    _id_pedido = ForeignKeyField(Pedido, primary_key=True)
    _asoc_pedido_compuesto = ForeignKeyField(Pedido_compuesto, default=None)

    def __init__(self, id_pedido, asoc__pedido_compuesto):
        self._id_pedido = id_pedido
        self._asoc_pedido_compuesto = asoc__pedido_compuesto

    @property
    def id_pedido(self):
        return self._id_pedido

    @property
    def asco_pedido_compuesto(self):
        return self._asoc_pedido_compuesto