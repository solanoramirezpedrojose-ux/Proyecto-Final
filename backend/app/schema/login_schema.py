from pydantic import BaseModel, ConfigDict

class LoginSchema(BaseModel):
    correo:str
    contrasena:str

    model_config = ConfigDict(from_attributes=True)
    