from datetime import date
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum,auto
import random

app = FastAPI()

class PosicionFutbol(Enum):
    PORTERO= auto()
    DEFENSA = auto()
    MEDIOCAMPISTA = auto()
    DELANTERO = auto()
    EXTREMO = auto()

class jugador(BaseModel):
    id: int
    name: str 
    dorsal: int
    nacimiento: date
    altura: float  
    posicion: PosicionFutbol
    equipo: str

# ARGENTINA
p1 = jugador(id=1, name="Messi", dorsal=10, nacimiento="1987-06-24", altura=1.70, posicion=PosicionFutbol.DELANTERO, equipo="Argentina")
p2 = jugador(id=2, name="Di Maria", dorsal=11, nacimiento="1988-02-14", altura=1.78, posicion=PosicionFutbol.EXTREMO, equipo="Argentina")

# PORTUGAL
p3 = jugador(id=3, name="Cristiano", dorsal=7, nacimiento="1985-02-05", altura=1.87, posicion=PosicionFutbol.DEFENSA, equipo="Portugal")
p4 = jugador(id=4, name="Bernardo Silva", dorsal=10, nacimiento="1994-08-10", altura=1.73, posicion=PosicionFutbol.MEDIOCAMPISTA, equipo="Portugal")

# COLOMBIA
p5 = jugador(id=5, name="James", dorsal=10, nacimiento="1991-07-12", altura=1.80, posicion=PosicionFutbol.MEDIOCAMPISTA, equipo="Colombia")
p6 = jugador(id=6, name="Luis Diaz", dorsal=7, nacimiento="1997-01-13", altura=1.78, posicion=PosicionFutbol.PORTERO, equipo="Colombia")

lista_jugador: list[jugador] = [p1,p2,p3,p4,p5,p6]

@app.get("/show_alljugadores/")
def all_jugadores():
    return lista_jugador


# ✅ show_one_player — busca por id con for, igual que tu pokemon
def buscar_jugador(id: int):
    for jugador in lista_jugador:
        if jugador.id == id:
            return jugador
    return None

@app.get("/show_onejugador/{id}")
def show_one_player(id: int):
    jugador = buscar_jugador(id)
    if not jugador:
        return {"mensaje": "jugador no encontrado"}
    return jugador

# ✅ compare_two_players — compara altura igual que pokemon compara attack
@app.get("/compare_jugadores/")
def compare_two_players(id_1: int, id_2: int):
    jugador_1 = buscar_jugador(id_1)
    jugador_2 = buscar_jugador(id_2)

    if not jugador_1 and not jugador_2:
        return {"mensaje": "ambos jugadores no encontrados"}
    
    if not jugador_1:
        return {"mensaje": "jugador 1 no encontrado"}

    if not jugador_2:
        return {"mensaje": "jugador 2 no encontrado"}
    
    if jugador_1.altura > jugador_2.altura:
        mas_alto = jugador_1.name
    elif jugador_2.altura > jugador_1.altura:
        mas_alto = jugador_2.name
    else:
        mas_alto = "ambos tienen la misma altura"

    return {
        "jugador_1": jugador_1.name,
        "jugador_2": jugador_2.name,
        "mas_alto": mas_alto
    }

# ✅ show_equipo — filtra por equipo con for, igual que pokemon filtra por tipo
@app.get("/show_equipo/")
def show_equipo(equipo: str):
    jugadores_equipo = []
    for jugador in lista_jugador:
        if jugador.equipo.lower() == equipo.lower():
            jugadores_equipo.append(jugador)

    if not jugadores_equipo:
        return {"mensaje": f"no se encontraron jugadores del equipo {equipo}"}

    return jugadores_equipo