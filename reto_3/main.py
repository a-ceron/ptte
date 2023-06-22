"""
Prueba técnica.

Reto 3.
Construcción de un API para obtener
un archivo CSV o su contenido en formato
JSON.


desarrollador: aceron
"""

from typing import Annotated
from pydantic import BaseModel, Field

from fastapi import Body
from fastapi import FastAPI

from objetos import consts
from objetos import dataManager as dm
from objetos import functionsManager as fm


app = FastAPI()


@app.get("/api/v1", response_model=dm.DevData)
async def get_personal_data():
    return dm.DevData(
        name="Ariel Ceron",
        age=26,
        grade="M.Sc Science Computing",
        skills=['Python', 'FastAPI', 'pyTorch'],
        experience_years=8
    )


@app.get("/api/v1/ejercicio/descarga/")
async def descargar_ejercicio(formato: str):
    return fm.pipeline(consts.DATA_PATH, formato)


@app.post("/api/v1/ejercicio/descarga/")
async def descargar_ejercicio_with_body(body:dm.Vacaciones):
    return fm.pipeline(consts.DATA_PATH, body.formato)