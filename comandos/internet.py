import webbrowser
import urllib.parse


def abrir_youtube():
    webbrowser.open("https://www.youtube.com")


def abrir_github():
    webbrowser.open("https://github.com")


def abrir_chatgpt():
    webbrowser.open("https://chat.openai.com")


def buscar_google(busqueda):

    texto = urllib.parse.quote(busqueda)

    url = f"https://www.google.com/search?q={texto}"

    webbrowser.open(url)