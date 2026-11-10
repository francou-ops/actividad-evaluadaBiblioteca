from sqlalchemy import select
from conexion import SessionLocal
from modelos import Libro, Usuario, Prestamo

def consultar_libros():
    with SessionLocal() as session:
        consulta = select(Libro)
        libros = session.scalars(consulta).all()
        return libros


def consultar_usuarios():
    with SessionLocal() as session:
        consulta = select(Usuario)
        usuarios = session.scalars(consulta).all()
        return usuarios

def consultar_prestamos():
    with SessionLocal() as session:
        consulta = select(Prestamo)
        prestamos = session.scalars(consulta).all()
        return prestamos
