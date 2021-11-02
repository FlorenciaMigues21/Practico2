from peewee import TextField, IntegerField, DateField, AutoField

from db import BaseModel


class Pedido(BaseModel):

    _estado = TextField()
    _total = IntegerField()
    _fecha_realizacion = DateField()

