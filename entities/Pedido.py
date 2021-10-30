

class Pedido:

    _estado = TextField()
    _total = IntegerField()
    _pedidoId = IntegerField(primary_key=True)

    def __init__(self, estado, total):
        self._estado = estado
        self._total = total
        self._productos = []

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        if estado is not None:
            self._estado = estado

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total):
        if total is not None:
            self._total = total

