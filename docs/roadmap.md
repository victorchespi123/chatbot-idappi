# Roadmap — Chatbot idappi

## Fase 1: MVP Química UCV ✅ COMPLETADA
- [x] Extraer estructura del curso desde WordPress/LearnDash
- [x] Crear base de datos con 96 registros
- [x] Chatbot CLI y web app con Claude API
- [x] Diseño profesional (negro + dorado, tipografía Inter)
- [x] Verificar contenido real de los 70 temas via API REST WordPress
- [x] Extraer Vimeo IDs de cada tema

## Fase 2: Deploy y Tracking ✅ COMPLETADA
- [x] Google Cloud project + Google Sheets API + cuenta de servicio
- [x] Tracking de interacciones a Google Sheets
- [x] Repo GitHub (victorchespi123/chatbot-idappi)
- [x] Deploy en Streamlit Community Cloud
- [x] App LIVE: https://3aumyb4fsk33dnabmhqnjy.streamlit.app

## Fase 3: Timestamps de Videos ✅ COMPLETADA (Química)
- [x] Descargar 66 transcripciones de Vimeo via JWT
- [x] Procesar con Claude AI → 465 subtemas con timestamps
- [x] Integrar timestamps al chatbot
- [x] Precisión ~98% en Química

## Fase 4: Expansión a Biología UCV ✅ EN PROGRESO
- [x] Extraer estructura de Biología (11 lecciones, 30 temas)
- [x] Crear base de datos (41 registros)
- [x] Integrar al chatbot (ahora cubre Química + Biología)
- [x] Activar subtítulos automáticos en Vimeo (30 videos)
- [x] Descargar 10 transcripciones disponibles → 52 subtemas
- [ ] Descargar 20 transcripciones restantes (Vimeo procesando)
- [ ] Procesar timestamps restantes con Claude

## Fase 5: Más Cursos ⬅️ PRÓXIMO
- [ ] Física UCV
- [ ] Anatomía Humana UCV
- [ ] Otros cursos de idappi

## Fase 6: Mejoras del Producto
- [ ] URL personalizada (reemplazar hash por nombre legible)
- [ ] Botón de feedback ("¿te sirvió?")
- [ ] Dashboard de analytics con datos del Google Sheet
- [ ] Embeber chatbot directamente en idappi.com (widget WordPress)
- [ ] Caché de respuestas frecuentes (ahorro de API calls)
