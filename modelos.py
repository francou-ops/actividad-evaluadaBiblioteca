from sqlalchemy import String, CheckConstraint, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from conexion import Base

class Libro(Base):
    __tablename__="libro"

    __table_args__ = (
        CheckConstraint("ejemplares_disponibles >= 0", name="check_ejemplares_disponibles"),
    )
    id: Mapped[int] = mapped_column(nullable=False, primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100), nullable=False)
    autor: Mapped[str] = mapped_column(String(30), nullable=False)
    ejemplares_disponibles: Mapped[int] = mapped_column(Integer, nullable=False)



class Usuario(Base):
    __tablename__="usuario"

    id: Mapped[int] = mapped_column(nullable=False, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(30), nullable=False)
    correo: Mapped[str] = mapped_column(String(50), nullable=False) # Falta que sea unico


class Prestamo(Base):
    __tablename__="prestamo"

    __table_args__= (
        CheckConstraint("cantidad > 0", name="check_cantidad"),
    )

    id: Mapped[int] = mapped_column(nullable=False, primary_key=True)
    libro_id: Mapped[int] = mapped_column(ForeignKey("libro.id"), nullable=False)
    usuario: Mapped[int] = mapped_column(ForeignKey("usuario.id"), nullable=False)
    fecha: Mapped[str] = mapped_column(String(10)) # AAA-MM-DD
    cantidad: Mapped[int] = mapped_column(Integer)
    estado: Mapped[bool] = mapped_column(Boolean, default=True) # True: activo; False: devuelto
