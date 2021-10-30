from peewee import TextField, ForeignKeyField

from entities.Cliente import Cliente


class Cuenta:
    _numero_tarjeta = TextField()
    _disponible = TextField()
    _propietario = ForeignKeyField(Cliente)
    def __init__(self,numero_tarjeta,disponible, propietario):
        self._numero_tarjeta = numero_tarjeta
        self._disponible = disponible
        self._propietario = propietario


    @property
    def numero_tarjeta(self):
        return self._numero_tarjeta

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, disponible):
        if disponible is not None:
            self._disponible = disponible
    @property
    def propietario(self):
        return self._propietario

    

