from comandos.abrir import (
    abrir_chrome,
    abrir_bloc_notas,
    abrir_calculadora,
    abrir_vscode,
    abrir_netbeans,
    abrir_mysql
)
from comandos.internet import (
    abrir_youtube,
    abrir_github,
    abrir_chatgpt,
    buscar_google
)

from comandos.sistema import obtener_hora
from voz.hablar import hablar
from comandos.conversacion import responder


COMANDOS = {
    "abre chrome": (abrir_chrome, "Abriendo Chrome."),
    "abre bloc de notas": (abrir_bloc_notas, "Abriendo el Bloc de notas."),
    "abre calculadora": (abrir_calculadora, "Abriendo la calculadora."),
    "abre youtube": (abrir_youtube, "Abriendo YouTube."),
    "abre hub": (abrir_github, "Abriendo GitHub."),
    "abre chati": (abrir_chatgpt, "Abriendo ChatGPT."),
    "abre visual studio code": (abrir_vscode, "Abriendo Visual Studio Code."),
    "abre code": (abrir_vscode, "Abriendo Visual Studio Code."),
    "abre netbeans": (abrir_netbeans, "Abriendo NetBeans."),
    "abre mysql": (abrir_mysql, "Abriendo MySQL Workbench."),
}




def ejecutar_comando(comando):

    # Salir
    if any(palabra in comando for palabra in [
        "salir",
        "adiós",
        "hasta luego",
        "apágate",
        "termina",
        "cierra",
        "vale"
    ]):
        hablar("Hasta luego, Diego.")
        return True

    # Conversación
    respuesta = responder(comando)

    if respuesta:
        hablar(respuesta)
        return True

    # Hora
    if "dime la hora" in comando or "qué hora es" in comando:
        hablar(f"Son las {obtener_hora()}")
        return True

    # Buscar
    if "busca" in comando:
        busqueda = comando.replace("busca", "").strip()
        hablar(f"Buscando {busqueda}")
        buscar_google(busqueda)
        return True

    # Abrir programas
    for clave, (funcion, respuesta) in COMANDOS.items():
        if clave in comando:
            hablar(respuesta)
            funcion()
            return True

    hablar("Todavía no conozco ese comando.")
    return True
