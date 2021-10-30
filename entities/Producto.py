from peewee import TextField, IntegerField


class Producto:
    _nombre_producto = TextField(primary_key=True)
    _precio = IntegerField()
    _stock = IntegerField()

    def __Init__(self,nombre_producto,precio,stock):
        self._nombreProducto = nombre_producto
        self._precio = precio
        self._stock = stock


    @property
    def nombre_producto(self):
        return self._nombreProducto

    @property
    def precio(self):
        return self._precio

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def cambiar_stock(self,nuevo_stock):
        if nuevo_stock is not None:
            self._stock = nuevo_stock

    @precio.setter
    def cambiar_precio(self, precio_nuevo):
        if precio_nuevo is not None:
            self._precio = precio_nuevo

