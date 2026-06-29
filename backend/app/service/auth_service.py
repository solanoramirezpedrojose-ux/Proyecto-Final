from app.repository.usuario_repository import UsuarioRepository

class AuthService:
    def __init__(self):
        self.usuario_repo = UsuarioRepository()

    def login(self, correo, contrasena):
        if not correo.strip():
            raise ValueError("El correo no puede estar vacio")

        if not contrasena.strip():
            raise ValueError("La contraseña no puede estar vacia")

        usuario = self.usuario_repo.get_by_correo(correo)

        if not usuario:
            raise ValueError("El usuario no existe")
        if usuario.contrasena != contrasena:
            raise ValueError("La contraseña es incorrecta")
        return usuario

    def es_administrador(self, usuario):
        return usuario is not None and usuario.rol.lower() == "administrador"
    def es_ciudadano(self, usuario):
        return usuario is not None and usuario.rol.lower() == "ciudadano"