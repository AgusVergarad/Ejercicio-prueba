def registro_cientificos():
    # 1 y 2. Solicitar cantidad de científicos
    cantidad_valida = 0
    num_cientificos = 0
   
    while cantidad_valida == 0:
        try:
            num_cientificos = int(input("¿Cuántos científicos desea registrar?: "))
            if num_cientificos > 0:
                cantidad_valida = 1  # Cambiamos la variable para salir del ciclo
            else:
                print("¡Dato de investigación inválido! Ingresa un entero positivo para continuar el registro.")
        except ValueError:
            print("¡Dato de investigación inválido! Ingresa un entero positivo para continuar el registro.")

    # 5. Contadores automáticos
    investigadores_principales = 0
    investigadores_asistentes = 0

    # 3. Registro iterativo usando un ciclo for (o podría ser un while también)
    contador_cientificos = 0
    while contador_cientificos < num_cientificos:
        print("\n--- Nuevo Registro ---")
       
        # Validación de ID
        id_valido = 0
        id_cientifico = ""
        while id_valido == 0:
            id_cientifico = input("Ingresa el ID del científico (mínimo 12 caracteres, sin espacios): ")
            if len(id_cientifico) >= 12 and " " not in id_cientifico:
                id_valido = 1
            else:
                print("ID inválido. Asegúrate de que tenga al menos 12 caracteres y ningún espacio.")

        # Validación de publicaciones
        pub_valida = 0
        publicaciones = 0
        while pub_valida == 0:
            try:
                publicaciones = int(input(f"Ingresa el número de publicaciones de {id_cientifico}: "))
                if publicaciones > 0:
                    pub_valida = 1
                else:
                    print("¡Error de registro! Ingresa un número entero positivo para el número de publicaciones.")
            except ValueError:
                print("¡Error de registro! Ingresa un número entero positivo para el número de publicaciones.")

        # 4. Clasificación del Científico
        if publicaciones > 12:
            investigadores_principales += 1
        else:
            investigadores_asistentes += 1
           
        contador_cientificos += 1

    # 6. Salida Final
    print("\n--- Resumen de Registro ---")
    print(f"¡El instituto cuenta con {investigadores_principales} Investigadores Principales y {investigadores_asistentes} Investigadores Asistentes! ¡Ciencia en marcha!")

# registro_cientificos()


def gestion_laboratorio():
    print("¡Bienvenido al sistema de gestión de equipos del Laboratorio Central de Investigación!")
   
    # Variables de estado inicial
    equipos_disponibles = 25
    capacidad_maxima = 25
    historial_usos = 0
   
    # Variable de control para repetir el menú
    menu_activo = 1
   
    while menu_activo == 1:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1.- Equipos disponibles.")
        print("2.- Asignar equipo.")
        print("3.- Liberar equipo.")
        print("4.- Historial de usos.")
        print("5.- Salir.")
       
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            opcion = 0 # Asignar valor inválido para que caiga en el 'else'
           
        if opcion == 1:
            print(f"\nActualmente hay {equipos_disponibles} equipos disponibles.")
           
        elif opcion == 2:
            try:
                cantidad = int(input("\n¿Cuántos equipos desea asignar?: "))
                if cantidad <= 0:
                    print("Error: La cantidad a asignar debe ser mayor a 0.")
                elif cantidad > equipos_disponibles:
                    print(f"Error: No hay suficiente disponibilidad. Solo quedan {equipos_disponibles} equipos.")
                else:
                    equipos_disponibles -= cantidad
                    historial_usos += cantidad
                    print(f"Se han asignado {cantidad} equipos exitosamente.")
            except ValueError:
                print("Error: Ingrese un número entero.")
               
        elif opcion == 3:
            try:
                cantidad = int(input("\n¿Cuántos equipos desea liberar?: "))
                if cantidad <= 0:
                    print("Error: La cantidad a liberar debe ser mayor a 0.")
                elif (equipos_disponibles + cantidad) > capacidad_maxima:
                    print(f"Error: La liberación supera la capacidad máxima del laboratorio ({capacidad_maxima} equipos).")
                else:
                    equipos_disponibles += cantidad
                    historial_usos -= cantidad
                    print(f"Se han liberado {cantidad} equipos exitosamente.")
            except ValueError:
                print("Error: Ingrese un número entero.")
               
        elif opcion == 4:
            print(f"\nHistorial de usos (equipos actualmente asignados en esta sesión): {historial_usos}")
           
        elif opcion == 5:
            print("\nGracias por utilizar nuestro software, hasta la próxima.")
            menu_activo = 0  # Cambiamos la variable para que el while se detenga
           
        else:
            if opcion != 0:
                print("\nOpción inválida. Por favor, seleccione un número del 1 al 5.")

# gestion_laboratorio()