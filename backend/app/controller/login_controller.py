from fastapi import APIRouter, HTTPException
from app.schema.login_schema import LoginSchema
from app.service.auth_service import AuthService

router = APIRouter(prefix="/api/auth", tags=["Auth"])
service = AuthService()

@router.post("/login")
def login(login_data: LoginSchema):
    try:
        usuario = service.login(
            login_data.correo,
            login_data.contrasena
        )
        token = f"TOKEN-{usuario.cedula}-{usuario.rol}"
        return {
            "message": "Login successful",
            "token": token,
            "user": {
                "cedula": usuario.cedula,
                "nombre": usuario.nombre,
                "correo": usuario.correo,
                "rol": usuario.rol
            }
        }
    except ValueError as error:
        raise HTTPException(status_code=401, detail=str(error))