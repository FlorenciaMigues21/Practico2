from peewee import *


def subatablasFunc():

    db = PostgresqlDatabase('practico2BDD', host='localhost', port=5432, user='zlab', password='UMzLab!')

    try:
        db.connect()
    except:
        print("Error al conectarse con la base de datos.")



    class cliente(Model):
        class Meta:
            database = db
            db_table = 'cliente'

    class pedido(Model):
        class Meta:
            database = db
            db_table = 'pedido'

    class producto(Model):
        nombreProducto = TextField(primary_key=True)
        precio = IntegerField()
        stock = IntegerField()

        class Meta:
            database = db
            db_table = 'producto'

    class lineaDePedido(Model):
        numero = IntegerField()
        nombre_producto = ForeignKeyField(producto)
        pedidoAsoaciado = ForeignKeyField(pedido, primary_key=True)

        class Meta:
            database = db
            db_table = 'lineaDePedido'

    class cuenta(Model):
        numero_tarjeta = TextField()
        disponible = TextField()
        propietario = ForeignKeyField(cliente)

        class Meta:
            database = db
            db_table = 'cuenta'
            primary_key = CompositeKey("numero_tarjeta","propietario")

    class pedidoCompuesto(Model):
        idPedido = ForeignKeyField(pedido, primary_key=True)

        class Meta:
            database = db
            db_table = 'pedidoCompuesto'

    class pedidoSimple(Model):
        idPedido = ForeignKeyField(pedido, primary_key=True)
        asocPedidoCompuesto = ForeignKeyField(pedidoCompuesto, default=None)

        class Meta:
            database = db
            db_table = 'pedidoSimple'


    db.create_tables([cliente])
    db.create_tables([pedido])
    db.create_tables([lineaDePedido])
    db.create_tables([producto])
    db.create_tables([cuenta])
    db.create_tables([pedidoCompuesto])
    db.create_tables([pedidoSimple])