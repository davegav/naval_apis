#from datetime import datetime
from pydantic import BaseModel
import random

class PartidaInDB(BaseModel):
    id_partida: int = 0
    nombre: str
    tableroenemigo: str = "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    tableropropio: str = "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    turnopropio: bool = random.choice([True, False])
    fin: bool = False

database_partidas = []
generator = {"id":0}
def save_partida(partida_in_db: PartidaInDB):
    generator["id"] = generator["id"] + 1 # desaparece con el autoincrement del SQL
    partida_in_db.id_partida = generator["id"]
    database_partidas.append(partida_in_db)
    return partida_in_db

def update_partida(partida_in_db: PartidaInDB):
    database_partidas[partida_in_db.id] = partida_in_db
    return partida_in_db

# Tablero 12x12 
# 4 tipos de barcos
#     (1) Portaaviones = 5
#     (2) buque = 4
#     (3) submarino = 3
#     (4) galeon = 3
#     (5) pesquero = 2
# tablero_mio = "0000000000000"
# tablero_enemigo =

# Conversiones
#     (0) Mar
#     (1) Portaaviones
#     (2) buque
#     (3) submarino
#     (4) galeon
#     (5) pesquero
#     (6) Ataque perdido
#     (7) Golpe


# 000000000010
# 000000000070
# 000000000610
# 000000000010
# 000000000010

# 000000000010000000000070000000000610000000000010000000000010