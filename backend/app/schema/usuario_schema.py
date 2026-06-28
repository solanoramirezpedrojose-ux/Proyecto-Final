from pydantic import BaseModel, ConfigDict

class UsuarioSchema(BaseModel):
    cedula:str
    nombre:str
    correo:str
    contrasena:str
    rol:str

    model_config = ConfigDict(from_attributes=True)

class UsuarioResponseSchema(BaseModel):
    cedula:str
    nombre:str
    correo:str
    rol:str

    model_config = ConfigDict(from_attributes=True)