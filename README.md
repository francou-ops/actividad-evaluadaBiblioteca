# Biblioteca

Programa de consola para registrar libros, usuarios y préstamos. Los datos se guardan en el archivo `biblioteca.db`, usando SQLite y SQLAlchemy.

## Cómo ejecutarlo

Necesitas Python 3.13 o superior y `uv` instalado.

Abre una terminal dentro de la carpeta del proyecto y ejecuta:

```bash
uv sync
```

Esto instala las dependencias. Después, crea las tablas de la base de datos:

```bash
uv run python crear_tablas.py
```

Este paso se necesita al preparar el proyecto por primera vez. Si las tablas ya existen, no borra sus datos.

Para iniciar el programa:

```bash
uv run python main.py
```

Ejecuta siempre los comandos desde la carpeta del proyecto para usar la misma base de datos.

## Menú principal

Escribe el número de la opción y presiona Enter:

```text
Biblioteca
1. Registrar (Libros - Usuarios - Préstamos)
2. Consultar (Libros - Usuarios - Préstamos)
3. Eliminar (Libros - Usuarios - Préstamos)
4. Prestar libro
5. Salir
```

### 1. Registrar

Abre un submenú para elegir qué registrar:

- **Libro:** pide título, autor y número de ejemplares disponibles.
- **Usuario:** pide nombre y correo.
- **Préstamo:** pide el ID del libro, el ID del usuario, la fecha y la cantidad de ejemplares.

Los ID se asignan automáticamente y se pueden ver en la opción Consultar.

### 2. Consultar

Permite listar libros, usuarios o préstamos. Muestra sus ID y los datos registrados. En los libros también muestra los ejemplares disponibles.

### 3. Eliminar

Permite eliminar un libro, usuario o préstamo indicando su ID.

- Un libro o usuario con préstamos registrados no se puede eliminar.
- Si se elimina un préstamo activo, sus ejemplares vuelven a estar disponibles.

### 4. Prestar libro

Registra un préstamo, igual que la opción Registrar → Préstamo. El libro y el usuario deben existir y debe haber suficientes ejemplares disponibles.

El préstamo queda activo y la cantidad prestada se descuenta de los ejemplares disponibles.

### 5. Salir

Cierra el programa. Los datos guardados se conservan para la próxima ejecución.

## Ejemplo de uso

1. Entra a **Registrar → Libro** y registra un libro con 3 ejemplares.
2. Entra a **Registrar → Usuario** y registra una persona.
3. Usa **Consultar** para ver los ID de ambos.
4. Selecciona **Prestar libro** e ingresa esos ID, una fecha como `2026-11-10` y una cantidad de `1`.
5. Consulta los libros: ahora quedan 2 ejemplares disponibles.

Ingresa números en los menús, ID y cantidades. Usa el formato `AAAA-MM-DD` para las fechas. Actualmente, una entrada inválida puede terminar el programa; puedes iniciarlo nuevamente con el mismo comando.

## Archivos principales

- `main.py`: menú e ingreso de datos.
- `conexion.py`: conexión a la base de datos.
- `modelos.py`: definición de libros, usuarios y préstamos.
- `crear_tablas.py`: creación de las tablas.
- `insertar.py`: registro de datos y préstamos.
- `consultar.py`: consultas de los registros.
- `eliminar.py`: eliminación de registros.
- `biblioteca.db`: datos guardados.
