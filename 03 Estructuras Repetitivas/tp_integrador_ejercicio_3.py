# Nombre y Apellido: Cristian Manjarrés 
     
# TP Integrador – Repetitivas- Condicionales y Secuenciales. 
# Institución: UTN
# Carrera: Tecnicatura Universitaria en Programación
# Materia: Programación I

# ✅ Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”
# Objetivo: Reservas, cancelaciones y disponibilidad de turnos

# Validación del nombre del operador
nombre_operador = input("Por favor, ingrese el nombre del operador: ")

while not nombre_operador.isalpha():
    print("Error: el nombre debe contener solo letras.")    
    nombre_operador = input("Por favor, ingrese el nombre del operador: ")


# Inicializando turnos disponibles
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""


opcion = 0

# Menú principal del sistema

while opcion != 5:
    opcion = input("""
    1. Reservar turno
    2. Cancelar turno
    3. Ver agenda del día
    4. Ver resumen general
    5. Cerrar sistema
    Por favor, escoge una opción del menú (1-5): 
    """)

    while not opcion.isdigit():
        print("Error: por favor ingrese un número válido.")
        opcion = input("Por favor, ingrese sólo números, del 1 al 5: ")

    opcion = int(opcion)

    if opcion < 1 or opcion > 5:
        print("Error: opción fuera de rango.")
        continue

    # Opción 1: Reservar un turno
    if opcion == 1:
        dia = input("""
        Selecciona el día:
        1. Lunes
        2. Martes
        Opción: """)

        while not dia.isdigit():
            print("Error: ingrese un número válido.")
            dia = input("Ingrese 1 para el día Lunes, 2 para el día Martes: ")

        dia = int(dia)

        while dia < 1 or dia > 2:
            print("Error: opción fuera de rango.")
            dia = input("Ingrese 1 para Lunes, 2 para Martes: ")

            while not dia.isdigit():
                print("Error: ingrese un número válido.")
                dia = input("Ingrese 1 para el día lunes, 2 para el día Martes: ")

            dia = int(dia)

        nombre_paciente = input("Por favor, ingrese el nombre del paciente: ")

        while not nombre_paciente.isalpha():
            print("Error: debe contener sólo letras.")
            nombre_paciente = input("Por favor, ingrese el nombre del paciente: ")

        if dia == 1:
            if nombre_paciente == lunes1 or nombre_paciente == lunes2 or nombre_paciente == lunes3 or nombre_paciente == lunes4:
                print("Error: el paciente ya tiene reservado un turno para el día Lunes.")
            elif lunes1 == "":
                lunes1 = nombre_paciente 
                print("Turno reservado correctamente.")
            elif lunes2 == "":
                lunes2 = nombre_paciente
                print("Turno reservado correctamente.")
            elif lunes3 == "":
                lunes3 = nombre_paciente
                print("Turno reservado correctamente.")
            elif lunes4 == "":
                lunes4 = nombre_paciente
                print("Turno reservado correctamente.")
            else:
                print("No hay turnos disponibles para el día Lunes.")

        elif dia == 2:
            if nombre_paciente == martes1 or nombre_paciente == martes2 or nombre_paciente == martes3:
                print("Error: el paciente ya tiene agendado un turno para el día Martes.")
            elif martes1 == "":
                martes1 = nombre_paciente
                print("Turno reservado correctamente.")
            elif martes2 == "":
                martes2 = nombre_paciente
                print("Turno reservado correctamente.")
            elif martes3 == "":
                martes3 = nombre_paciente
                print("Turno reservado correctamente.")
            else:
                print("No hay turnos disponibles para el día Martes.")


    # Opción 2: Cancelar un turno por nombre        
    elif opcion == 2:

        dia = input("""
        Selecciona el día:
        1. Lunes
        2. Martes
        Opción: """)

        while not dia.isdigit():
            print("Por favor, ingrese un número válido.")
            dia = input("Ingrese 1 para el día Lunes, 2 para el día Martes:")

        dia = int(dia)

        while dia < 1 or dia > 2:
            print("Error: opción fuera de rango.")
            dia = input("Ingrese 1 para el día Lunes, 2 para el día Martes:")

            while not dia.isdigit():
                print("Por favor, ingrese un número válido.")
                dia = input("Ingrese 1 para el día Lunes, 2 para el día Martes: ")  

            dia = int(dia)  

        nombre_paciente = input("Por favor, ingrese el nombre del paciente: ")

        while not nombre_paciente.isalpha():
            print("Error: debe contener sólo letras.")
            nombre_paciente = input("Por favor, ingrese el nombre del paciente: ")


        if dia == 1:
            if nombre_paciente == lunes1:
                lunes1 = ""
                print("Turno cancelado correctamente.")
            elif nombre_paciente == lunes2:
                lunes2 = ""
                print("Turno cancelado correctamente.")
            elif nombre_paciente == lunes3:
                lunes3 = ""
                print("Turno cancelado correctamente.")
            elif nombre_paciente == lunes4:
                lunes4 = ""
                print("Turno cancelado correctamente.")
            else:
                print("El paciente no tiene un turno reservado para el día Lunes.")

        elif dia == 2:
            if nombre_paciente == martes1:
                martes1 = ""
                print("Turno cancelado correctamente.")
            elif nombre_paciente == martes2:
                martes2 = ""
                print("Turno cancelado correctamente.")
            elif nombre_paciente == martes3:
                martes3 = ""
                print("Turno cancelado correctamente.")
            else:
                print("El paciente no tiene un turno reservado para el día Martes.")

    # Opción 3: Mostrar la agenda del día seleccionado
    elif opcion == 3:   
        dia = input("""
        Selecciona el día:
        1. Lunes
        2. Martes
        Opción: """)

        while not dia.isdigit():
            print("Por favor, ingrese un número válido.")
            dia = input("Ingrese 1 para el día Lunes, 2 para el día Martes: ")

        dia = int(dia)

        while dia < 1 or dia > 2:
            print("Error: opción fuera de rango.")
            dia = input("Ingrese 1 para el día Lunes, 2 para el día Martes: ")

            while not dia.isdigit():
                print("Por favor, ingrese un número válido.")
                dia = input("Ingrese 1 para el día Lunes, 2 para el día Martes: ")

            dia = int(dia)

        if dia == 1:

            print("\n--- Agenda del día Lunes ---")


            if lunes1 == "":
                print("Turno 1: (libre)")
            else:
                print(f"Turno 1: {lunes1}")

            if lunes2 == "":
                print("Turno 2: (libre)")
            else:
                print(f"Turno 2: {lunes2}")

            if lunes3 == "":
                print("Turno 3: (libre)")
            else:
                print(f"Turno 3: {lunes3}")

            if lunes4 == "":
                print("Turno 4: (libre)")
            else:
                print(f"Turno 4: {lunes4}")

        elif dia == 2:

            print("\n--- Agenda del día Martes ---")

            if martes1 == "":
                print("Turno 1: (libre)")
            else:
                print(f"Turno 1: {martes1}")

            if martes2 == "":
                print("Turno 2: (libre)")
            else:
                print(f"Turno 2: {martes2}")

            if martes3 == "":
                print("Turno 3: (libre)")
            else:
                print(f"Turno 3: {martes3}")

    # Opción 4: Calcular y mostrar resumen general
    elif opcion == 4:

        # Contadores de turnos ocupados y disponibles
        turnos_ocupados_lunes = 0
        total_turnos_lunes = 4
        turnos_ocupados_martes = 0
        total_turnos_martes = 3

        if lunes1 != "":
            turnos_ocupados_lunes += 1
        if lunes2 != "":
            turnos_ocupados_lunes += 1
        if lunes3 != "":
            turnos_ocupados_lunes += 1
        if lunes4 != "":
            turnos_ocupados_lunes += 1

        turnos_disponibles_lunes = total_turnos_lunes - turnos_ocupados_lunes

        if martes1 != "":
            turnos_ocupados_martes += 1
        if martes2 != "":
            turnos_ocupados_martes += 1
        if martes3 != "":
            turnos_ocupados_martes += 1

        turnos_disponibles_martes = total_turnos_martes - turnos_ocupados_martes

        print(f"Turnos ocupados del día Lunes: {turnos_ocupados_lunes} turnos.")
        print(f"Turnos disponibles para el día Lunes: {turnos_disponibles_lunes} turnos.")
        print(f"Turnos ocupados del día Martes: {turnos_ocupados_martes} turnos.")
        print(f"Turnos disponibles para el día Martes: {turnos_disponibles_martes} turnos.")

        if turnos_ocupados_lunes > turnos_ocupados_martes:
            print("El día Lunes tiene más turnos ocupados que el día Martes.")
        elif turnos_ocupados_lunes < turnos_ocupados_martes:
            print("El día Martes tiene más turnos ocupados que el día Lunes.")
        else:
            print("El día Lunes y el día Martes tienen la misma cantidad de turnos ocupados.")

    # Opción 5: Cerrando el sistema
    elif opcion == 5:
        print("Saliendo del sistema... ")
