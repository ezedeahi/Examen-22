# Examen práctico - Sistema de pedidos del kiosco
# Nombre y apellido:
# Curso:
#
# IMPORTANTE:
# Resolver el programa siguiendo las etapas indicadas en el README.md.
# Realizar los commits y push cuando se indique.



# =========================
# ETAPA 1 - INICIO
# =========================

# Crear las variables necesarias.
# Crear las listas de productos y precios.
# Pedir los datos del cliente.


# =========================
# ETAPA 2 - COMPRAS
# =========================

# Mostrar el menú y procesar la opción seleccionada.
# Utilizar las listas para obtener producto y precio.


# =========================
# ETAPA 3 - CICLO PRINCIPAL
# =========================

# Modificar el programa para que continúe funcionando
# hasta que el usuario decida finalizar la compra.


# =========================
# ETAPA 4 - PEDIDO Y RESUMEN
# =========================

# Mostrar el estado actual del pedido.
# Recorrer las listas con un for para mostrar productos y precios.
cantidad = 0
productos = []

nombre = input ("tu nombre es? : ")
dinero = int(input("cuanto dinero tenes? : "))
dinero_1 = dinero
print ("hola " , nombre , " tenes " , dinero , " pesos")
objetos= ["agua" , "alfajor" , "tostado" ]
precios= [700 , 900 , 2200 ]

while True:
    print("que queres?: ")
    print ("estos son los productos que tenemos: ")
    for orden in range(len(objetos)):
        print(f" {orden+1} {objetos[orden]} {precios[orden]}" )
    print(" 4 consultar pedido")
    print(" 5 salir")
    pedido = int(input("que numero de producto queres? : "))
    if pedido == 1:
        if dinero < precios[0]:
            print("no te alcanza para comprar agua")
        else:
            print("compraste agua")
            dinero-= precios[0]
            print(f"te quedan {dinero} pesos")
            cantidad += 1
            productos.append ("agua")
    elif pedido == 2:
        if dinero < precios[1]:
            print("no te alcanza para comprar alfajor")
        else:
            print("compraste alfajor")
            dinero-= precios[1]
            print(f"te quedan {dinero} pesos")
            cantidad += 1
            productos.append ("agua")
    elif pedido == 2:
        if dinero < precios[1]:
            print("no te alcanza para comprar alfajor")
        else:
            print("compraste alfajor")
            dinero-= precios[1]
            print(f"te quedan {dinero} pesos")
            cantidad += 1
            productos.append ("alfajor")
    elif pedido == 3:
        if dinero < precios[2]:
            print("no te alcanza para comprar tostado")
        else:
            print("compraste tostado")
            dinero-= precios[2]
            print(f"te quedan {dinero} pesos")
            cantidad += 1
            productos.append ("tostado")
    elif pedido == 4:
        print("\n===== PEDIDO ACTUAL =====")
        print("cliente: ", nombre)
        print(f"compraste {cantidad} productos")
        print(f"gastaste {dinero_1-dinero} pesos")
        print(f"te quedan {dinero} pesos")
        if cantidad == 0:
            print("no compraste nada")
        else:
         print(f"los productos que compraste son ")
         for producto in productos:
            print("-",producto)
    elif pedido == 5:
            print("\n===== PEDIDO FINALIZADO =====")
            print("cliente:", nombre)
            print(f"compraste {cantidad} productos")
            print(f"gastaste {dinero_1 - dinero} pesos")
            print(f"te quedan {dinero} pesos")
            if cantidad == 0:
                print("no compraste nada")
            else:
                print("los productos que compraste son:")
                for producto in productos:
                    print("-", producto)
            break
    else:
            print("opcion invalida")
    if pedido != 4 and pedido != 5:
       print(f"compraste {cantidad} productos")
       print("los productos que compraste son:")
       for producto in productos:
        print("-", producto)


