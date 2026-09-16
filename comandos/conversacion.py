import random

RESPUESTAS = {

    "como estas": [
        "Estoy funcionando perfectamente.",
        "Todo en orden.",
        "Me encuentro lista para ayudarte."
    ],

    "gracias": [
        "De nada, Diego.",
        "Siempre es un placer ayudarte.",
        "Para eso estoy."
    ],

    "quien eres": [
        "Soy Anirul, tu asistente personal.",
        "Soy Anirul, diseñado para ayudarte."
    ],

    "buenos dias": [
        "Buenos días, Diego.",
        "Espero que tengas un gran día."
    ],

    "buenas tardes": [
        "Buenas tardes."
    ],

    "buenas noches": [
        "Buenas noches."
    ]
}


def responder(comando):

    for pregunta, respuestas in RESPUESTAS.items():

        if pregunta in comando:

            return random.choice(respuestas)

    return None