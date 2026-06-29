from app.entity.seguimiento import SeguimientoORM
from app.repository.seguimiento_repository import SeguimientoRepository
from app.repository.aviso_repository import AvisoRepository


class SeguimientoService:

    def __init__(self):
        self.seguimiento_repo = SeguimientoRepository()
        self.aviso_repo = AvisoRepository()

    def registrar_seguimiento(self, codigo_seguimiento, codigo_aviso, estado, observacion, fecha_actualizacion, responsable):
        if not codigo_seguimiento.strip():
            raise ValueError("El codigo del seguimiento no puede estar vacio")
        if not codigo_aviso.strip():
            raise ValueError("El codigo del aviso no puede estar vacio")
        if not estado.strip():
            raise ValueError("El estado no puede estar vacio")
        if not observacion.strip():
            raise ValueError("La observacion no puede estar vacia")
        if not fecha_actualizacion.strip():
            raise ValueError("La fecha de actualizacion no puede estar vacia")
        if not responsable.strip():
            raise ValueError("El responsable no puede estar vacio")
        estados_validos = ["Pendiente", "En proceso", "Resuelto"]
        if estado not in estados_validos:
            raise ValueError("El estado debe ser Pendiente, En proceso o Resuelto")
        if self.seguimiento_repo.get_by_codigo(codigo_seguimiento):
            raise ValueError("Ya existe un seguimiento con ese codigo")
        aviso = self.aviso_repo.get_by_codigo(codigo_aviso)
        if not aviso:
            raise ValueError("No existe un aviso con ese codigo")

        seguimiento = SeguimientoORM(
            codigo_seguimiento,
            codigo_aviso,
            estado,
            observacion,
            fecha_actualizacion,
            responsable
        )
        self.seguimiento_repo.create(seguimiento)
        aviso.estado = estado
        self.aviso_repo.update(aviso)
        return seguimiento

    def buscar_seguimiento_por_codigo(self, codigo_seguimiento):
        seguimiento = self.seguimiento_repo.get_by_codigo(codigo_seguimiento)

        if not seguimiento:
            raise ValueError("No existe un seguimiento con ese codigo")
        return seguimiento

    def obtener_todos_los_seguimientos(self):
        return self.seguimiento_repo.get_all()

    def obtener_seguimientos_por_aviso(self, codigo_aviso):
        if not self.aviso_repo.get_by_codigo(codigo_aviso):
            raise ValueError("No existe un aviso con ese codigo")
        return self.seguimiento_repo.get_by_aviso(codigo_aviso)

    def actualizar_seguimiento(self, codigo_seguimiento, codigo_aviso, estado, observacion, fecha_actualizacion, responsable):
        estados_validos = ["Pendiente", "En proceso", "Resuelto"]

        if estado not in estados_validos:
            raise ValueError("El estado debe ser Pendiente, En proceso o Resuelto")

        seguimiento = SeguimientoORM(
            codigo_seguimiento,
            codigo_aviso,
            estado,
            observacion,
            fecha_actualizacion,
            responsable
        )

        seguimiento_actualizado = self.seguimiento_repo.update(seguimiento)

        if not seguimiento_actualizado:
            raise ValueError("No existe un seguimiento con ese codigo")

        aviso = self.aviso_repo.get_by_codigo(codigo_aviso)

        if aviso:
            aviso.estado = estado
            self.aviso_repo.update(aviso)
        return seguimiento_actualizado

    def eliminar_seguimiento(self, codigo_seguimiento):
        seguimiento_eliminado = self.seguimiento_repo.delete(codigo_seguimiento)

        if not seguimiento_eliminado:
            raise ValueError("No existe un seguimiento con ese codigo")
        return seguimiento_eliminado