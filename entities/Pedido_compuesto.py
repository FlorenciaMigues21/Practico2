from peewee import ForeignKeyField

from entities.Pedido import Pedido


class Pedido_compuesto:
    _id_pedido = ForeignKeyField(Pedido, primary_key=True)

    def __init__(self,id_pedido):
        self._id_pedido = id_pedido


    @property
    def id_pedido(self):
        return self._id_pedido
