import os

def obtener_canciones():

    carpeta = "musica"
    canciones = []

    for archivo in os.listdir(carpeta):
        if archivo.endswith(".mp3"):
            canciones.append(archivo)
    
    return canciones
