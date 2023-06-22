"""
Estructura de datos para el manejo del body
"""
from pydantic import BaseModel


class Vacaciones(BaseModel):
    formato: str


class DevData(BaseModel):
    name: str
    age: int
    grade: str
    skills: list 
    experience_years: int
