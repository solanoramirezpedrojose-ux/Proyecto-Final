from fastapi import APIRouter, HTTPException
from app.schema.usuario_schema import UsuarioSchema, UsuarioResponseSchema
from app.service.usuario_service import UsuarioService

router = APIRouter(prefix="/api/users", tags=["Users"])
service = UsuarioService()

@router.post("/add", response_model=UsuarioResponseSchema)
def register_user(usuario: UsuarioSchema):
    try:
        return service.registrar_usuario(
            usuario.cedula,
            usuario.nombre,
            usuario.correo,
            usuario.contrasena,
            usuario.rol
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

@router.get("/list", response_model=list[UsuarioResponseSchema])
def list_users():
    return service.obtener_todos_los_usuarios()

@router.get("/search/{cedula}", response_model=UsuarioResponseSchema)
def search_user(cedula: str):
    try:
        return service.buscar_usuario_por_cedula(cedula)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))

@router.put("/update/{cedula}", response_model=UsuarioResponseSchema)
def update_user(cedula: str, usuario: UsuarioSchema):
    try:
        return service.actualizar_usuario(
            cedula,
            usuario.nombre,
            usuario.correo,
            usuario.contrasena,
            usuario.rol
        )
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))

@router.delete("/delete/{cedula}")
def delete_user(cedula: str):
    try:
        return service.eliminar_usuario(cedula)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))