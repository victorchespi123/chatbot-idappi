# Registro de Sesiones — Chatbot idappi

## Sesión 1 — 2026-06-27
**Tema**: Creación del chatbot desde cero, deploy y tracking.

**Acciones**:
- Acceso a WordPress de idappi.com, inventario de 16 cursos en LearnDash.
- Extracción completa del curso Química UCV (87 pasos, 70 temas, 9 cuestionarios).
- Creación de base de datos Excel con 96 registros (URLs, keywords, descripciones).
- Chatbot CLI con Claude API, probado con 8 preguntas — todas correctas.
- Web app Streamlit v1 (rechazada: "muy genérica") → v2 con diseño profesional (negro + dorado).
- Correcciones UI: quitar Deploy, quitar stats, arreglar contraste input.
- Separación del proyecto en carpeta independiente.
- Google Cloud: proyecto chatbot-idappi, Sheets API, cuenta de servicio.
- Tracking a Google Sheets conectado y verificado.
- GitHub repo creado, GitHub CLI instalado.
- Deploy en Streamlit Community Cloud — app LIVE.

## Sesión 2 — 2026-06-28
**Tema**: Verificación de contenido, timestamps de video e integración de Biología.

**Acciones**:
- Verificación real del contenido de los 70 temas de Química via API REST de WordPress.
- Keywords enriquecidas con contenido verificado (de ~75% a ~90% precisión).
- Extracción de Vimeo IDs de cada tema (70 temas → 66 con video).
- Descarga de 66 transcripciones de Vimeo (878K chars) usando JWT del browser.
- Procesamiento de transcripciones con Claude AI → 465 subtemas con timestamps exactos.
- Integración de timestamps al chatbot (ahora indica "minuto 03:05").
- Precisión Química subió a ~98%.
- Prueba con 8 preguntas variadas — todas correctas con timestamps.

**Integración Biología UCV**:
- Extracción del curso (11 lecciones, 30 temas, 1 cuestionario).
- Base de datos creada (41 registros).
- Chatbot actualizado: "Asistente Académico" con Química + Biología.
- Sidebar con ambos cursos, sugerencias mixtas.
- Activación de subtítulos AI en Vimeo para los 30 videos de Biología.
- 10 transcripciones descargadas, 9 procesadas → 52 subtemas con timestamps.
- 20 videos pendientes (Vimeo procesando subtítulos).
- Actualización de docs: separación definitiva del proyecto de métricas.

**Decisiones**:
- El chatbot es un proyecto independiente del de métricas de Instagram.
- Objetivo: chatbot general para todos los cursos de idappi.com.
- Próximo curso a integrar: Física UCV o Anatomía Humana UCV.

**Próximos pasos**:
- Completar timestamps de Biología (cuando Vimeo procese los 20 videos restantes).
- Prueba piloto con alumnos.
- Agregar más cursos.
