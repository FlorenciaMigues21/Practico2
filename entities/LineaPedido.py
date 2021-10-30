from peewee import IntegerField, ForeignKeyField

from entities.Pedido import Pedido
from entities.Producto import Producto


class LineaPedido:
    _numero = IntegerField()
    _nombre_producto = ForeignKeyField(Producto)
    _pedido_asoaciado = ForeignKeyField(Pedido, primary_key=True)
    def __init__(self, nombre_producto, numero, pedido_asociado):
        self._nombre_producto = nombre_producto
        self._numero = numero
        self._pedido_asoaciado = pedido_asociado

    @property
    def nombre_producto(self):
        return self._nombre_producto

    @property
    def numero(self):
        return self._numero

    @property
    def pedido_asociado(self):
        return self._pedido_asoaciado

    @numero.setter
    def cantidad(self, numero_nuevo):
        if numero_nuevo is not None:
            self._numero = numero_nuevo
