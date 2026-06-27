# Tareas Técnicas Pendientes — Chatbot idappi

## Prioridad Alta
- [ ] Compartir link del chatbot con alumnos de Química UCV
- [ ] Monitorear Google Sheet de tracking durante 1-2 semanas
- [ ] Analizar datos: qué preguntan, con qué frecuencia, qué temas son más buscados
- [ ] Evaluar si las respuestas del chatbot son precisas y útiles

## Prioridad Media
- [ ] Enriquecer base de datos: entrar a cada tema y documentar contenido real (videos, ejercicios)
- [ ] Agregar botón de feedback ("¿te sirvió?") en la interfaz
- [ ] Crear dashboard de analytics con los datos de Google Sheets
- [ ] Optimizar prompt de Claude para respuestas más precisas
- [ ] Personalizar URL del chatbot (cambiar hash por nombre legible)
- [ ] Agregar manejo de errores cuando la API falla (fallback local con TF-IDF)

## Prioridad Baja
- [ ] Agregar más cursos (Biología, Física, Anatomía)
- [ ] Crear widget embebible para WordPress (integrar en idappi.com)
- [ ] Implementar caché de respuestas frecuentes (ahorro de API calls)
- [ ] Modo offline con búsqueda TF-IDF como backup

## Completadas
- [x] Acceso a WordPress de idappi.com via Chrome
- [x] Inventario de 16 cursos en LearnDash
- [x] Extraer contenido del curso Química UCV (87 pasos, 17 lecciones, 70 temas, 9 cuestionarios)
- [x] Crear base de datos Excel con 96 registros (IDs, tipos, URLs, keywords, descripciones)
- [x] Chatbot CLI funcional con Claude API
- [x] Web app Streamlit con diseño profesional (negro + dorado, tipografía Inter)
- [x] Correcciones UI: quitar Deploy button, quitar stats, arreglar contraste input box
- [x] Separar proyecto en carpeta independiente (chatbot idappi/)
- [x] Crear documentación del proyecto (docs/)
- [x] Configurar Google Cloud project + Google Sheets API + cuenta de servicio
- [x] Integrar tracking de interacciones a Google Sheets
- [x] Crear repo GitHub (victorchespi123/chatbot-idappi, público)
- [x] Instalar GitHub CLI + autenticación
- [x] Deploy en Streamlit Community Cloud (app LIVE)
- [x] Verificar tracking funcionando (4 interacciones registradas)
