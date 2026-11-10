from conexion import Base, engine
from modelos import Libro, Usuario, Prestamo

Base.metadata.create_all(engine)

print("Tablas creadas")
