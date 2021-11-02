from peewee import *

from db import BaseModel

database = PostgresqlDatabase('practico2', host='localhost', port=5432, user='zlab', password='UMzLab!')
database.connect()


class Cliente(BaseModel):
    _nombre = TextField()
    _direccion = TextField()
    _telefono = TextField()
    _email = CharField(primary_key=True)

    def _modificacion_client(mail, nombre = None, direccion = None, telefono = None):
        if nombre is not None:
            Cliente.update(_nombre=nombre).where(Cliente._email == mail).execute()
        if direccion is not None:
            Cliente.update(_direccion=direccion).where(Cliente._email == mail).execute()
        if telefono is not None:
            Cliente.update(_telefono = telefono).where(Cliente._email == mail).execute()

    def _baja_cliente(mail):
        Cliente.delete().where(Cliente._email == mail).execute()







