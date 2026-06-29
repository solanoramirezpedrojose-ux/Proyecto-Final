from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder

from app.schema.aviso_schema import AvisoSchema
from app.service.reporte_service import ReporteService

router = APIRouter(prefix="/api/reports", tags=["Reports"])
service = ReporteService()

@router.get("/general-statistics")
def get_general_statistics():
    return service.obtener_estadisticas_generales()

@router.get("/notices-by-type")
def get_notices_by_type():
    return service.contar_avisos_por_tipo()

@router.get("/pending-notices", response_model=list[AvisoSchema])
def get_pending_notices():
    return service.obtener_avisos_pendientes()

@router.get("/in-progress-notices", response_model=list[AvisoSchema])
def get_in_progress_notices():
    return service.obtener_avisos_en_proceso()

@router.get("/resolved-notices", response_model=list[AvisoSchema])
def get_resolved_notices():
    return service.obtener_avisos_resueltos()

@router.get("/follow-ups-by-notice/{codigo_aviso}")
def get_follow_ups_by_notice(codigo_aviso: str):
    try:
        reporte = service.obtener_reporte_seguimientos_por_aviso(codigo_aviso)
        return jsonable_encoder(reporte)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))