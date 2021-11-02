from sqlite3 import Date

from consultas import Consultas
from entities.Cliente import Cliente
from entities.Cuenta import Cuenta
from entities.Pedido_compuesto import Pedido_compuesto
from entities.Pedido_simple import Pedido_simple
from entities.Producto import Producto
from entities.Pedido import Pedido
from entities.LineaPedido import LineaPedido

from datetime import datetime


def modificar_stock(producto, nuevo_stock):
    Producto.update(_stock=nuevo_stock).where(Producto._nombre_producto == producto)


def crear_pedido_unica_cuenta(productos, cuenta):

    # productos = [['Fernet', 1],
    #              ['Coca', 3],
    #              ['Hielo', 1]]

    # cuenta =

    # Asumo que para cada producto ya hay una cantidad adecuada

    pedido_padre = Pedido_compuesto.create(_estado='pendiente', _total=0, _fecha_realizacion=datetime.datetime.now())
    pedidos_hijos = [Pedido_simple.create(_asoc_pedido_compuesto=pedido_padre.id)]

    cant = 0
    pos = 0

    for i in range(len(productos)):
        if cant <= 20:

            # Entra en el pedido_simple actual
            if productos[i][1] + cant <= 20:
                LineaPedido.create(_numero=productos[i][1],
                                   _nombre_producto=productos[i][0],
                                   _pedido_asociado=pedidos_hijos[pos].id)
                cant += 20

            # Este producto no entra en un solo pedido_simple
            elif productos[i][1] > 20:
                while(productos[i][1] > 20):
                    pedidos_hijos.append(Pedido_simple.create(_asoc_pedido_compuesto=pedido_padre.id))
                    pos+=1
                    LineaPedido.create(_numero=20,
                                       _nombre_producto=productos[i][0],
                                       _pedido_asociado=pedidos_hijos[pos].id)
                    productos[i][1]-=20

                if productos[i][1] > 0:
                    pass



            #LineaPedido.create(_numero=productos[i][1], _nombre_producto=productos[i][0], _pedido_asociado='...')



def crear_pedido_simple(prod, acc): #prod=productos, acc=cuenta

    # Se considera que todos los productos entran en este pedido simple

    # prod = [['Fernet', 1],
    #         ['Coca', 3],
    #         ['Hielo', 1]]

    pedido = Pedido.create(_estado='pendiente',
                           _total=0,
                           _fecha_realizacion=datetime.today().strftime('%Y-%m-%d'))

    print(pedido.id)

    pedido_s = Pedido_simple.create(_id_pedido=pedido.id, _cuenta_asociada=acc)

    for p in prod:
        LineaPedido.create(_numero=p[1], _nombre_producto=p[0], _pedido_asociado=pedido.id)







def crear_producto(nombre, precio, stock):
    # crear_producto("Coca", 70, 100)
    # crear_producto("Fernet", 500, 90)
    # crear_producto("Hielo", 130, 60)
    # crear_producto("Vasos descartables", 40, 20)
    # crear_producto("Papas", 90, 50)
    # crear_producto("Merca", 799, 10)

    Producto.create(_nombre_producto=nombre, _pedidoId=2, _precio=precio, _stock=stock)

def verificar_string(linea):
    if linea is None or linea == "":
        return True
    else:
        return False

def consultas():
    aux = Consultas()
    while True:
        print("Seleccione la opción que desee insertando el número correspondiente\n",
              "1. Listar pedidos en cierto rango de fechas y estado\n",
              "2. Listar productos en stock\n",
              "3. Listar clientes\n",
              "4. Listar pedidos con su cliente asociado\n",
              "5. Listar pedidos de un cliente\n",
              "6. Regresar")
        eleccion = (int(input()))
        if eleccion == 1:
            print("Ingrese el estado:\n",
                  "1. Rechazado",
                  "2. Pendiente",
                  "3. Entregado",
                  "4. Despachado")
            select = (int(input()))
            if verificar_string(select):
                print("Debe ingresar un estado")
            else:
                print("Ingrese fecha inicial en formato dd-mm-YYYY")
                fecha_init = input()
                if fecha_init is not None:
                    fecha_init_ob = datetime.strptime(fecha_init, '%d-%m-%Y').date()
                print("Ingrese fecha final en formato dd-mm-YYYY")
                fecha_final = input()
                if fecha_final is not None:
                    fecha_final_ob = datetime.strptime(fecha_final, '%d-%m-%Y').date()
                if select == 1:
                    if fecha_init is None or fecha_final:
                        aux.listar_pedidos("Rechazado")
                    else:
                        aux.listar_pedidos("Rechazado",fecha_init_ob,fecha_final_ob)
                if select == 2:
                    if fecha_init is None or fecha_final:
                        aux.listar_pedidos("Pendiente")
                    else:
                        aux.listar_pedidos("Pendiente",fecha_init_ob,fecha_final_ob)
                if select == 3:
                    if fecha_init is None or fecha_final:
                        aux.listar_pedidos("Entregado")
                    else:
                        aux.listar_pedidos("Despachado",fecha_init_ob,fecha_final_ob)
        if eleccion == 2:
            aux.listar_productos()
        if eleccion == 3:
            aux.listar_clientes()
        if eleccion == 4:
            pass
        if eleccion == 6:
            return
