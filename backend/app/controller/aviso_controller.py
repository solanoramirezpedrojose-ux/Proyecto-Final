from fastapi import APIRouter, HTTPException
from app.schema.aviso_schema import AvisoSchema
from app.service.aviso_service import AvisoService

router = APIRouter(prefix="/api/notices", tags=["Notices"])
service = AvisoService()

@router.post("/add", response_model=AvisoSchema)
def add_notice(aviso: AvisoSchema):
    try:
        return service.registrar_aviso(
            aviso.codigo,
            aviso.cedula_usuario,
            aviso.tipo_dano,
            aviso.descripcion,
            aviso.ubicacion,
            aviso.fecha,
            aviso.estado
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

@router.get("/list", response_model=list[AvisoSchema])
def list_notices():
    return service.obtener_todos_los_avisos()

@router.get("/search/{codigo}", response_model=AvisoSchema)
def search_notice(codigo: str):
    try:
        return service.buscar_aviso_por_codigo(codigo)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))

@router.get("/search-by-user/{cedula_usuario}", response_model=list[AvisoSchema])
def search_notices_by_user(cedula_usuario: str):
    return service.obtener_avisos_por_usuario(cedula_usuario)

@router.get("/search-by-status/{estado}", response_model=list[AvisoSchema])
def search_notices_by_status(estado: str):
    return service.obtener_avisos_por_estado(estado)

@router.get("/search-by-type/{tipo_dano}", response_model=list[AvisoSchema])
def search_notices_by_type(tipo_dano: str):
    return service.obtener_avisos_por_tipo_dano(tipo_dano)

@router.put("/update/{codigo}", response_model=AvisoSchema)
def update_notice(codigo: str, aviso: AvisoSchema):
    try:
        return service.actualizar_aviso(
            codigo,
            aviso.cedula_usuario,
            aviso.tipo_dano,
            aviso.descripcion,
            aviso.ubicacion,
            aviso.fecha,
            aviso.estado
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

@router.delete("/delete/{codigo}")
def delete_notice(codigo: str):
    try:
        return service.eliminar_aviso(codigo)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))