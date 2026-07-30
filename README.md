# LLM Red Team Lab: Prompt Injection & Output Sanitization

Este laboratorio demuestra la ejecución de ataques de inyección de prompts (Prompt Injection y System Override) contra un modelo de lenguaje integrado en una API, y la implementación de contramedidas en el backend para mitigar el impacto en el cliente.

## Arquitectura

*   **Backend:** FastAPI (Python).
*   **LLM Provider:** Groq Cloud API (Llama-3-8b-8192).
*   **Red Teaming Script:** Script personalizado en Python usando `httpx` para enviar vectores de ataque automatizados.
*   **Defensa:** Middleware de salida que implementa sanitización HTML (`bleach`), normalización Unicode y neutralización de enlaces (defanging).

## Estructura del Proyecto

*   `app/main.py`: Código fuente del servidor FastAPI con la lógica de integración y las capas de sanitización de salida.
*   `red_team_test.py`: Script de auditoría con payloads maliciosos predefinidos para evaluar la resistencia del LLM.
*   `requirements.txt`: Dependencias del entorno.

## Configuración y Ejecución

1. Clonar el repositorio e instalar dependencias:
   ```bash
   pip install -r requirements.txt