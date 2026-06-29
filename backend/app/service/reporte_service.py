from app.repository.aviso_repository import AvisoRepository
from app.repository.seguimiento_repository import SeguimientoRepository


class ReporteService:

    def __init__(self):
        self.aviso_repo = AvisoRepository()
        self.seguimiento_repo = SeguimientoRepository()

    def obtener_estadisticas_generales(self):
        avisos = self.aviso_repo.get_all()

        total = len(avisos)
        pendientes = len(self.aviso_repo.get_by_estado("Pendiente"))
        en_proceso = len(self.aviso_repo.get_by_estado("En proceso"))
        resueltos = len(self.aviso_repo.get_by_estado("Resuelto"))

        return {
            "total": total,
            "pendientes": pendientes,
            "en_proceso": en_proceso,
            "resueltos": resueltos
        }

    def contar_avisos_por_tipo(self):
        avisos = self.aviso_repo.get_all()
        conteo = {}

        for aviso in avisos:
            if aviso.tipo_dano not in conteo:
                conteo[aviso.tipo_dano] = 0
            conteo[aviso.tipo_dano] += 1
        return conteo

    def obtener_avisos_pendientes(self):
        return self.aviso_repo.get_by_estado("Pendiente")

    def obtener_avisos_en_proceso(self):
        return self.aviso_repo.get_by_estado("En proceso")

    def obtener_avisos_resueltos(self):
        return self.aviso_repo.get_by_estado("Resuelto")

    def obtener_reporte_seguimientos_por_aviso(self, codigo_aviso):
        seguimientos = self.seguimiento_repo.get_by_aviso(codigo_aviso)

        return {
            "codigo_aviso": codigo_aviso,
            "cantidad_seguimientos": len(seguimientos),
            "seguimientos": seguimientos
        }