from pydantic import BaseModel, ConfigDict

class AvisoSchema(BaseModel):
    codigo:str
    cedula_usuario:str
    tipo_dano:str
    descripcion:str
    descripcion:str
    ubicacion:str
    fecha:str
    estado:str = "Pendiente"

    model_config = ConfigDict(from_attributes=True)