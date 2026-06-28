from pydantic import BaseModel, ConfigDict

class SeguimientoSchema(BaseModel):
    codigo_seguimiento:str
    codigo_aviso:str
    estado:str
    observacion:str
    fecha_actualizacion:str
    responsable:str

    model_config = ConfigDict(from_attributes=True)
