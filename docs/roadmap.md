# Roadmap — Chatbot idappi

## Fase 1: MVP del Chatbot ✅ COMPLETADA
- [x] Extraer estructura completa del curso Química UCV desde WordPress/LearnDash
- [x] Crear base de datos con 96 registros (lecciones, temas, cuestionarios, URLs, keywords)
- [x] Desarrollar chatbot CLI con Claude API
- [x] Desarrollar web app con Streamlit
- [x] Diseño elegante con identidad visual de idappi (negro + dorado)
- [x] Separar proyecto en carpeta independiente (`chatbot idappi/`)

## Fase 2: Deploy y Tracking ✅ COMPLETADA
- [x] Configurar Google Cloud project (chatbot-idappi)
- [x] Habilitar Google Sheets API
- [x] Crear cuenta de servicio y credenciales
- [x] Crear Google Sheet para tracking de interacciones
- [x] Integrar tracking en app_chatbot.py
- [x] Crear repositorio en GitHub (victorchespi123/chatbot-idappi)
- [x] Instalar GitHub CLI y autenticar
- [x] Configurar Streamlit Secrets (API keys + credenciales Google)
- [x] Deploy en Streamlit Community Cloud
- [x] App LIVE en: https://3aumyb4fsk33dnabmhqnjy.streamlit.app
- [x] Verificar tracking funcionando (4 interacciones registradas)

## Fase 3: Prueba Piloto con Alumnos ⬅️ ACTUAL
- [ ] Compartir link con grupo de alumnos de Química UCV
- [ ] Monitorear interacciones en Google Sheets (1-2 semanas)
- [ ] Analizar qué temas buscan más
- [ ] Evaluar precisión de las respuestas
- [ ] Recopilar feedback de alumnos

## Fase 4: Mejora de Precisión
- [ ] Entrar a cada uno de los 70 temas y registrar contenido real (videos, ejercicios)
- [ ] Enriquecer keywords con contenido verificado
- [ ] Subir precisión del 70-75% al 90-95%
- [ ] Agregar manejo de preguntas frecuentes específicas
- [ ] Optimizar prompt de Claude para mejores respuestas

## Fase 5: Expansión
- [ ] Agregar más cursos de idappi (Biología UCV, Física UCV, Anatomía, etc.)
- [ ] Embeber chatbot directamente en idappi.com (widget WordPress)
- [ ] Sistema de feedback del alumno ("¿te sirvió esta respuesta?")
- [ ] Dashboard de analytics para el equipo de idappi
- [ ] URL personalizada para el chatbot
