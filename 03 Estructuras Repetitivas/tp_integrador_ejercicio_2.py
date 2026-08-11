# Nombre y Apellido: Cristian Manjarrés 
    
# TP Integrador – Repetitivas- Condicionales y Secuenciales. 
# Institución: UTN
# Carrera: Tecnicatura Universitaria en Programación
# Materia: Programación I

# Ejercicio 2 — “Acceso al Campus y Menú Seguro”
# Objetivo: Login con intentos + menú de acciones con validación estricta.


# Credenciales y variables iniciales
usuario_correcto = "alumno"
clave_correcta = "python123" 
intentos = 0
cuenta_bloqueada = True
opcion = 0


# Validación del acceso, máximo de 3 intentos
while intentos < 3: 
    print(f"Intento {intentos + 1}/3")

    usuario = input("Por favor, ingrese su usuario: ")
    clave = input("Por favor, ingresa su clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        cuenta_bloqueada = False
        print("Acceso concedido.")
        break

    else:
        print("Error: credenciales inválidas.")
        intentos += 1

        if intentos == 3:
            cuenta_bloqueada = True
            print("Cuenta bloqueada")


# Menú disponible cuando el acceso es concedido
if not cuenta_bloqueada:
    while opcion != 4:
        opcion = input("""
        1. Ver estado de inscripción
        2. Cambiar clave
        3. Mostrar mensaje motivacional
        4. Salir
        Por favor, elige la opción que desees (1-4): """)


        # Validación de la opción ingresada
        while not opcion.isdigit():
            print("Error: por favor, ingrese un número válido.")
            opcion = input("Ingrese una opción del 1 al 4: ")

        opcion = int(opcion)

        if opcion < 1 or opcion > 4: 
            print("Error: opción fuera de rango.")
            continue

        if opcion == 1:
            print("Inscripto")

        # Cambio de clave: mínimo 6 caracteres, con confirmación
        elif opcion == 2:
            nueva_clave = input(
                "Por favor, ingrese su nueva clave. Mínimo seis caracteres: "
            )
            nueva_clave_confirmacion = input(
                "Por favor, confirme su nueva clave: "
            )

            if len(nueva_clave) < 6:
                print("Error: mínimo 6 caracteres.")

            elif nueva_clave == nueva_clave_confirmacion:
                clave_correcta = nueva_clave
                print("Clave cambiada correctamente.")

            else:
                print("Error: las claves no coinciden.")

        elif opcion == 3:
            print("Nadie en la breve historia de la computación ha escrito nunca un software perfecto. Es poco probable que seas el primero. - Andy Hunt")

        elif opcion == 4:
            print("Saliendo del sistema...")
