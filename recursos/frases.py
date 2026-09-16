import random

RESPUESTAS_ACTIVACION = [
    "Sí, Diego.",
    "Te escucho.",
    "¿En qué puedo ayudarte?",
    "Aquí estoy.",
    "Adelante."
]


def respuesta_activacion():
    return random.choice(RESPUESTAS_ACTIVACION)