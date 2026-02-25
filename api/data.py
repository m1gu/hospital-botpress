"""
Datos ficticios del Hospital Digital Salud.
Horarios: Lunes a Viernes 8:00-18:00
Duración citas: 30 minutos
"""

HOSPITAL = {
    "nombre": "Hospital Digital Salud",
    "horario": "Lunes a Viernes 8:00 - 18:00",
    "duracion_cita_minutos": 30,
}

ESPECIALIDADES = ["Cardiología", "Pediatría", "Dermatología"]

# Cada médico tiene días asignados y horarios
MEDICOS = [
    {
        "id": 1,
        "nombre": "Dr. García",
        "especialidad": "Cardiología",
        "dias": ["lunes", "miércoles", "viernes"],
    },
    {
        "id": 2,
        "nombre": "Dra. López",
        "especialidad": "Cardiología",
        "dias": ["martes", "jueves"],
    },
    {
        "id": 3,
        "nombre": "Dr. Martínez",
        "especialidad": "Pediatría",
        "dias": ["lunes", "martes", "miércoles"],
    },
    {
        "id": 4,
        "nombre": "Dra. Rodríguez",
        "especialidad": "Pediatría",
        "dias": ["jueves", "viernes"],
    },
    {
        "id": 5,
        "nombre": "Dr. Sánchez",
        "especialidad": "Dermatología",
        "dias": ["lunes", "miércoles", "viernes"],
    },
    {
        "id": 6,
        "nombre": "Dra. Torres",
        "especialidad": "Dermatología",
        "dias": ["martes", "jueves"],
    },
]

# Slots horarios disponibles (cada 30 min de 8:00 a 18:00)
HORARIOS_BASE = [
    "08:00", "08:30", "09:00", "09:30", "10:00", "10:30",
    "11:00", "11:30", "12:00", "12:30", "13:00", "13:30",
    "14:00", "14:30", "15:00", "15:30", "16:00", "16:30",
    "17:00", "17:30",
]

# Citas ya agendadas (simuladas) — para que no todo aparezca disponible
CITAS_OCUPADAS = {
    "Dr. García": {
        "2026-02-25": ["09:00", "10:00", "14:00"],
        "2026-02-26": ["08:00", "11:00"],
        "2026-02-27": ["10:00", "15:00", "16:00"],
    },
    "Dra. López": {
        "2026-02-25": ["09:30", "10:30"],
        "2026-02-26": ["08:30", "14:30"],
    },
    "Dr. Martínez": {
        "2026-02-25": ["08:00", "09:00", "10:00"],
        "2026-02-26": ["11:00", "14:00"],
    },
    "Dra. Rodríguez": {
        "2026-02-26": ["09:00", "13:00"],
        "2026-02-27": ["10:00", "11:00", "15:00"],
    },
    "Dr. Sánchez": {
        "2026-02-25": ["08:00", "12:00"],
        "2026-02-27": ["09:00", "10:00"],
    },
    "Dra. Torres": {
        "2026-02-25": ["10:00", "14:00", "16:00"],
        "2026-02-26": ["08:00", "09:00"],
    },
}
