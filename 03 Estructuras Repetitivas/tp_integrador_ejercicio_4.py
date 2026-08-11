# Nombre y Apellido: Cristian Manjarrés 
     
# TP Integrador – Repetitivas- Condicionales y Secuenciales. 
# Institución: UTN
# Carrera: Tecnicatura Universitaria en Programación
# Materia: Programación I

# Ejercicio 4 — “Escape Room: La Bóveda”
# Objetivo: Abrir las tres cerraduras, administrando energía, tiempo y alarma.


# Variables iniciales del juego
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0

# Validación del nombre del agente
nombre_agente = input("Por favor, ingrese el nombre del agente: ")

while not nombre_agente.isalpha():
    print("Error: debe contener sólo letras.")
    nombre_agente = input("Por favor, ingrese el nombre del agente: ")


# Ciclo principal del juego
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    # Bloqueo de la bóveda si se cumplen condiciones
    if alarma and tiempo <= 3:
        break

    print(f"""
    ---- ESTADO ACTUAL ----
    Energía: {energia}
    Tiempo: {tiempo}
    Cerraduras Abiertas: {cerraduras_abiertas}/3
    Alarma: {alarma}
    """)

    opcion = input("""
    Seleccione una opción del menú:
    1. Forzar cerradura
    2. Hackear panel
    3. Descansar
    Opción: """)

    while not opcion.isdigit():
        print("Error: ingrese un número válido.")
        opcion = input("""
        Seleccione una opción del menú:
        1. Forzar cerradura
        2. Hackear panel
        3. Descansar
        Opción: """)

    opcion = int(opcion)

    if opcion < 1 or opcion > 3:
        print("Error: opción fuera de rango.")
        continue

    # Opción 1: Forzar cerradura    
    if opcion == 1:
        forzar_seguidas += 1
        energia -= 20
        tiempo -= 2

        # La tercera acción consecutiva de forzar activa la alarma y no abre cerradura
        if forzar_seguidas == 3:
            alarma = True
            print("Cerradura trabada. Alarma activada.")


        # Riesgo de alarma con energía menor a 40
        if forzar_seguidas < 3 and energia < 40:
            numero_cerradura = input("""
            Riesgo de alarma. 
            Ingrese un número del 1 al 3:
            """)

            while not numero_cerradura.isdigit():
                print("Error: ingrese un número válido.")
                numero_cerradura = input("Ingrese un número del 1 al 3: ")

            numero_cerradura = int(numero_cerradura)

            while numero_cerradura < 1 or numero_cerradura > 3:
                print("Error: opción fuera de rango.")
                numero_cerradura = input("Ingrese un número del 1 al 3: ")

                while not numero_cerradura.isdigit():
                    print("Error: ingrese un número válido.")
                    numero_cerradura = input("Ingrese un número del 1 al 3: ")

                numero_cerradura = int(numero_cerradura)

            if numero_cerradura == 3:
                alarma = True
                print("Alarma activada.")
            
        if not alarma:
            cerraduras_abiertas += 1

    # Opción 2: Hackear panel
    elif opcion == 2:
        forzar_seguidas = 0
        energia -= 10
        tiempo -= 3


        # Hackeo de 4 pasos que agrega una letra en cada uno
        for i in range(4):
            codigo_parcial += "A"
            print(f"Paso {i + 1}/4 - Hackeando Panel...")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Hackeo exitoso, se abrió una cerradura.")

    # Opción 3: Descansar
    elif opcion == 3:
        forzar_seguidas = 0
        energia += 15

        if energia > 100:
            energia = 100

        tiempo -= 1

        if alarma:
            energia -= 10


# Condiciones de fin del juego
if cerraduras_abiertas == 3:
    print("VICTORIA")

elif alarma and tiempo <= 3:
    print("DERROTA (bloqueo)")

elif energia <= 0 or tiempo <= 0:
    print("DERROTA")
