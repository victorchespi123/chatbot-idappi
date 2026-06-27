#!/usr/bin/env python3
"""
Chatbot de Química UCV — idappi.com
Responde preguntas de alumnos con links directos al contenido del curso.
Usa Claude como motor de IA para interpretar preguntas y buscar en la base de datos.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
import openpyxl
import anthropic

load_dotenv()

EXCEL_PATH = Path(__file__).parent / "quimica_ucv_base_datos.xlsx"
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def load_database():
    wb = openpyxl.load_workbook(EXCEL_PATH, read_only=True)
    ws = wb["Base de Datos Química UCV"]
    records = []
    for row in ws.iter_rows(min_row=2, values_only=True):
        if not row[0]:
            break
        records.append({
            "id": row[0],
            "tipo": row[1],
            "leccion": row[2],
            "tema": row[3] or "",
            "nombre_completo": row[4],
            "url": row[5],
            "keywords": row[6],
            "descripcion": row[7],
        })
    wb.close()
    return records


def build_db_context(records):
    lines = []
    for r in records:
        lines.append(f"[{r['tipo']}] {r['nombre_completo']}")
        lines.append(f"  Keywords: {r['keywords']}")
        lines.append(f"  Desc: {r['descripcion']}")
        lines.append(f"  URL: {r['url']}")
        lines.append("")
    return "\n".join(lines)


SYSTEM_PROMPT = """Eres el asistente virtual del curso de QUÍMICA – UCV en la plataforma idappi.com.
Tu trabajo es ayudar a los alumnos a encontrar exactamente dónde estudiar cada tema.

REGLAS:
1. Respondé SIEMPRE en español, de forma amigable y cercana (tuteo).
2. Cuando el alumno pregunte por un tema, buscá en la base de datos y devolvé:
   - El nombre del tema/lección
   - El link directo (URL completa)
   - Una breve explicación de qué va a encontrar ahí
3. Si hay varios temas relacionados, mencioná todos los relevantes (máximo 3), ordenados por relevancia.
4. Si la pregunta NO tiene relación con química o el curso, respondé amablemente que solo podés ayudar con temas del curso.
5. Si el alumno pregunta algo muy específico que podría estar en varios temas, mencioná las opciones.
6. Usá emojis para hacerlo más amigable: 📚 🔗 ✅ 💡 🧪 ⚗️
7. Sé conciso pero útil. No des explicaciones largas del tema — tu rol es DIRIGIR al alumno al contenido correcto.
8. Si el alumno te saluda, respondé brevemente y preguntá en qué tema necesita ayuda.

FORMATO DE RESPUESTA cuando encontrás contenido:
📚 **[Nombre del tema]**
🔗 [URL]
💡 [Qué va a encontrar ahí - 1 línea]
"""


def chat(query, records, db_context, history):
    history.append({"role": "user", "content": query})

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=f"{SYSTEM_PROMPT}\n\nBASE DE DATOS DEL CURSO:\n{db_context}",
        messages=history
    )

    assistant_msg = response.content[0].text
    history.append({"role": "assistant", "content": assistant_msg})
    return assistant_msg


def main():
    print("=" * 60)
    print("  🧪 CHATBOT DE QUÍMICA UCV — idappi.com")
    print("=" * 60)

    print("\nCargando base de datos del curso...")
    records = load_database()
    db_context = build_db_context(records)
    lecciones = sum(1 for r in records if r['tipo'] == 'Lección')
    temas = sum(1 for r in records if r['tipo'] == 'Tema')
    quizzes = sum(1 for r in records if r['tipo'] == 'Cuestionario')
    print(f"✅ {len(records)} registros: {lecciones} lecciones, {temas} temas, {quizzes} cuestionarios")
    print(f"🤖 Motor: Claude AI\n")
    print("Escribí tu pregunta sobre Química (o 'salir' para terminar):\n")

    history = []

    while True:
        try:
            query = input("👨‍🎓 > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\n👋 ¡Hasta luego! Éxitos estudiando Química.")
            break

        if not query:
            continue
        if query.lower() in ('salir', 'exit', 'quit', 'q'):
            print("\n👋 ¡Hasta luego! Éxitos estudiando Química.")
            break

        try:
            response = chat(query, records, db_context, history)
            print(f"\n🤖 {response}\n")
        except Exception as e:
            print(f"\n❌ Error: {e}\n")


if __name__ == "__main__":
    main()
