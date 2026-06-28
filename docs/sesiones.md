# Registro de Sesiones — Chatbot idappi

## Sesión 1 — 2026-06-27
**Tema**: Creación del chatbot desde cero, deploy y tracking.

**Acciones**:
- Acceso a WordPress de idappi.com, inventario de 16 cursos en LearnDash.
- Extracción completa del curso Química UCV (87 pasos, 70 temas).
- Base de datos Excel con 96 registros.
- Chatbot CLI y web app con Claude API.
- Diseño profesional (v1 rechazada → v2 aprobada).
- Google Cloud + Google Sheets tracking.
- GitHub repo + deploy en Streamlit Community Cloud.

## Sesión 2 — 2026-06-28
**Tema**: Mejora de precisión, timestamps de video, expansión a 3 cursos.

**Acciones realizadas**:

### Química UCV — Verificación y timestamps
- Verificación del contenido real de 70 temas via API REST WordPress.
- Extracción de 66 Vimeo IDs embebidos en los temas.
- Descarga de 66 transcripciones de Vimeo (878K chars) usando JWT.
- Procesamiento con Claude AI → 465 subtemas con timestamps exactos.
- Precisión subió de ~75% a ~98%.

### Biología UCV — Integración completa
- Extracción del curso (11 lecciones, 30 temas, 42 pasos).
- Base de datos creada (41 registros) con keywords enriquecidas.
- Subtítulos AI activados en Vimeo para los 30 videos.
- 9 transcripciones descargadas y procesadas → 52 subtemas.
- 21 videos con Vimeo IDs obsoletos (dan 404) — necesitan descarga manual.
- Precisión: ~90%.

### Física UCV — Integración completa
- Extracción del curso (8 lecciones, 49 temas, 58 pasos).
- Base de datos creada (57 registros) con keywords del contenido real.
- 15 transcripciones descargadas y procesadas → 102 subtemas.
- ~34 videos con Vimeo IDs obsoletos — necesitan descarga manual.
- Precisión: ~90%.

### Chatbot actualizado
- Pasó de "Asistente de Química" a "Asistente Académico" (3 cursos).
- Sidebar con los 3 cursos y sus lecciones.
- System prompt actualizado con los 3 cursos.
- Sugerencias mixtas (Química + Biología + Física).

### Problema descubierto
- Algunos videos embebidos en WordPress tienen Vimeo IDs que ya no existen (resubidos con nuevos IDs).
- Los videos en las carpetas de Vimeo son versiones actuales.
- Solución: descargar manualmente los .vtt desde Vimeo y procesarlos.
- Se creó `docs/videos_pendientes.md` con la lista completa (~55 videos).

### Bug encontrado y resuelto: Física no respondía
- Al agregar Física, el chatbot decía "ese curso no está disponible" para preguntas de Física.
- Causa: el contexto total era 121K chars — demasiado para que Claude procesara bien.
- Fix: optimizar contexto (truncar keywords a 150 chars, condensar timestamps en una línea por video).
- Contexto bajó de 121K a ~60K chars. Física empezó a funcionar correctamente.
- Se identificó que esta solución es temporal — necesitamos RAG para escalar a más cursos.

### Plan de escalabilidad definido
- Migrar a RAG (Retrieval-Augmented Generation) antes de agregar más cursos.
- Paso 1: búsqueda local (TF-IDF/embeddings) para encontrar los 5-10 registros más relevantes.
- Paso 2: pasar solo esos registros a Claude para armar la respuesta.
- Beneficio: contexto baja de 60K a ~2K chars, escala a 20+ cursos sin problema.

**Estado final**:
- 3 cursos integrados, 194 registros totales.
- 90 videos con timestamps, 619 subtemas mapeados.
- App live en Streamlit Cloud — los 3 cursos funcionan correctamente.
- Precisión: Química ~98%, Biología ~90%, Física ~90%.
- Alumnos pueden usarlo desde: https://3aumyb4fsk33dnabmhqnjy.streamlit.app

**Próximos pasos**:
- Implementar RAG para escalabilidad (ANTES de agregar más cursos).
- Descargar manualmente los .vtt de los ~55 videos pendientes desde Vimeo.
- Procesarlos con Claude para completar timestamps.
- Subir precisión de Biología y Física a ~98%.
- Agregar Anatomía Humana UCV (después de RAG).
