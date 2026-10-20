import asyncio
import edge_tts
import pygame
import os
import uuid

VOZ =  "ro-RO-AlinaNeural"   # Voz 
# es-CO-SalomeNeural
# es-PY-TaniaNeural
# ro-RO-AlinaNeural

pygame.mixer.init()


async def generar_audio(texto, archivo):
    comunicacion = edge_tts.Communicate(texto, VOZ)
    await comunicacion.save(archivo)


def hablar(texto):

    print(f"AnNa: {texto}")

    nombre = f"voz_{uuid.uuid4().hex}.mp3"

    asyncio.run(generar_audio(texto, nombre))

    pygame.mixer.music.load(nombre)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove(nombre)

