from fastapi import APIRouter, HTTPException
from app.schema.seguimiento_schema import SeguimientoSchema
from app.service.seguimiento_service import SeguimientoService

router = APIRouter(prefix="/api/follow-ups", tags=["Follow-ups"])
service = SeguimientoService()

@router.post("/add", response_model=SeguimientoSchema)
def register_follow_up(seguimiento: SeguimientoSchema):
    try:
        return service.registrar_seguimiento(
            seguimiento.codigo_seguimiento,
            seguimiento.codigo_aviso,
            seguimiento.estado,
            seguimiento.observacion,
            seguimiento.fecha_actualizacion,
            seguimiento.responsable
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

@router.get("/list", response_model=list[SeguimientoSchema])
def list_follow_ups():
    return service.obtener_todos_los_seguimientos()

@router.get("/search/{codigo_seguimiento}", response_model=SeguimientoSchema)
def search_follow_up(codigo_seguimiento: str):
    try:
        return service.buscar_seguimiento_por_codigo(codigo_seguimiento)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))

@router.get("/search-by-notice/{codigo_aviso}", response_model=list[SeguimientoSchema])
def search_follow_ups_by_notice(codigo_aviso: str):
    try:
        return service.obtener_seguimientos_por_aviso(codigo_aviso)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))

@router.put("/update/{codigo_seguimiento}", response_model=SeguimientoSchema)
def update_follow_up(codigo_seguimiento: str, seguimiento: SeguimientoSchema):
    try:
        return service.actualizar_seguimiento(
            codigo_seguimiento,
            seguimiento.codigo_aviso,
            seguimiento.estado,
            seguimiento.observacion,
            seguimiento.fecha_actualizacion,
            seguimiento.responsable
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

@router.delete("/delete/{codigo_seguimiento}")
def delete_follow_up(codigo_seguimiento: str):
    try:
        return service.eliminar_seguimiento(codigo_seguimiento)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))