from sqlalchemy import select
from conexion import SessionLocal
from modelos import Libro, Usuario, Prestamo

def eliminar_libro(libro_id):
    with SessionLocal() as session:
        libro = session.get(Libro, libro_id)
        if libro:
            if session.scalar(select(Prestamo.id).where(Prestamo.libro_id == libro_id)) is not None:
                raise ValueError("El libro tiene préstamos registrados y no se puede eliminar.")
            session.delete(libro)
            session.commit()
            print(f"Libro con ID {libro_id} eliminado.")
        else:
            print(f"No se encontró un libro con ID {libro_id}.")


def eliminar_usuario(usuario_id):
    with SessionLocal() as session:
        usuario = session.get(Usuario, usuario_id)
        if usuario is None:
            raise ValueError("No existe un usuario con ese ID.")
        if session.scalar(select(Prestamo.id).where(Prestamo.usuario == usuario_id)) is not None:
            raise ValueError("El usuario tiene préstamos registrados y no se puede eliminar.")
        session.delete(usuario)
        session.commit()
        print("Usuario eliminado.")


def eliminar_prestamo(prestamo_id):
    with SessionLocal() as session:
        prestamo = session.get(Prestamo, prestamo_id)
        if prestamo is None:
            raise ValueError("No existe un préstamo con ese ID.")
        if prestamo.estado:
            libro = session.get(Libro, prestamo.libro_id)
            if libro is not None:
                libro.ejemplares_disponibles += prestamo.cantidad
        session.delete(prestamo)
        session.commit()
        print("Préstamo eliminado.")
