from peewee import TextField, IntegerField


class Producto:
    _nombre_producto = TextField(primary_key=True)
    _precio = IntegerField()
    _stock = IntegerField()

    def modificar_stock(nombre,stock):
        Producto.update(_nombre_producto= nombre).where(Producto._stock == stock).execute()

