from app.config.data_base import SessionLocal
from app.entity.aviso import AvisoORM
from app.entity.seguimiento import SeguimientoORM


class ReporteService:

    def obtener_estadisticas_generales(self):
        db = SessionLocal()

        try:
            avisos = db.query(AvisoORM).all()

            total = 0
            pendientes = 0
            en_proceso = 0
            resueltos = 0

            for aviso in avisos:
                total += 1

                if aviso.estado == "Pendiente":
                    pendientes += 1

                if aviso.estado == "En proceso":
                    en_proceso += 1

                if aviso.estado == "Resuelto":
                    resueltos += 1

            return {
                "total": total,
                "pendientes": pendientes,
                "en_proceso": en_proceso,
                "resueltos": resueltos
            }

        finally:
            db.close()

    def contar_avisos_por_tipo(self):
        db = SessionLocal()

        try:
            avisos = db.query(AvisoORM).all()
            conteo = {}

            for aviso in avisos:
                tipo = aviso.tipo_dano

                if tipo not in conteo:
                    conteo[tipo] = 0

                conteo[tipo] += 1

            return conteo

        finally:
            db.close()

    def obtener_reporte_seguimientos_por_aviso(self, codigo_aviso):
        db = SessionLocal()

        try:
            seguimientos = db.query(SeguimientoORM).filter_by(
                codigo_aviso=codigo_aviso
            ).all()

            lista = []

            for seguimiento in seguimientos:
                lista.append({
                    "codigo_seguimiento": seguimiento.codigo_seguimiento,
                    "codigo_aviso": seguimiento.codigo_aviso,
                    "estado": seguimiento.estado,
                    "observacion": seguimiento.observacion,
                    "fecha_actualizacion": seguimiento.fecha_actualizacion,
                    "responsable": seguimiento.responsable
                })

            return {
                "codigo_aviso": codigo_aviso,
                "cantidad_seguimientos": len(lista),
                "seguimientos": lista
            }

        finally:
            db.close()