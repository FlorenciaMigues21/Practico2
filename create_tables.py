from entities.Cliente import Cliente
from entities.Pedido import Pedido
from entities.Producto import Producto
from entities.Pedido_compuesto import Pedido_compuesto
from entities.Pedido_simple import Pedido_simple
from entities.LineaPedido import LineaPedido
from entities.Cuenta import Cuenta


from peewee import *

db = PostgresqlDatabase('database2', host='localhost', port=5432, user='zlab', password='UMzLab!')
db.connect()


def create_tables():
    with db:
        db.create_tables([Pedido_simple])


if __name__ == '__main__':

    create_tables()
