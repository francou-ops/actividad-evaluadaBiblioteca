from insertar import insertar_libro, insertar_prestamo, insertar_usuario
from consultar import consultar_libros, consultar_usuarios, consultar_prestamos
from eliminar import eliminar_libro, eliminar_usuario, eliminar_prestamo

# Del menú 1. Registrar
def registrar_libro():
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    ejemplares_disponibles = int(input("Ingrese el número de ejemplares disponibles: "))
    insertar_libro(titulo, autor, ejemplares_disponibles)
    print("Libro registrado exitosamente.")

def registrar_usuario():
    nombre = input("Ingrese el nombre del usuario: ")
    correo = input("Ingrese el correo del usuario: ")
    insertar_usuario(nombre, correo)
    print("Usuario registrado exitosamente.")

def registrar_prestamo():
    libro_id = int(input("Ingrese el ID del libro: "))
    usuario_id = int(input("Ingrese el ID del usuario: "))
    fecha = input("Ingrese la fecha del préstamo (AAAA-MM-DD): ")
    cantidad = int(input("Ingrese la cantidad de libros prestados: "))
    insertar_prestamo(libro_id, usuario_id, fecha, cantidad)
    print("Préstamo registrado exitosamente.")


    # Del menú 2. Consultar
def pedir_libros():
    libros = consultar_libros()
    print("\nLibros registrados:")
    for libro in libros:
        print(f"ID: {libro.id}, Título: {libro.titulo}, Autor: {libro.autor}, Ejemplares disponibles: {libro.ejemplares_disponibles}")

def pedir_usuarios():
    usuarios = consultar_usuarios()
    print("\nUsuarios registrados:")
    for usuario in usuarios:
        print(f"ID: {usuario.id}, Nombre: {usuario.nombre}, Correo: {usuario.correo}")

def pedir_prestamos():
    prestamos = consultar_prestamos()
    print("\nPréstamos registrados:")
    for prestamos in prestamos:
        print(f"ID: {prestamos.id}, Libro ID: {prestamos.libro_id}, Usuario ID: {prestamos.usuario}, Fecha: {prestamos.fecha}, Cantidad: {prestamos.cantidad}, Estado: {'Activo' if prestamos.estado else 'Devuelto'}")


    # 3. Eliminar
def borrar_libro():
    libro_id = int(input("Ingrese el ID del libro a eliminar: "))
    eliminar_libro(libro_id)

def borrar_usuario():
    usuario_id = int(input("Ingrese el ID del usuario a eliminar: "))
    eliminar_usuario(usuario_id)

def borrar_prestamo():
    prestamo_id = int(input("Ingrese el ID del préstamo a eliminar: "))
    eliminar_prestamo(prestamo_id)


    # 4. Prestar
def prestar_libro():
    libro_id = int(input("Ingrese el ID del libro a prestar: "))
    usuario_id = int(input("Ingrese el ID del usuario que recibirá el préstamo: "))
    fecha = input("Ingrese la fecha del préstamo (AAAA-MM-DD): ")
    cantidad = int(input("Ingrese la cantidad de libros a prestar: "))
    insertar_prestamo(libro_id, usuario_id, fecha, cantidad)
    print("Préstamo registrado exitosamente.")


def main():
    while True:
        print("\nBiblioteca")
        print("1. Registrar (Libros - Usuarios - Préstamos)")
        print("2. Consultar (Libros - Usuarios - Préstamos)")
        print("3. Eliminar (Libros - Usuarios - Préstamos)")
        print("4. Prestar libro")
        print("5. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            print("\nElija una opción:")
            print("1. Registrar Libro")
            print("2. Registrar Usuario")
            print("3. Registrar Préstamo")
            sub_opcion = int(input("Seleccione una opción: "))

            # Menú de opción 1
            if sub_opcion == 1:
                registrar_libro()
            elif sub_opcion == 2:
                registrar_usuario()
            elif sub_opcion == 3:
                registrar_prestamo()
            else:
                print("Opción inválida. Intente nuevamente.")


        elif opcion == 2:
            print("\nElija una opción:")
            print("1. Consultar Libros")
            print("2. Consultar Usuarios")
            print("3. Consultar Préstamos")
            sub_opcion = int(input("Seleccione una opción: "))

            # Menú de opción 2
            if sub_opcion == 1:
                pedir_libros()
            elif sub_opcion == 2:
                pedir_usuarios()
            elif sub_opcion == 3:
                pedir_prestamos()
            else:
                print("Opción inválida. Intente nuevamente.")

        elif opcion == 3:
            print("\nElija una opción:")
            print("1. Eliminar Libro")
            print("2. Eliminar Usuario")
            print("3. Eliminar Préstamo")
            sub_opcion = int(input("Seleccione una opción: "))
            # Menú de opción 3
            if sub_opcion == 1:
                borrar_libro()
            elif sub_opcion == 2:
                borrar_usuario()
            elif sub_opcion == 3:
                borrar_prestamo()
            else:
                print("Opción inválida. Intente nuevamente.")

        elif opcion == 4:
            prestar_libro()
        elif opcion == 5:
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
