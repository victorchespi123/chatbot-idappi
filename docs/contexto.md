# Contexto del Proyecto — Chatbot idappi

## Objetivo Global
Chatbot con IA para la plataforma educativa **idappi.com** (EdTech desde Paraguay) que permite a los alumnos preguntar sobre cualquier tema del curso y recibir el link directo al contenido correspondiente.

## Proyecto Piloto
- **Curso**: QUÍMICA – UCV (93 estudiantes inscritos)
- **Plataforma LMS**: LearnDash sobre WordPress
- **Contenido**: 17 lecciones, 70 temas, 9 cuestionarios (87 pasos totales)
- **Público**: Estudiantes de secundaria, preingreso a Medicina, autodidactas
- **URL del curso**: https://idappi.com/courses/quimica/

## Cómo Funciona
1. El alumno escribe una pregunta en lenguaje natural (ej: "¿dónde veo lo de molaridad?")
2. Claude AI interpreta la pregunta y busca en la base de datos del curso
3. Responde con el nombre del tema, link directo a idappi.com y breve descripción
4. Se registra la interacción en Google Sheets para analytics

## URLs del Proyecto
- **App en producción**: https://3aumyb4fsk33dnabmhqnjy.streamlit.app
- **Repo GitHub**: https://github.com/victorchespi123/chatbot-idappi (público)
- **Google Sheet tracking**: https://docs.google.com/spreadsheets/d/1FMy-gOlDEBSErZrk4AAlPiEQWgFzl8bbYcoipSaA1f4
- **Google Cloud Project**: chatbot-idappi (ID: smooth-reason-500712-r0)

## Stack Tecnológico
- **Frontend**: Streamlit (Python) con CSS custom (tema oscuro, paleta idappi)
- **IA**: Claude API (Anthropic) — modelo claude-sonnet-4-6
- **Base de datos del curso**: Excel (`quimica_ucv_base_datos.xlsx`) con 96 registros
- **Tracking**: Google Sheets API via cuenta de servicio
- **Deploy**: Streamlit Community Cloud (conectado a GitHub)
- **Plataforma destino**: idappi.com (WordPress + LearnDash)

## Estructura de Archivos
```
chatbot idappi/
├── app_chatbot.py              # Web app principal (Streamlit)
├── chatbot_quimica.py          # Versión terminal (CLI)
├── quimica_ucv_base_datos.xlsx # Base de datos del curso (96 registros)
├── requirements.txt            # Dependencias Python
├── google_credentials.json     # Credenciales Google (NO en GitHub)
├── .env                        # API keys (NO en GitHub)
├── .gitignore                  # Protege archivos sensibles
└── docs/                       # Documentación del proyecto
    ├── contexto.md
    ├── roadmap.md
    ├── tareas.md
    └── sesiones.md
```

## Base de Datos del Curso
Cada registro tiene:
| Campo | Descripción |
|-------|-------------|
| ID | Número secuencial |
| Tipo | Lección / Tema / Cuestionario |
| Lección | Nombre de la lección padre |
| Tema/Subtema | Nombre del tema específico |
| Nombre Completo | Ruta jerárquica (Lección > Tema) |
| URL | Link directo en idappi.com |
| Palabras Clave | Keywords para matching de la IA |
| Descripción para IA | Texto descriptivo del contenido |

## Tracking de Interacciones
Cada pregunta de un alumno registra en Google Sheets:
- Fecha y hora
- Pregunta del alumno
- Respuesta del chatbot (primeros 500 chars)
- Temas detectados
- URLs devueltas
- Session ID (para agrupar preguntas de una misma sesión)

## Precisión Estimada
- **Actual**: ~70-75% (keywords inferidas por nombre de tema, no por contenido real)
- **Objetivo**: ~95% (requiere entrar a cada tema y documentar contenido real)

## Relación con Otros Proyectos
- **meticas instagram/**: Proyecto separado de análisis de métricas de Instagram/YouTube/TikTok para @vicbenitezpro
- Este chatbot es independiente con su propio repositorio GitHub
