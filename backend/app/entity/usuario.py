from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.config.data_base import Base

class UsuarioORM(Base):
    __tablename__ = "usuario_tb"
    cedula = Column(String(80), primary_key=True)
    nombre = Column(String(80))
    correo = Column(String(100), unique=True)
    contrasena = Column(String(80))
    rol = Column(String(100))

    avisos = relationship("AvisoORM", back_populates="usuario")

    def __init__(self, cedula, nombre, correo, contrasena, rol):
        self.cedula = cedula
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.rol = rol

    def __repr__(self):
        return f"Usuario(cedula='{self.cedula}', nombre='{self.nombre}', correo='{self.correo}', rol='{self.rol}')"