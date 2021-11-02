from peewee import IntegerField, ForeignKeyField

from db import BaseModel
from entities.Pedido import Pedido
from entities.Producto import Producto


class LineaPedido(BaseModel):
    _numero = IntegerField()
    _nombre_producto = ForeignKeyField(Producto)
    _pedido_asoaciado = ForeignKeyField(Pedido, primary_key=True)
