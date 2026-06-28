from app.config.data_base import SessionLocal
from app.entity.aviso import AvisoORM

class AvisoRepository:
    def __init__(self):
        self.db = SessionLocal()

    def create(self, avisoORM: AvisoORM):
        self.db.add(avisoORM)
        self.db.commit()
        self.db.refresh(avisoORM)
        return avisoORM

    def get_by_codigo(self, codigo:str):
        return self.db.query(AvisoORM).filter_by(codigo = codigo).first()

    def get_all(self):
        return self.db.query(AvisoORM).all()

    def get_by_usuario(self, cedula_usuario:str):
        return self.db.query(AvisoORM).filter_by(cedula_usuario = cedula_usuario).all()

    def get_by_estado(self, estado:str):
        return self.db.query(AvisoORM).filter_by(estado = estado).all()

    def get_by_tipo_dano(self, tipo_dano:str):
        return self.db.query(AvisoORM).filter_by(tipo_dano = tipo_dano).all()

    def update(self, aviso_new:AvisoORM):
        aviso = self.get_by_codigo(aviso_new.codigo)

        if aviso:
            aviso.cedula_usuario = aviso_new.cedula_usuario
            aviso.tipo_dano = aviso_new.tipo_dano
            aviso.descripcion = aviso_new.descripcion
            aviso.ubicacion = aviso_new.ubicacion
            aviso.fecha = aviso_new.fecha
            aviso.estado = aviso_new.estado
            self.db.commit()
        return aviso

    def update_estado(self, codigo:str, estado:str):
        aviso = self.get_by_estado(codigo)

        if aviso:
            aviso.estado = estado
            self.db.commit()
        return aviso

    def delete(self, codigo:str):
        aviso = self.get_by_codigo(codigo)

        if aviso:
            self.db.delete(aviso)
            self.db.commit()
        return aviso