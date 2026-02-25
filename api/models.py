from pydantic import BaseModel


class Medico(BaseModel):
    id: int
    nombre: str
    especialidad: str
    dias: list[str]


class SlotHorario(BaseModel):
    hora: str
    disponible: bool


class DisponibilidadResponse(BaseModel):
    medico: str
    fecha: str
    slots: list[SlotHorario]


class ErrorResponse(BaseModel):
    detail: str
