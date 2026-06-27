# Registro de Sesiones — Chatbot idappi

## Sesión 1 — 2026-06-26
**Tema**: Creación del chatbot de Química UCV para idappi.com

**Contexto**:
- El proyecto nació como extensión del proyecto de métricas de Instagram.
- Victor quiere analizar idappi.com, mejorar SEO/GEO y gestionar WordPress como admin.
- Se identificó el curso de Química UCV como piloto para un chatbot de IA.

**Acciones realizadas**:
- Acceso al panel de WordPress de idappi.com via Chrome (extensión Claude in Chrome).
- Navegación completa por LearnDash LMS: 16 cursos en total.
- Extracción completa de la estructura del curso QUÍMICA – UCV:
  - 93 estudiantes, 17 lecciones, 70 temas, 9 cuestionarios (87 pasos).
  - URLs reales de cada lección y tema (base: `idappi.com/courses/quimica/`).
- Creación de `quimica_ucv_base_datos.xlsx` con 96 registros (ID, tipo, lección, tema, URL, keywords, descripción para IA).
- Desarrollo de chatbot CLI (`chatbot_quimica.py`) con Claude API.
- Desarrollo de web app (`app_chatbot.py`) con Streamlit.
- Primera versión: diseño genérico — rechazada por Victor (muy "hecha con IA").
- Segunda versión: diseño profesional con paleta idappi (negro + dorado), tipografía Inter.
- Correcciones aplicadas: quitar Deploy button, quitar stats, arreglar contraste del input box.
- Separación del proyecto en carpeta independiente (`chatbot idappi/`).

**Decisiones tomadas**:
- El chatbot se desplegará en Streamlit Community Cloud (no Netlify — no soporta Python).
- Tracking de interacciones via Google Sheets.
- Repositorio GitHub independiente para el chatbot.
- Diseño debe ser elegante y profesional, no genérico.

**Stack definido**: Streamlit + Claude API + Excel (base de datos) + Google Sheets (tracking).

**Precisión estimada**: ~70-75% con datos actuales (keywords inferidas por nombre de tema, no por contenido real). Para subir a ~95% se necesita entrar a cada tema y documentar contenido.

**Próximos pasos**:
- Configurar Google Sheets para tracking.
- Crear repo GitHub y hacer deploy en Streamlit Cloud.
- Prueba piloto con alumnos.
