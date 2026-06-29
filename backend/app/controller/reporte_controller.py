from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from app.service.reporte_service import ReporteService
router = APIRouter(prefix="/api/reports", tags=["Reports"])
service = ReporteService()

@router.get("/general-statistics")
def get_general_statistics():
    try:
        return service.obtener_estadisticas_generales()
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@router.get("/notices-by-type")
def get_notices_by_type():
    try:
        return service.contar_avisos_por_tipo()
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.get("/follow-ups-by-notice/{codigo_aviso}")
def get_follow_ups_by_notice(codigo_aviso: str):
    try:
        reporte = service.obtener_reporte_seguimientos_por_aviso(codigo_aviso)
        return jsonable_encoder(reporte)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))