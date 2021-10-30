import subaTablas
from peewee import *
db = PostgresqlDatabase('practico2BDD', host='localhost',port=5432,user='zlab',password='UMzLab!')
db.connect()

class Cliente:
    _nombre = TextField()
    _direccion = TextField()
    _telefono = TextField()
    _email = CharField(primary_key=True)
    def __init__(self, nombre, direccion, telefono, email):
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._email = email

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if nombre is not None:
            self._nombre = nombre

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, direccion):
        if direccion is not None:
            self._direccion = direccion

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, telefono):
        if telefono is not None:
            self._telefono = telefono

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if email is not None:
            self._email = email

    def crear_cliente(self):
        pass

    def modificar_cliente(self):
        pass

    def eliminar_cliente(self):
        pass