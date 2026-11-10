from modelos import Libro, Usuario, Prestamo
from conexion import SessionLocal

def insertar_libro(titulo, autor, ejemplares_disponibles):
    if not titulo.strip():
        raise ValueError("El título no puede estar vacío.")
    if not autor.strip():
        raise ValueError("El autor no puede estar vacío.")
    if ejemplares_disponibles < 0:
        raise ValueError("El número de ejemplares disponibles no puede ser negativo.")

    libro = Libro(
        titulo=titulo.strip(),
        autor=autor.strip(),
        ejemplares_disponibles=ejemplares_disponibles
    )
    with SessionLocal() as session:
        session.add(libro)
        session.commit()


def insertar_usuario(nombre, correo):
    if not nombre.strip():
        raise ValueError("El nombre no puede estar vacío.")
    if not correo.strip():
        raise ValueError("El correo no puede estar vacío.")

    usuario = Usuario(
        nombre=nombre.strip(),
        correo=correo.strip()
    )
    with SessionLocal() as session:
        session.add(usuario)
        session.commit()

def insertar_prestamo(libro_id, usuario_id, fecha, cantidad):
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor que cero.")

    with SessionLocal() as session:
        usuario = session.get(Usuario, usuario_id)
        libro = session.get(Libro, libro_id)
        if usuario is None:
            raise ValueError("No existe un usuario con ese ID.")
        if libro is None:
            raise ValueError("No existe un libro con ese ID.")
        if cantidad > libro.ejemplares_disponibles:
            raise ValueError("No hay suficientes ejemplares disponibles.")

        libro.ejemplares_disponibles -= cantidad
        session.add(Prestamo(
            libro_id=libro_id, usuario=usuario_id, fecha=fecha,
            cantidad=cantidad, estado=True
        ))
        session.commit()