def menu():
    while True:
        print("Seleccione la opción que desee insertando el número correspondiente\n",
              "1. Ingresar cliente\n",
              "2. Modificar cliente\n",
              "3. Eliminar cliente\n",
              "4. Crear cuenta nueva\n",
              "5. Ingresar pedido\n",
              "6. Ingresar artículos en el stock\n",
              "7. Registrar pago de los pedidos\n",
              "8. Realizar consultas\n",
              "9. Salir")
        aux = input()
        eleccion = (int(aux))
        if eleccion == 1:
            print("Ingrese su nombre:")
            nombre = input()
            print("Ingrese su dirección:")
            direccion = input()
            print("Ingrese su teléfono:")
            telefono = input()
            print("Ingrese su mail:")
            mail = input()
            print("Ingrese su número de tarjeta:")
            nro_tarjeta = input()
            if verificar_string(nombre) or verificar_string(direccion) or verificar_string(
                    telefono) or verificar_string(mail) or verificar_string(nro_tarjeta):
                print("Datos mal ingresados, intentelo de nuevo")
            else:
                try:
                    Cliente.create(_nombre=nombre, _direccion=direccion, _telefono=telefono, _email=mail)
                    Cuenta.create(_numero_tarjeta = nro_tarjeta , _disponible = 0, _propietario = mail)
                    print("El cliente se creo correctamente")
                except:
                    print("Hubo un error, verifique si el cliente no existe ya y si ingresó correctamente los datos")
        if eleccion == 2:
            print("Ingrese email del cliente que desea modificar:")
            email = input()
            cliente = Cliente.select().where(Cliente._email==email).execute()
            if verificar_string(email):
                print("Debe ingresar un mail")
            elif len(cliente) == 0:
                print("No existe el cliente, debe crearlo primero.")
            else:
                print("Ingrese que desea modificar:\n",
                      "1. Nombre\n",
                      "2. Dirección\n",
                      "3. Teléfono\n",
                      "4. Email\n")
                cambio = (int(input()))
                if cambio is None or cambio < 1 or cambio > 4:
                    print("Debe ingresar un valor correcto")
                else:
                    if cambio == 1:
                        print("Ingrese nuevo nombre:\n")
                        nuevo_nombre = input()
                        if verificar_string(nuevo_nombre):
                            print("Debe ingresar un nombre")
                        else:
                            Cliente._modificacion_client(email,nuevo_nombre)
                            print("Se modificó correctamente.")
                    elif cambio == 2:
                        print("Ingrese nueva dirección:\n")
                        nueva_dirección = input()
                        if verificar_string(nueva_dirección):
                            print("Debe ingresar una dirección")
                        else:
                            Cliente._modificacion_client(email,None,nueva_dirección)
                            print("Se modificó correctamente.")
                    elif cambio == 3:
                        print("Ingrese nuevo teléfono:\n")
                        nuevo_telefono = input()
                        if verificar_string(nuevo_telefono):
                            print("Debe ingresar un teléfono")
                        else:
                            Cliente._modificacion_client(email, None, None,nuevo_telefono)
                            print("Se modificó correctamente.")
        if eleccion == 3:
            print("Ingresar email del cliente:")
            email = input()
            if verificar_string(email):
                print("Debe ingresar el email.")
            else:
                Cliente._baja_cliente(email)
                print("Se eliminó correctamente")

        if eleccion == 4:
            print("Ingrese el email del cliente al que quiere asociar la cuenta")
            email = input()
            cliente = Cliente.select().where(Cliente._email == email).execute()
            if len(cliente) == 0:
                print("El cliente no existe.")
            else:
                print("Ingrese número de tarjeta:")
                nro = input()
                if verificar_string(nro):
                    print("Debe ingresar un número")
                else:
                    Cuenta.create(_propietario = email,_numero_tarjeta = nro, _disponible = 0)
        if eleccion == 6:
            print("Ingrese el nombre del producto nuevo:")
            nuevo = input()
            print("Ingrese el precio:")
            precio = (int(input()))
            print("Ingrese el stock disponible:")
            stock = (int(input()))
            if verificar_string(nuevo) or verificar_string(precio) or verificar_string(stock):
                print("Debe ingresar todos los datos")
            else:
                Producto.create(_precio = precio, _nombre_producto = nuevo, _stock = stock)
        if eleccion == 8:
            consultas()
        if eleccion == 9:
            break

if __name__ == '__main__':
    #date_str = '09-19-2018'

    prods = [['Fernet', 1], ['Coca', 3], ['Hielo', 1]]
    acc = 1
    crear_pedido_simple(prods, acc)
