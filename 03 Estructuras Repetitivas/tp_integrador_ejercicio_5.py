# Nombre y Apellido: Cristian Manjarrés 
   
# TP Integrador – Repetitivas- Condicionales y Secuenciales. 
# Institución: UTN
# Carrera: Tecnicatura Universitaria en Programación
# Materia: Programación I

# Ejercicio 5 — “Escape Room:"La Arena del Gladiador"
# Objetivo: Crear un simulador de batalla por turnos, entre un gladiador y un enemigo.

# Variables iniciales del combate
vida_gladiador = 100    
vida_enemigo = 100      
pociones = 3            
ataque_pesado = 15      
ataque_enemigo = 12     
turno_gladiador = True  
primer_turno = True

# Validación del nombre del gladiador
nombre_gladiador = input("""
---- BIENVENIDO A LA ARENA ----
Ingrese el nombre del gladiador: """)

while not nombre_gladiador.isalpha():
    print("Error: Solo se permiten letras.")
    nombre_gladiador = input("Ingrese el nombre del gladiador: ")

# Ciclo principal del combate
while vida_gladiador > 0 and vida_enemigo > 0:

    # Turno del gladiador
    if turno_gladiador:

        if primer_turno:
            print("==== INICIO DEL COMBATE ====")
        else:
            print("==== NUEVO TURNO ====")

        print(f"""
        {nombre_gladiador} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) 
        | Pociones: {pociones} |
        """)

        opcion = input("""
        Elige tu acción:
        1. Ataque Pesado
        2. Ráfaga Veloz
        3. Curar
        Opción: """)

        while not opcion.isdigit():
            print("Error: ingrese un número válido.")
            opcion = input("""
            1. Ataque Pesado
            2. Ráfaga Veloz
            3. Curar
            Opción: """)

        opcion = int(opcion)

        if opcion < 1 or opcion > 3:
            print("Error: opción fuera de rango.")
            continue

        primer_turno = False

        # Opción 1: Ataque pesado
        if opcion == 1:

            ataque_final = ataque_pesado

            # Golpe crítico cuando el enemigo tiene menos de 20 HP
            if vida_enemigo < 20:
                ataque_final = ataque_pesado * 1.5
                print("¡Golpe Crítico!")

            vida_enemigo -= ataque_final
            print(f"¡Atacaste al enemigo por {ataque_final} puntos de daño!")
            turno_gladiador = False

        # Opción 2: Ráfaga veloz
        elif opcion == 2:

            print("¡Inicias una ráfaga de golpes!")

            for i in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")
            turno_gladiador = False

        # Opción 3: Curar
        elif opcion == 3:

            if pociones > 0:
                pociones -= 1
                vida_gladiador += 30

                print(f"""Haz utilizado una poción, sumas 30 puntos de vida.
                Te quedan {pociones} pociones.""")
            else:
                print("¡No quedan pociones!")

            turno_gladiador = False

    # Turno automático del enemigo
    else:
        if vida_enemigo > 0:
            vida_gladiador -= ataque_enemigo
            print("¡El enemigo contraataca! Pierdes 12 puntos de vida.")

        turno_gladiador = True

# Resultado final del combate
if vida_gladiador > 0:
    print(f"¡VICTORIA! {nombre_gladiador} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate")
