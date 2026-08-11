# Nombre y Apellido: Cristian Manjarrés 
      
# TP integrador – Repetitivas- Condicionales y Secuenciales. 
# Institución: UTN
# Carrera: Tecnicatura Universitaria en Programación
# Materia: Programación I

# Ejercicio 1— “Caja del Kiosco” 
# Objetivo: Simular una compra con validaciones y cálculo de total. 

# Validación del nombre del cliente
nombre_cliente = input("Por favor, ingrese su nombre: ")

while not nombre_cliente.isalpha():
    print("Error: el nombre debe contener solo letras.")
    nombre_cliente = input("Por favor, ingrese su nombre: ")

# Validación de la cantidad de productos
cantidad_productos = input("Por favor, ingrese la cantidad de productos: ")

while not cantidad_productos.isdigit() or cantidad_productos == "0":
    print("Error: ingrese un número entero positivo.")
    cantidad_productos = input("Por favor, ingrese la cantidad de productos: ")
cantidad_productos = int(cantidad_productos)

# Acumuladores para los totales de compra
total_sin_descuentos = 0
total_con_descuentos = 0

# Carga de productos
for i in range(cantidad_productos):
    precio = input(f"Producto {i + 1} - Por favor ingrese el precio del producto: ")
    
    while not precio.isdigit():
        print("Error: ingrese un número entero válido.")
        precio = input("Por favor, ingrese el precio del producto: ")

    precio_original = int(precio)

    descuento = input("Seleccione si su producto tiene descuento, S para si, N para no: ").lower()

    while descuento != "s" and descuento != "n":
        print("Error: ingrese solamente S o N.")
        descuento = input("Seleccione si su producto tiene descuento, S para si, N para no: ").lower()

    precio_final = precio_original


    # Aplicar 10% de descuento si es que corresponde
    if descuento == "s":
        precio_final = precio_original * 0.90


    total_sin_descuentos += precio_original
    total_con_descuentos += precio_final

    print(f"El precio final del producto es: ${precio_final:.2f}.")

# Cálculos finales
ahorro_total = total_sin_descuentos - total_con_descuentos
promedio_por_producto = total_con_descuentos / cantidad_productos

# Resumen de la compra
print(f"Total sin descuentos: ${total_sin_descuentos:.2f}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro: ${ahorro_total:.2f}")
print(f"Promedio por producto: ${promedio_por_producto:.2f}")
