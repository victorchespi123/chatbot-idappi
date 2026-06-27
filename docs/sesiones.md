# Registro de Sesiones — Chatbot idappi

## Sesión 1 — 2026-06-27
**Tema**: Creación completa del chatbot, deploy y tracking.

**Contexto**:
- El proyecto nació como extensión del proyecto de métricas de Instagram.
- Victor quiere analizar idappi.com, mejorar SEO/GEO y gestionar WordPress.
- Se identificó el curso de Química UCV como piloto para un chatbot de IA.

**Acciones realizadas**:

### Fase 1: Extracción de datos
- Acceso al panel de WordPress de idappi.com via Chrome (extensión Claude in Chrome).
- Navegación completa por LearnDash LMS: 16 cursos en total.
- Extracción completa de la estructura del curso QUÍMICA – UCV:
  - 93 estudiantes, 17 lecciones, 70 temas, 9 cuestionarios (87 pasos).
  - URLs reales de cada lección y tema (base: `idappi.com/courses/quimica/`).
- Creación de `quimica_ucv_base_datos.xlsx` con 96 registros.

### Fase 2: Desarrollo del chatbot
- Chatbot CLI (`chatbot_quimica.py`) con Claude API — probado con 4 preguntas, todas correctas.
- Web app (`app_chatbot.py`) con Streamlit.
- Primera versión UI: rechazada por Victor ("muy genérica, hecha con IA").
- Segunda versión: diseño profesional con paleta idappi (negro + dorado), tipografía Inter.
- Correcciones: quitar Deploy button, quitar stats, arreglar contraste del input box (fondo oscuro + texto blanco).

### Fase 3: Infraestructura
- Separación del proyecto en carpeta independiente (`chatbot idappi/`).
- API key de Anthropic agregada al `.env`.
- Google Cloud: proyecto "chatbot-idappi", Sheets API habilitada, cuenta de servicio creada.
- Google Sheet "Chatbot idappi - Tracking" creado y conectado.
- Headers de tracking configurados: Fecha, Pregunta, Respuesta, Temas, URLs, Session ID.

### Fase 4: Deploy
- GitHub CLI instalado (v2.95.0) y autenticado como victorchespi123.
- Repo `victorchespi123/chatbot-idappi` creado (privado → público para Streamlit Cloud).
- Código pusheado a GitHub.
- Streamlit Community Cloud: cuenta creada, conectada a GitHub, secrets configurados (ANTHROPIC_API_KEY + credenciales Google).
- App deployada y LIVE en: `https://3aumyb4fsk33dnabmhqnjy.streamlit.app`
- Tracking verificado: 4 interacciones registradas en Google Sheets.

**Decisiones tomadas**:
- Chatbot desplegado en Streamlit Community Cloud (no Netlify — no soporta Python).
- Tracking de interacciones via Google Sheets.
- Repo GitHub público (necesario para Streamlit Cloud gratis; credenciales protegidas por .gitignore).
- Diseño debe ser elegante y profesional, no genérico (feedback guardado en memoria).
- Python 3.12 para deploy (3.9 no disponible en Streamlit Cloud).

**Precisión estimada**: ~70-75% con datos actuales. Para subir a ~95% se necesita entrar a cada tema y documentar contenido real.

**Próximos pasos**:
- Compartir link con alumnos para prueba piloto.
- Monitorear interacciones 1-2 semanas.
- Analizar datos y mejorar precisión.
