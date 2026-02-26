from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta

from data import (
    HOSPITAL, ESPECIALIDADES, MEDICOS,
    HORARIOS_BASE, CITAS_OCUPADAS
)
from models import Medico, SlotHorario, DisponibilidadResponse

app = FastAPI(
    title="Hospital Digital — API de Disponibilidad",
    description="API para consultar especialidades, médicos y horarios disponibles.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DIAS_SEMANA = {
    0: "lunes", 1: "martes", 2: "miércoles",
    3: "jueves", 4: "viernes", 5: "sábado", 6: "domingo"
}


@app.get("/health")
def health():
    return {"status": "ok", "hospital": HOSPITAL["nombre"]}


@app.get("/especialidades", response_model=list[str])
def get_especialidades():
    """Retorna la lista de especialidades disponibles."""
    return ESPECIALIDADES


@app.get("/medicos", response_model=list[Medico])
def get_medicos(especialidad: str = Query(..., description="Nombre de la especialidad")):
    """Retorna los médicos de una especialidad específica."""
    especialidad_lower = especialidad.lower()
    resultado = [m for m in MEDICOS if m["especialidad"].lower() == especialidad_lower]
    if not resultado:
        raise HTTPException(
            status_code=404,
            detail=f"No se encontraron médicos para la especialidad '{especialidad}'"
        )
    return resultado


@app.get("/disponibilidad", response_model=DisponibilidadResponse)
def get_disponibilidad(
    medico: str = Query(..., description="Nombre del médico, e.g. 'Dr. García'"),
    fecha: str = Query(..., description="Fecha en formato YYYY-MM-DD")
):
    """
    Retorna los slots de horario para un médico en una fecha específica.
    Valida que:
    - El médico exista
    - La fecha sea de lunes a viernes
    - El médico atienda ese día de la semana
    """
    # Validar que el médico exista
    medico_data = None
    for m in MEDICOS:
        if m["nombre"].lower() == medico.lower():
            medico_data = m
            break

    if not medico_data:
        raise HTTPException(status_code=404, detail=f"Médico '{medico}' no encontrado")

    # Validar formato de fecha
    try:
        fecha_obj = datetime.strptime(fecha, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Formato de fecha inválido. Use YYYY-MM-DD")

    # Validar que sea día laborable (lunes a viernes)
    dia_semana = DIAS_SEMANA.get(fecha_obj.weekday())
    if fecha_obj.weekday() >= 5:
        raise HTTPException(
            status_code=400,
            detail="El hospital solo atiende de lunes a viernes"
        )

    # Validar que el médico atienda ese día
    if dia_semana not in medico_data["dias"]:
        raise HTTPException(
            status_code=400,
            detail=f"{medico_data['nombre']} no atiende los {dia_semana}. "
                   f"Días disponibles: {', '.join(medico_data['dias'])}"
        )

    # Obtener slots ocupados
    ocupados = CITAS_OCUPADAS.get(medico_data["nombre"], {}).get(fecha, [])

    # Construir respuesta con slots
    slots = [
        SlotHorario(hora=h, disponible=(h not in ocupados))
        for h in HORARIOS_BASE
    ]

    return DisponibilidadResponse(
        medico=medico_data["nombre"],
        fecha=fecha,
        slots=slots
    )


@app.get("/fechas-disponibles")
def get_fechas_disponibles(
    medico: str = Query(..., description="Nombre del médico"),
    dias: int = Query(5, description="Cantidad de días a buscar hacia adelante")
):
    """
    Retorna las próximas fechas disponibles para un médico
    (útil para que el bot sugiera fechas).
    """
    medico_data = None
    for m in MEDICOS:
        if m["nombre"].lower() == medico.lower():
            medico_data = m
            break

    if not medico_data:
        raise HTTPException(status_code=404, detail=f"Médico '{medico}' no encontrado")

    fechas = []
    hoy = datetime.now()
    for i in range(1, 30):  # Buscar en los próximos 30 días
        fecha = hoy + timedelta(days=i)
        dia_semana = DIAS_SEMANA.get(fecha.weekday())
        if dia_semana in medico_data["dias"]:
            fechas.append({
                "fecha": fecha.strftime("%Y-%m-%d"),
                "dia": dia_semana
            })
            if len(fechas) >= dias:
                break

    return {"medico": medico_data["nombre"], "fechas_disponibles": fechas}
