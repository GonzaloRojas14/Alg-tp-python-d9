# Sistema de Gestión de Hotel

## Grupo D9

Peralta Luciano Ivan n\
Ramírez Pablo Nicolas n\
Rojas Gonzalo Damián n\
Vaernet Bianca Estefania n\
Zárate Brisa Yael n\

## Comisión

K1.4

## Descripción general del sistema

Sistema de gestión hotelera desarrollado en Python que se ejecuta por consola. Permite administrar las operaciones diarias de un hotel:

- **Registro de huéspedes:** Alta, consulta, búsqueda por DNI y baja de huéspedes.
- **Gestión de habitaciones:** Visualización del estado de las 13 habitaciones del hotel (5 simples, 5 dobles, 3 suites), cambio de estado a mantenimiento.
- **Check-in:** Asignación de habitaciones a huéspedes registrados, selección de tipo de habitación y cantidad de noches.
- **Check-out:** Finalización de estadías con emisión de factura, cálculo automático del monto total y liberación de la habitación.
- **Estadísticas:** Reportes de ocupación general, ocupación por tipo de habitación, ingresos totales y huésped con más noches acumuladas.
- **Persistencia:** Los datos se guardan automáticamente en archivos `.txt` al cerrar el programa y se cargan al iniciar.

### Estructura del proyecto

```
gestion_hotel/
├── main.py              # Punto de entrada y menú principal
├── habitaciones.py      # Gestión de habitaciones
├── huespedes.py         # Gestión de huéspedes
├── reservas.py          # Check-in y check-out
├── estadisticas.py      # Reportes y estadísticas
├── validaciones.py      # Validación de entradas
├── interfaz.py          # Presentación visual (colores, cuadros, tablas)
├── datos.py             # Persistencia en archivos .txt
├── README.md            # Este archivo
└── datos/               # Carpeta de datos generados
    ├── huespedes.txt
    ├── habitaciones.txt
    └── reservas.txt
```

### Conceptos aplicados

- Estructuras condicionales (`if`, `elif`, `else`)
- Estructuras repetitivas (`while`, `for`)
- Funciones con y sin retorno
- Validaciones de entrada con bucles
- Contadores y acumuladores
- Banderas (variables booleanas)
- Modularización en múltiples archivos
- Manejo de archivos `.txt` con `with open`
- Manejo de excepciones con `try/except`
- Convenciones PEP8

## Instrucciones de ejecución

### Requisitos previos

- Python 3.x instalado en el sistema.
- No se requieren bibliotecas externas.

### Cómo ejecutar

1. Abrir una terminal o consola.
2. Navegar a la carpeta del proyecto:
   ```bash
   cd ruta/a/gestion_hotel
   ```
3. Ejecutar el programa:
   ```bash
   python main.py
   ```
4. Seguir las instrucciones del menú en pantalla.

### Notas

- En la primera ejecución, el sistema inicializa automáticamente las habitaciones del hotel.
- Los datos se guardan al seleccionar la opción "Guardar y salir" del menú principal.
- Los archivos de datos se almacenan en la carpeta `datos/`.
