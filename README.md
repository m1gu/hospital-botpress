# 🏥 Hospital Digital Salud — Bot de Agendamiento

## URL del Bot
[Abrir Chat](https://cdn.botpress.cloud/webchat/v3.6/shareable.html?configUrl=https://files.bpcontent.cloud/2026/02/24/22/20260224221346-T6VAJ2PT.json)

## Descripción
Bot conversacional desarrollado en Botpress para el Hospital Digital Salud,
especializado en agendar citas médicas con integración de 2 APIs reales.

## Especialidades Disponibles
- Cardiología
- Pediatría
- Dermatología

## Arquitectura de APIs

### API 1 — Disponibilidad (FastAPI + Docker)
- **URL Base**: *(Pendiente deploy en Azure Container Apps)*
- **Hosting**: Azure Container Apps (Docker)
- **Tecnología**: Python + FastAPI
- **Endpoints**:
  | Método | Endpoint | Descripción |
  |--------|----------|-------------|
  | GET | /especialidades | Lista de especialidades |
  | GET | /medicos?especialidad=X | Médicos por especialidad |
  | GET | /disponibilidad?medico=X&fecha=Y | Horarios disponibles |
  | GET | /fechas-disponibles?medico=X | Próximas fechas disponibles |
  | GET | /health | Estado del servicio |

### API 2 — Registro de Citas (Sheety → Google Sheets)
- **URL Base**: `https://api.sheety.co/b57b0a5e18a9a06aabe0530240e45e36/hospitalDigitalSaludCitas/citas`
- **Método**: POST
- **Autenticación**: Bearer Token
- **Campos**: nombre, cedula, telefono, especialidad, medico, fecha, hora, estado

## Master Prompt
*(Se incluirá en Fase 4)*

## Video Demo
*(Pendiente)*

## Cómo Probar
1. Abrir la URL del bot
2. Escribir "Hola, quiero agendar una cita"
3. Seguir las instrucciones del asistente
4. Al finalizar, verificar la cita en la Google Sheet

## Tecnologías Utilizadas
- Botpress Cloud (Bot conversacional)
- Python + FastAPI (API de disponibilidad)
- Docker + Azure Container Apps (Hosting de la API)
- Azure Container Registry (Registro de imagen Docker)
- Sheety.co + Google Sheets (Registro de citas)
