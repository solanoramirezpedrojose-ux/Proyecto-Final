from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.config.data_base import Base

class SeguimientoORM(Base):
    __tablename__ = "seguimiento_tb"
    codigo_seguimiento = Column(String(80), primary_key=True)
    codigo_aviso = Column(String(80), ForeignKey("aviso_tb.codigo"))
    estado = Column(String(30))
    observacion = Column(String(300))
    fecha_actualizacion = Column(String(50))
    responsable = Column(String(80))

    aviso = relationship("AvisoORM", back_populates="seguimientos")

    def __init__(self, codigo_seguimiento, codigo_aviso, estado, observacion, fecha_actualizacion, responsable):
        self.codigo_seguimiento = codigo_seguimiento
        self.codigo_aviso = codigo_aviso
        self.estado = estado
        self.observacion = observacion
        self.fecha_actualizacion = fecha_actualizacion
        self.responsable = responsable

    def __repr__(self):
        return f"Seguimiento(codigo='{self.codigo_seguimiento}', aviso='{self.codigo_aviso}', estado='{self.estado}')"