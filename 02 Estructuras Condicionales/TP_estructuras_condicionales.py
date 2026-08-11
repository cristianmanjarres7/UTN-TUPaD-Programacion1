# TECNICATURA UNIVERSITARIA					Nombre: Cristian Manjarrés
# EN PROGRAMACIÓN						    
# A DISTANCIA
# Preuniversitario

#                       Trabajo práctico - Estructuras condicionales

# Actividades

# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.


edad = int(input("Por favor, ingrese su edad: "))

if edad > 18:
    print("Es mayor de edad")
else:
    pass


# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.


nota_usuario = int(input("Por favor, ingrese su nota: "))

if nota_usuario >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.


numero = int(input("Por favor, ingrese un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# • Niño/a: menor de 12 años.
# • Adolescente: mayor o igual que 12 años y menor que 18 años.
# • Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# • Adulto/a: mayor o igual que 30 años.

edad = int(input("Por favor, ingrese su edad: "))

if edad < 12:
    print("Es un niño/a")
elif edad < 18:
    print("Es un adolescente")
elif edad < 30:
    print("Es un adulto/a joven")
else: 
    print("Es un adulto/a")


# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".
# Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos
# que tiene un iterable tal como una lista o un string.

contraseña = input("Por favor, ingrese su contraseña: ")
longitud = len(contraseña)

if longitud >= 8 and longitud <= 14:
    print("Ha ingresado una contraseña correcta.") 
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# 6) Escribir un programa que solicite al usuario el consumo mensual de energía eléctrica en
# kilovatios (kWh) e indique la categoría del consumo según el siguiente criterio:
# • Menor que 150 kWh: “Consumo bajo”.
# • Entre 150 y 300 kWh (inclusive): “Consumo medio”.
# • Mayor que 300 kWh: “Consumo alto”.
# Además, si el consumo supera los 500 kWh, mostrar un mensaje adicional que diga:
# “Considere medidas de ahorro energético”.
# El programa debe imprimir por pantalla la categoría correspondiente.

consumo_energia = int(input("Por favor, ingrese su consumo mensual de energía eléctrica: "))

if consumo_energia < 150:
    print("Consumo bajo")
elif consumo_energia <= 300:
    print("Consumo medio")
else:
    print("Consumo alto")
    if consumo_energia > 500:
        print("Considere medidas de ahorro energético")


# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

frase_palabra = input("Por favor, ingrese una frase o palabra: ")

ultima_letra = frase_palabra[-1]

if ultima_letra in "aeiouAEIOU":
    print(f"{frase_palabra}!")
else:
    print(frase_palabra)


# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo con la opción seleccionada por
# el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Por favor, ingrese su nombre: ")

opcion_elegida = int(input("Por favor, elija la opción que desee: \n"
"1. Si quiere su nombre en mayúsculas. \n"
"2. Si quiere su nombre en minúsculas. \n"
"3. Si quiere su nombre con la primera letra mayúscula. \n"
"Opción: "
""))

if opcion_elegida == 1:
    print(nombre.upper())
elif opcion_elegida == 2:
    print(nombre.lower())    
elif opcion_elegida == 3:
    print(nombre.title()) 
else:
    print("Por favor, elija una opcion válida")


# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# • Menor que 3: "Muy leve" (imperceptible).
# • Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# • Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# • Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# • Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# • Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).


magnitud_terremoto = float(input("Por favor, ingrese la magnitud del terremoto: "))

if magnitud_terremoto < 3:
    print("Muy leve")
elif magnitud_terremoto < 4:
    print("Leve")
elif magnitud_terremoto < 5: 
    print("Moderado")
elif magnitud_terremoto < 6:
    print("Fuerte")
elif magnitud_terremoto < 7:
    print("Muy Fuerte")
else:
    print("Extremo")


# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año :

# Periodo del año/ Estación en el hemisferio norte / Estación en el hemisferio sur
# desde el 21 de diciembre hasta el 20 de marzo / invierno / verano
# desde el 21 de marzo hasta el 20 de junio / primavera / otoño
# desde el 21 de junio hasta el 20 de septiembre / verano / invierno
# desde el 21 de septiembre hasta el 20 de diciembre / otoño / primavera

# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("Por favor, seleccione el hemisferio en el cual se encuentra: \n"
                   "Las opciones son: 'N' para el hemisferio Norte y 'S' para el hemisferio Sur: ").upper()

mes = int(input("Por favor, ingrese el mes del año actual: "))

dia = int(input("Por favor, ingrese que día es: "))

if hemisferio == "S":
    if mes == 1 or mes == 2:
        print("Verano")
    elif mes == 12 and dia >= 21:
        print("Verano") 
    elif mes == 3 and dia <= 20:
        print("Verano")
    elif mes == 4 or mes == 5:
        print("Otoño")
    elif mes == 3 and dia >= 21:
        print("Otoño")
    elif mes == 6 and dia <= 20:
        print("Otoño")
    elif mes == 7 or mes == 8:
        print("Invierno")
    elif mes == 6 and dia >= 21:
        print("Invierno") 
    elif mes == 9 and dia <= 20:
        print("Invierno")
    elif mes == 10 or mes == 11:
        print("Primavera")
    elif mes == 9 and dia >= 21:
        print("Primavera")
    elif mes == 12 and dia <= 20:
        print("Primavera")

elif hemisferio == "N":
    if mes == 1 or mes == 2:
        print("Invierno")
    elif mes == 12 and dia >= 21:
        print("Invierno") 
    elif mes == 3 and dia <= 20:
        print("Invierno")
    elif mes == 4 or mes == 5:
        print("Primavera")
    elif mes == 3 and dia >= 21:
        print("Primavera")
    elif mes == 6 and dia <= 20:
        print("Primavera")
    elif mes == 7 or mes == 8:
        print("Verano")
    elif mes == 6 and dia >= 21:
        print("Verano") 
    elif mes == 9 and dia <= 20:
        print("Verano")
    elif mes == 10 or mes == 11:
        print("Otoño")
    elif mes == 9 and dia >= 21:
        print("Otoño")
    elif mes == 12 and dia <= 20:
        print("Otoño")
    



