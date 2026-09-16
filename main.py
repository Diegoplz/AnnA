from voz.hablar import hablar
from voz.escuchar import escuchar
from comandos.gestor import ejecutar_comando
from recursos.frases import respuesta_activacion

def main():

    hablar("Sistema iniciado. Esperando activación.")

    while True:

        texto = escuchar()

        if texto == "":
            continue

        if "despierta" in texto:

            hablar(respuesta_activacion())

            comando = escuchar()

            if comando == "":
                continue

            continuar = ejecutar_comando(comando)

            if not continuar:
                break


if __name__ == "__main__":
    main()