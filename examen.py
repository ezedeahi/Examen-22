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

nombre = input ("tu nombre es? : ")
dinero = int(input("cuanto dinero tenes? : "))
objetos= ["agua" , "alfajor" , "tostado"]
precios= [700 , 900 , 2200]
print("que queres?: ")
print ("estos son los productos que tenemos: ")
for orden in range(len(objetos)):
    print(f" {orden+1} {objetos[orden]} {precios[orden]}")



