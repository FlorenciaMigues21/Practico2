from peewee import TextField, ForeignKeyField, AutoField, IntegerField

from db import BaseModel
from entities.Cliente import Cliente


class Cuenta(BaseModel):
    _numero_tarjeta = TextField()
    _disponible = IntegerField()
    _propietario = ForeignKeyField(Cliente)

    def eliminar_cuenta(mail):
        Cuenta.delete().where(Cuenta._propietario == mail).execute()

    def aumentar_disponible(mail, aumento):
        #idaaa = Cuenta.get(Cuenta._propietario==mail).id
        #print(idaaa)
        #print(Cuenta.select(Cuenta.id).where(Cuenta._propietario==mail))

        temp = Cuenta.select().where(Cuenta._propietario == mail)

        for i in temp:
            print(i.id)

    

