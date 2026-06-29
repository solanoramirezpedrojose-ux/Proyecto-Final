from app.repository.aviso_repository import AvisoRepository
from app.repository.seguimiento_repository import SeguimientoRepository


class ReporteService:

    def __init__(self):
        self.aviso_repo = AvisoRepository()
        self.seguimiento_repo = SeguimientoRepository()

    def obtener_estadisticas_generales(self):
        avisos = self.aviso_repo.get_all()

        total = len(avisos)
        pendientes = 0
        en_proceso = 0
        resueltos = 0

        for aviso in avisos:
            if aviso.estado == "Pendiente":
                pendientes += 1
            elif aviso.estado == "En proceso":
                en_proceso += 1
            elif aviso.estado == "Resuelto":
                resueltos += 1

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
            tipo = aviso.tipo_dano

            if tipo not in conteo:
                conteo[tipo] = 0

            conteo[tipo] += 1

        return conteo

    def obtener_reporte_seguimientos_por_aviso(self, codigo_aviso):
        seguimientos = self.seguimiento_repo.get_by_aviso(codigo_aviso)

        return {
            "codigo_aviso": codigo_aviso,
            "cantidad_seguimientos": len(seguimientos),
            "seguimientos": seguimientos
        }