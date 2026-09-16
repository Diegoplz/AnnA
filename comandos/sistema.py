from datetime import datetime

def obtener_hora():

    ahora= datetime.now()

    return ahora.strftime("%H:%M")

