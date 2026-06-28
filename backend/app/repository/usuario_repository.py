from app.config.data_base import SessionLocal
from app.entity.usuario import UsuarioORM

class UsuarioRepository:
    def __init__(self):
        self.db = SessionLocal()

    def create(self, usuarioORM:UsuarioORM):
        self.db.add(usuarioORM)
        self.db.commit()
        self.db.refresh(usuarioORM)
        return usuarioORM

    def get_by_cedula(self, cedula:str):
        return self.db.query(UsuarioORM).filter_by(cedula = cedula).first()

    def get_by_correo(self, correo:str):
        return self.db.query(UsuarioORM).filter_by(correo = correo).first()

    def get_all(self):
        return self.db.query(UsuarioORM).all()

    def update(self, usuario_new:UsuarioORM):
        usuario = self.get_by_cedula(usuario_new.cedula)

        if usuario:
            usuario.nombre = usuario_new.nombre
            usuario.correo = usuario_new.correo
            usuario.contrasena = usuario_new.contrasena
            usuario.rol = usuario_new.rol
            self.db.commit()
        return usuario

    def delete(self, cedula:str):
        usuario = self.get_by_cedula(cedula)

        if usuario:
            self.db.delete(usuario)
            self.db.commit()