from app.entity.usuario import UsuarioORM
from app.repository.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self):
        self.repo = UsuarioRepository()

    def registrar_usuario(self, cedula, nombre, correo, contrasena, rol):
        if not cedula.strip():
            raise ValueError("La cedula no puede estar vacia")
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacio")
        if not correo.strip():
            raise ValueError("El correo no puede estar vacio")
        if not contrasena.strip():
            raise ValueError("La contrasena no puede estar vacia")
        if not rol.strip():
            raise ValueError("El rol no puede estar vacio")
        roles_validos = ["administrador", "ciudadano"]
        if rol.lower() not in roles_validos:
            raise ValueError("El rol debe ser administrador o ciudadano")
        if self.repo.get_by_cedula(cedula):
            raise ValueError("Ya existe un usuario con esa cedula")
        if self.repo.get_by_correo(correo):
            raise ValueError("Ya existe un usuario con ese correo")

        usuario = UsuarioORM(
            cedula,
            nombre,
            correo,
            contrasena,
            rol.lower()
        )
        return self.repo.create(usuario)

    def buscar_usuario_por_cedula(self, cedula):
        usuario = self.repo.get_by_cedula(cedula)

        if not usuario:
            raise ValueError("No existe usuario con esa cedula")
        return usuario

    def buscar_usuario_por_correo(self, correo):
        usuario = self.repo.get_by_correo(correo)

        if not usuario:
            raise ValueError("No existe un usuario con ese correo")
        return usuario

    def obtener_todos_los_usuarios(self):
        return self.repo.get_all()

    def actualizar_usuario(self, cedula, nombre, correo, contrasena, rol):
        usuario = UsuarioORM(
            cedula,
            nombre,
            correo,
            contrasena,
            rol
        )
        usuario_actualizado = self.repo.update(usuario)

        if not usuario_actualizado:
            raise ValueError("No existe usuario con esa cedula")
        return usuario_actualizado

    def eliminar_usuario(self, cedula):
        usuario = self.repo.delete(cedula)

        if not usuario:
            raise ValueError("No existe usuario con esa cedula")
        return usuario