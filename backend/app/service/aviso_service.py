from app.entity.aviso import AvisoORM
from app.repository.aviso_repository import AvisoRepository
from app.repository.usuario_repository import UsuarioRepository
from app.repository.seguimiento_repository import SeguimientoRepository

class AvisoService:
    def __init__(self):
        self.aviso_repo = AvisoRepository()
        self.usuario_repo = UsuarioRepository()
        self.seguimiento_repo = SeguimientoRepository()

    def registrar_aviso(self, codigo, cedula_usuario, tipo_dano, descripcion, ubicacion, fecha, estado):
        if not codigo.strip():
            raise ValueError("El codigo del aviso no puede estar vacio")
        if not cedula_usuario.strip():
            raise ValueError("La cedula del usuario no puede estar vacia")
        if not tipo_dano.strip():
            raise ValueError("El tipo de dano no puede estar vacio")
        if not descripcion.strip():
            raise ValueError("La descripcion no puede estar vacia")
        if not ubicacion.strip():
            raise ValueError("La ubicacion no puede estar vacia")
        if not fecha.strip():
            raise ValueError("La fecha no puede estar vacia")
        estados_validos = ["Pendiente", "En proceso", "Resuelto"]
        if estado not in estados_validos:
            raise ValueError("El estado debe ser Pendiente, En proceso o Resuelto")
        if self.aviso_repo.get_by_codigo(codigo):
            raise ValueError("Ya existe un aviso con ese codigo")
        if not self.usuario_repo.get_by_cedula(cedula_usuario):
            raise ValueError("No existe un usuario registrado con esa cedula")

        aviso = AvisoORM(
            codigo,
            cedula_usuario,
            tipo_dano,
            descripcion,
            ubicacion,
            fecha,
            estado
        )
        return self.aviso_repo.create(aviso)

    def buscar_aviso_por_codigo(self, codigo):
        aviso = self.aviso_repo.get_by_codigo(codigo)
        if not aviso:
            raise ValueError("No existe aviso con ese codigo")
        return aviso

    def obtener_todos_los_avisos(self):
        return self.aviso_repo.get_all()

    def obtener_avisos_por_usuario(self, cedula_usuario):
        return self.aviso_repo.get_by_usuario(cedula_usuario)

    def obtener_avisos_por_estado(self, estado):
        return self.aviso_repo.get_by_estado(estado)

    def obtener_avisos_por_tipo_dano(self, tipo_dano):
        return self.aviso_repo.get_by_tipo_dano(tipo_dano)

    def actualizar_aviso(self, codigo, cedula_usuario, tipo_dano, descripcion, ubicacion, fecha, estado):
        if not codigo.strip():
            raise ValueError("El codigo del aviso no puede estar vacio")
        if not cedula_usuario.strip():
            raise ValueError("La cedula del usuario no puede estar vacia")
        if not tipo_dano.strip():
            raise ValueError("El tipo de dano no puede estar vacio")
        if not descripcion.strip():
            raise ValueError("La descripcion no puede estar vacia")
        if not ubicacion.strip():
            raise ValueError("La ubicacion no puede estar vacia")
        if not fecha.strip():
            raise ValueError("La fecha no puede estar vacia")
        estados_validos = ["Pendiente", "En proceso", "Resuelto"]
        if estado not in estados_validos:
            raise ValueError("El estado debe ser Pendiente, En proceso o Resuelto")
        if not self.usuario_repo.get_by_cedula(cedula_usuario):
            raise ValueError("No existe un usuario registrado con esa cedula")
        aviso = AvisoORM(
            codigo,
            cedula_usuario,
            tipo_dano,
            descripcion,
            ubicacion,
            fecha,
            estado
        )
        aviso_actualizado = self.aviso_repo.update(aviso)
        if not aviso_actualizado:
            raise ValueError("No existe un aviso con ese codigo")
        return aviso_actualizado

    def actualizar_estado_aviso(self, codigo, estado):
        estados_validos = ["Pendiente", "En proceso", "Resuelto"]

        if estado not in estados_validos:
            raise ValueError("El estado debe ser Pendiente, En proceso o Resuelto")

        aviso_actualizado = self.aviso_repo.update_estado(codigo, estado)

        if not aviso_actualizado:
            raise ValueError("No existe un aviso con ese codigo")

        return aviso_actualizado

    def eliminar_aviso(self, codigo):
        seguimientos = self.seguimiento_repo.get_by_aviso(codigo)
        if len(seguimientos) > 0:
            raise ValueError("No se puede eliminar el aviso porque tiene seguimientos registrados")

        aviso_eliminado = self.aviso_repo.delete(codigo)

        if not aviso_eliminado:
            raise ValueError("No existe aviso con ese codigo")
        return {
            "message": "Aviso eliminado correctamente"
        }