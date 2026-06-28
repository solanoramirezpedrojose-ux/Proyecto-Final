from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.config.data_base import Base

class AvisoORM(Base):
    __tablename__ = "aviso_tb"
    codigo = Column(String(80), primary_key=True)
    cedula_usuario = Column(String(80), ForeignKey("usuario_tb.cedula"))
    tipo_dano = Column(String(300))
    descripcion = Column(String(300))
    ubicacion = Column(String(120))
    fecha = Column(String(20))
    estado = Column(String(100))

    usuario = relationship("UsuarioORM", back_populates="avisos")
    seguimientos = relationship("SeguimientoORM", back_populates="aviso")

    def __init__(self, codigo, cedula_usuario, tipo_dano, descripcion, ubicacion, fecha, estado):
        self.codigo = codigo
        self.cedula_usuario = cedula_usuario
        self.tipo_dano = tipo_dano
        self.descripcion = descripcion
        self.ubicacion = ubicacion
        self.fecha = fecha
        self.estado = estado

    def __repr__(self):
            return f"Aviso(codigo='{self.codigo}', cedula_usuario='{self.cedula_usuario}', estado='{self.estado}')"