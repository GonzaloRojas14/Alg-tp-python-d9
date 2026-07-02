
import os
from validaciones import pedir_entero
from datos import cargar_huespedes
from datos import cargar_habitaciones
from datos import cargar_reservas
from datos import guardar_huespedes
from datos import guardar_habitaciones
from datos import guardar_reservas

def limpiar_pantalla():
    """Limpia la terminal para evitar que los menus
    se apilen visualmente."""
    # os.name == 'nt' en Windows, 'posix' en Mac/Linux
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def pausar():
    """Espera a que el usuario presione Enter antes
    de limpiar la pantalla. Evita que los resultados
    desaparezcan inmediatamente."""
    input("\n  Presione Enter para continuar...")


def mostrar_menu_principal():
    """Muestra el menu principal del sistema.
    Accion elemental de salida (Escribir)."""
    limpiar_pantalla()
    print("\n" + "=" * 44)
    print("   SISTEMA DE GESTION DE HOTEL")
    print("=" * 44)
    print("  1. Gestion de huespedes")
    print("  2. Gestion de habitaciones")
    print("  3. Reservas (Check-in)")
    print("  4. Check-out")
    print("  5. Estadisticas")
    print("  6. Guardar y salir")
    print("-" * 44)


def menu_huespedes(lista_huespedes, lista_reservas):
    """Submenu de gestion de huespedes.
    Bucle while + if-elif-else."""
    seguir = True  # bandera
    while seguir:
        limpiar_pantalla()
        print("\n" + "-" * 36)
        print("   GESTION DE HUESPEDES")
        print("-" * 36)
        print("  1. Registrar nuevo huesped")
        print("  2. Ver todos los huespedes")
        print("  3. Buscar huesped por DNI")
        print("  4. Eliminar huesped")
        print("  5. Volver al menu principal")
        print("-" * 36)

        opcion = pedir_entero(
            "  Seleccione opcion (1-5): ", 1, 5,
            cancelable=False
        )

        if opcion == 1:
            #registrar_huesped
            pausar()
        elif opcion == 2:
            #mostrar_huespedes
            pausar()
        elif opcion == 3:
            from validaciones import pedir_dni
            dni = pedir_dni("  DNI a buscar")
            pausar()
        elif opcion == 4:
            pausar()
        elif opcion == 5:
            seguir = False


def menu_habitaciones(lista_hab):
    """Submenu de gestion de habitaciones.
    Bucle while + if-elif-else."""
    seguir = True  # bandera
    while seguir:
        limpiar_pantalla()
        print("\n" + "-" * 40)
        print("   GESTION DE HABITACIONES")
        print("-" * 40)
        print("  1. Ver todas las habitaciones")
        print("  2. Ver habitaciones disponibles")
        print("  3. Cambiar estado de habitacion")
        print("  4. Volver al menu principal")
        print("-" * 40)

        opcion = pedir_entero(
            "  Seleccione opcion (1-4): ", 1, 4,
            cancelable=False
        )

        if opcion == 1:
            #mostrar_habitaciones
            pausar()
        elif opcion == 2:
            #mostrar_disponibles
            pausar()
        elif opcion == 3:
            # Cambiar estado (ej: mantenimiento)
            num = pedir_entero(
                "  Numero de habitacion", 100, 399
            )
            if num is not None:
                print("  Estados posibles:")
                print("    1. disponible")
                print("    2. mantenimiento")
                est = pedir_entero(
                    "  Seleccione estado (1-2)",
                    1, 2
                )
                if est is not None:
                    if est == 1:
                        nuevo = "disponible"
                    else:
                        nuevo = "mantenimiento"
                    resultado = cambiar_estado(
                        lista_hab, num, nuevo
                    )
                    if resultado:
                        print("  Estado actualizado"
                              " correctamente.")
            pausar()
        elif opcion == 4:
            seguir = False


def menu_estadisticas(lista_reservas, lista_hab,
                      lista_huespedes):
    """Submenu de estadisticas.
    Bucle while + if-elif-else."""
    seguir = True  # bandera
    while seguir:
        limpiar_pantalla()
        print("\n" + "-" * 40)
        print("   ESTADISTICAS")
        print("-" * 40)
        print("  1. Reporte de ocupacion")
        print("  2. Ingresos totales")
        print("  3. Ocupacion por tipo de habitacion")
        print("  4. Huesped con mas noches")
        print("  5. Volver al menu principal")
        print("-" * 40)

        opcion = pedir_entero(
            "  Seleccione opcion (1-5): ", 1, 5,
            cancelable=False
        )

        if opcion == 1:
            pausar()
        elif opcion == 2:
            pausar()
        elif opcion == 3:
            pausar()
        elif opcion == 4:
            pausar()
        elif opcion == 5:
            seguir = False


def main():
    """Funcion principal del programa.
    Carga datos, ejecuta menu y guarda al salir."""
    print("\n  Cargando datos del sistema...")

    # Cargar datos desde archivos .txt
    lista_huespedes = cargar_huespedes()
    lista_habitaciones = cargar_habitaciones()
    lista_reservas = cargar_reservas()

    # Si no hay habitaciones, inicializar
    if len(lista_habitaciones) == 0:
        print("  Primera ejecucion detectada.")
        print("  Inicializando habitaciones del"
              " hotel...")
        #guardar habitaciones
        guardar_habitaciones(lista_habitaciones)

    print("  Datos cargados correctamente.")
    print("  Huespedes: "
          + str(len(lista_huespedes)))
    print("  Habitaciones: "
          + str(len(lista_habitaciones)))
    print("  Reservas: "
          + str(len(lista_reservas)))

    # Bucle principal del menu (while, pre-test)
    seguir = True  # bandera
    while seguir:
        mostrar_menu_principal()
        opcion = pedir_entero(
            "  Seleccione opcion (1-6): ", 1, 6,
            cancelable=False
        )

        if opcion == 1:
            menu_huespedes(
                lista_huespedes, lista_reservas
            )
        elif opcion == 2:
            menu_habitaciones(lista_habitaciones)
        elif opcion == 3:
            pausar()
        elif opcion == 4:
            pausar()
        elif opcion == 5:
            menu_estadisticas(
                lista_reservas,
                lista_habitaciones,
                lista_huespedes
            )
        elif opcion == 6:
            # Guardar todos los datos antes de salir
            print("\n  Guardando datos...")
            guardar_huespedes(lista_huespedes)
            guardar_habitaciones(lista_habitaciones)
            guardar_reservas(lista_reservas)
            print("  Datos guardados correctamente.")
            print("\n  Gracias por usar el Sistema"
                  " de Gestion de Hotel.")
            print("  Hasta pronto!\n")
            seguir = False


# Punto de entrada del programa
if __name__ == "__main__":
    main()
