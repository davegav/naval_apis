from typing import Dict
from pydantic import BaseModel

class usuarioInDB(BaseModel):
    nombre: str   # usuarioInDB.nombre = "diego"
    mejorpuntaje: int
    ultimopuntaje: int

database_usuarios = Dict[str, usuarioInDB] # {"nombre": "diego", }
database_usuarios = {"Diego": usuarioInDB(**{"nombre":"Diego",
                "mejorpuntaje":1000,
                "ultimopuntaje":10}),
                "Felix": usuarioInDB(**{"nombre":"Felix",
                "mejorpuntaje":30,
                "ultimopuntaje":30})}
def get_usuario(nombre: str):
    if nombre in database_usuarios.keys():
        return database_usuarios[nombre]
    else:
        return None
def update_usuario(usuario_in_db: usuarioInDB):
    database_usuarios[usuario_in_db.nombre] = usuario_in_db
    return usuario_in_db