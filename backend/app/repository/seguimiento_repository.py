from app.config.data_base import SessionLocal
from app.entity.seguimiento import SeguimientoORM

class SeguimientoRepository:
    def __init__(self):
        self.db = SessionLocal()

    def create(self, seguimientoORM:SeguimientoORM):
        self.db.add(seguimientoORM)
        self.db.commit()
        return seguimientoORM

    def get_by_codigo(self, codigo_seguimiento: str):
        return self.db.query(SeguimientoORM).filter_by(
            codigo_seguimiento=codigo_seguimiento
        ).first()

    def get_all(self):
        return self.db.query(SeguimientoORM).all()

    def get_by_aviso(self, codigo_aviso: str):
        return self.db.query(SeguimientoORM).filter_by(
            codigo_aviso=codigo_aviso
        ).all()

    def update(self, seguimiento_new: SeguimientoORM):
        seguimiento = self.get_by_codigo(seguimiento_new.codigo_seguimiento)

        if seguimiento:
            seguimiento.codigo_aviso = seguimiento_new.codigo_aviso
            seguimiento.estado = seguimiento_new.estado
            seguimiento.observacion = seguimiento_new.observacion
            seguimiento.fecha_actualizacion = seguimiento_new.fecha_actualizacion
            seguimiento.responsable = seguimiento_new.responsable

            self.db.commit()

        return seguimiento

    def delete(self, codigo_seguimiento:str):
        seguimiento = self.get_by_codigo(codigo_seguimiento)

        if seguimiento:
            self.db.delete(seguimiento)
            self.db.commit()
        return seguimiento