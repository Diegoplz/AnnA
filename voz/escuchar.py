import speech_recognition as sr


def escuchar():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("🎤 Escuchando...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        audio = recognizer.listen(source)

    try:

        texto = recognizer.recognize_google(audio, language="es-ES")

        print(f"Tú: {texto}")

        return texto.lower()

    except sr.UnknownValueError:

        print("No he entendido lo que has dicho.")
        return ""

    except sr.RequestError:

        print("No hay conexión a Internet.")
        return ""