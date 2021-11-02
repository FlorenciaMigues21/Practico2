from entities.Cliente import Cliente
from entities.Cuenta import Cuenta
from entities.Pedido import Pedido
from entities.Pedido_simple import Pedido_simple
from entities.Producto import Producto


class Consultas():
    def listar_productos(self):
        for productos in Producto.select():
            print('Nombre: {} - Stock disponible: {}'.format(productos._nombre_producto, productos._stock))

    def listar_clientes(self):
        for cliente in Cliente.select():
            print('Nombre:{}, Direccción:{}, Teléfono:{}, Email:{}'.format(cliente._nombre, cliente._direccion,
                                                                           cliente._telefono, cliente._email))

    def listar_pedido_cliente(self,mail,estado):
        for pedido in Pedido.select():
            print('Pedido: {}'.format())


    def listar_pedidos(self, estado, fecha_inicial = None, fecha_final = None):
        if fecha_inicial is None or fecha_final is None:
            for pedido in Pedido.select().where(Pedido._estado == estado):
                print('Pedido: {}'.format(pedido._id))
        else:
            for pedido in Pedido.select().where(
                    Pedido._estado == estado and fecha_final >= Pedido._fecha_realizacion >= fecha_inicial):
                print('Pedido: {}'.format(pedido._id))

    def listar_pedidos_clientes(self,fecha_inicial, fecha_final):
        for pedido in Pedido.select().where(
                fecha_final >= Pedido._fecha_realizacion >= fecha_inicial):
            print('Pedido: {}'.format())

    def listar_pedidos_cliente_esp(self,mail):
        id_cuentas = Cuenta.select().where(_propietario = mail)
        for cuentas in id_cuentas:
            idC = cuentas.get(id)
            pedidos = Pedido_simple.select().where(Pedido_simple._cuenta_asociada == idC)
