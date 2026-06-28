# Contexto del Proyecto — Chatbot idappi

## Objetivo Global
Chatbot con IA para la plataforma educativa **idappi.com** que permite a los alumnos preguntar sobre cualquier tema de sus cursos y recibir:
- El link directo al contenido en idappi.com
- El minuto exacto del video donde se explica el subtema
- Sugerencias de temas relacionados

## Plataforma
- **Sitio web**: idappi.com (WordPress + LearnDash LMS)
- **Empresa**: Idappi — EdTech desde Paraguay (CEO: Victor Benitez)
- **Videos**: Alojados en Vimeo con subtítulos automáticos (IA)
- **Pagos**: Pagopar (pasarela paraguaya)

## Cursos Integrados

### Química UCV
- **Estudiantes**: 93 inscritos
- **Contenido**: 17 lecciones, 70 temas, 9 cuestionarios (87 pasos)
- **Videos**: 66 con timestamps (465 subtemas mapeados)
- **Público**: Estudiantes de secundaria, preingreso a Medicina, autodidactas
- **URL**: https://idappi.com/courses/quimica/

### Biología UCV
- **Estudiantes**: 92 inscritos
- **Contenido**: 11 lecciones, 30 temas, 1 cuestionario (42 pasos)
- **Videos**: 9 con timestamps (52 subtemas), 21 pendientes (Vimeo procesando)
- **Público**: Estudiantes de secundaria, preingreso a Medicina
- **URL**: https://idappi.com/courses/fundamentos-de-biologia-general/

## URLs del Proyecto
- **App en producción**: https://3aumyb4fsk33dnabmhqnjy.streamlit.app
- **Repo GitHub**: https://github.com/victorchespi123/chatbot-idappi (público)
- **Google Sheet tracking**: https://docs.google.com/spreadsheets/d/1FMy-gOlDEBSErZrk4AAlPiEQWgFzl8bbYcoipSaA1f4
- **Google Cloud Project**: chatbot-idappi (ID: smooth-reason-500712-r0)

## Stack Tecnológico
- **Frontend**: Streamlit (Python) con CSS custom (tema oscuro, paleta idappi)
- **IA**: Claude API (Anthropic) — modelo claude-sonnet-4-6
- **Base de datos cursos**: Excel (`quimica_ucv_base_datos.xlsx`) — 137 registros (96 Química + 41 Biología)
- **Timestamps**: JSON (`video_timestamps.json`) — 75 videos con subtemas mapeados
- **Transcripciones**: Vimeo (subtítulos automáticos AI) descargadas via API
- **Tracking**: Google Sheets API via cuenta de servicio
- **Deploy**: Streamlit Community Cloud (auto-deploy desde GitHub)

## Estructura de Archivos
```
chatbot idappi/
├── app_chatbot.py              # Web app principal (Streamlit)
├── chatbot_quimica.py          # Versión terminal (CLI, legacy)
├── quimica_ucv_base_datos.xlsx # Base de datos de cursos (Química + Biología)
├── video_timestamps.json       # Timestamps de 75 videos (subtemas + minutos)
├── vimeo_transcripts.json      # Transcripciones Química (66 videos)
├── bio_transcripts.json        # Transcripciones Biología (10 videos)
├── requirements.txt            # Dependencias Python
├── google_credentials.json     # Credenciales Google (NO en GitHub)
├── .env                        # API keys (NO en GitHub)
├── .gitignore                  # Protege archivos sensibles
└── docs/                       # Documentación del proyecto
```

## Flujo de Funcionamiento
1. Alumno entra al chatbot (link público o embebido en idappi.com)
2. Escribe una pregunta en lenguaje natural
3. Claude AI busca en la base de datos (137 registros + 517 subtemas con timestamps)
4. Responde con: curso, tema, link directo, minuto del video
5. La interacción se registra en Google Sheets (tracking)

## Precisión
- **Química UCV**: ~98% (contenido verificado + 465 timestamps de video)
- **Biología UCV**: ~80% (contenido verificado, timestamps parciales — 21 videos pendientes)
