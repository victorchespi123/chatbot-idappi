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
- **Base de datos**: 96 registros con keywords enriquecidas + contenido verificado
- **Videos**: 66 con timestamps (465 subtemas mapeados)
- **Precisión**: ~98%
- **URL**: https://idappi.com/courses/quimica/
- **WordPress Post ID**: 2240

### Biología UCV
- **Estudiantes**: 92 inscritos
- **Contenido**: 11 lecciones, 30 temas, 1 cuestionario (42 pasos)
- **Base de datos**: 41 registros con keywords enriquecidas + contenido verificado
- **Videos**: 9 con timestamps (52 subtemas), ~21 pendientes (Vimeo IDs obsoletos — ver videos_pendientes.md)
- **Precisión**: ~90%
- **URL**: https://idappi.com/courses/fundamentos-de-biologia-general/
- **WordPress Post ID**: 7187

### Física UCV
- **Estudiantes**: N/D (curso gratuito)
- **Contenido**: 8 lecciones, 49 temas (58 pasos)
- **Base de datos**: 57 registros con keywords del contenido real
- **Videos**: 15 con timestamps (102 subtemas), ~34 pendientes (algunos Vimeo IDs obsoletos)
- **Precisión**: ~90%
- **URL**: https://idappi.com/courses/fisicaidappi/
- **WordPress Post ID**: 2232

## URLs del Proyecto
- **App en producción**: https://3aumyb4fsk33dnabmhqnjy.streamlit.app
- **Repo GitHub**: https://github.com/victorchespi123/chatbot-idappi (público)
- **Google Sheet tracking**: https://docs.google.com/spreadsheets/d/1FMy-gOlDEBSErZrk4AAlPiEQWgFzl8bbYcoipSaA1f4
- **Google Cloud Project**: chatbot-idappi (ID: smooth-reason-500712-r0)

## Stack Tecnológico
- **Frontend**: Streamlit (Python) con CSS custom (tema oscuro, paleta idappi)
- **IA**: Claude API (Anthropic) — modelo claude-sonnet-4-6
- **Base de datos cursos**: Excel (`quimica_ucv_base_datos.xlsx`) — 194 registros en 3 hojas
- **Timestamps**: JSON (`video_timestamps.json`) — 90 videos, 619 subtemas mapeados
- **Transcripciones**: Vimeo (subtítulos automáticos AI) descargadas via JWT del browser
- **Tracking**: Google Sheets API via cuenta de servicio
- **Deploy**: Streamlit Community Cloud (auto-deploy desde GitHub)

## Estructura de Archivos
```
chatbot idappi/
├── app_chatbot.py              # Web app principal (Streamlit)
├── chatbot_quimica.py          # Versión terminal (CLI, legacy)
├── quimica_ucv_base_datos.xlsx # Base de datos de cursos (3 hojas: Química + Biología + Física)
├── video_timestamps.json       # Timestamps de 90 videos (619 subtemas con minutos)
├── vimeo_transcripts.json      # Transcripciones Química (66 videos)
├── bio_transcripts.json        # Transcripciones Biología (10 videos)
├── fis_transcripts.json        # Transcripciones Física (15 videos)
├── auto_generated_captions.vtt # Ejemplo de VTT descargado manualmente
├── requirements.txt            # Dependencias Python
├── google_credentials.json     # Credenciales Google (NO en GitHub)
├── .env                        # API keys (NO en GitHub)
├── .gitignore                  # Protege archivos sensibles
└── docs/
    ├── contexto.md
    ├── roadmap.md
    ├── tareas.md
    ├── sesiones.md
    └── videos_pendientes.md    # Lista de videos sin transcripción
```

## Problema Conocido: Vimeo IDs Obsoletos
Algunos temas de Biología y Física en WordPress tienen embebidos Vimeo IDs que ya no existen (dan error 404 en Vimeo). Esto significa que los videos fueron resubidos con nuevos IDs. Los videos en las carpetas "biologia" y "fisica" de Vimeo son versiones más recientes. Para completar los timestamps, hay que:
1. Descargar manualmente los `.vtt` desde Vimeo (carpeta por carpeta)
2. Identificar a qué tema corresponde cada transcripción
3. Procesarlos con Claude para mapear timestamps
