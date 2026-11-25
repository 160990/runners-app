import csv
import json

def analyze_performance(name, time_str, pace_str, ai_score):
    """
    Simula el motor de IA que analiza los resultados de un corredor.
    En una versión real, esto conectaría con el API de Claude para generar texto dinámico.
    """

    # Lógica de ejemplo para recomendaciones basadas en datos
    pace_min = float(pace_str.replace(':', '.'))

    if pace_min < 4.0:
        advice = f"¡Increíble rendimiento, {name}! Estás en el nivel elite. Tu ritmo de {pace_str} min/km es muy competitivo."
    elif pace_min < 6.0:
        advice = f"Buen trabajo, {name}. Mantienes un ritmo sólido de {pace_str} min/km. Para bajar de los 5:00, enfócate en entrenamientos de intervalos."
    else:
        advice = f"Felicidades por terminar, {name}. Tu ritmo de {pace_str} min/km es un gran punto de partida. Te sugiero trabajar en tu base aeróbica."

    return {
        "atleta": name,
        "tiempo": time_str,
        "score_ia": ai_score,
        "recomendacion_coach": advice
    }

# Simulación de carga de datos desde un evento (CSV)
data_event = [
    ["BIB", "Nombre", "Tiempo", "Pace", "Score"],
    ["452", "Orlando Nano", "01:42:15", "4:51", 94],
    ["128", "Maria Garcia", "02:15:30", "6:25", 78],
    ["701", "Luis Perez", "01:20:05", "3:48", 98]
]

print("--- RUNNERS AI COACH ENGINE ---")
for row in data_event[1:]:
    analysis = analyze_performance(row[1], row[2], row[3], row[4])
    print(f"\nAtleta: {analysis['atleta']}")
    print(f"Tiempo: {analysis['tiempo']} | Score IA: {analysis['score_ia']}/100")
    print(f"Coach AI dice: {analysis['recomendacion_coach']}")
    print("-" * 30)

print("\nMotor de IA listo para integrar con la base de datos de Runners.")
