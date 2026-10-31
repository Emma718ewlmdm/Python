from biblioteca.biblioteca import obtener_canciones
from player.reproductor import Reproductor
import select
import sys


canciones = obtener_canciones()

if not canciones:
    print("No hay canciones en la carpeta musica.")
    sys.exit()

reproductor = Reproductor()

indice = 0


def reproducir_actual():
    ruta = "musica/" + canciones[indice]

    print(f"\n▶ Reproduciendo: {canciones[indice]}")

    reproductor.reproducir(ruta)


reproducir_actual()


while True:

    print("\n[P] Pausar/Reanudar")
    print("[N] Siguiente")
    print("[A] Anterior")
    print("[S] Detener")
    print("[Q] Salir")

    while True:

        # Esperar hasta 0.5 segundos por una entrada
        entrada, _, _ = select.select([sys.stdin], [], [], 0.5)

        # Si el usuario escribió algo
        if entrada:

            comando = input("> ").lower()

            if comando == "p":

                if reproductor.esta_pausado():
                    reproductor.reanudar()
                    print("▶ Reanudando...")
                else:
                    reproductor.pausar()
                    print("⏸ Pausado")

            elif comando == "n":

                indice += 1

                if indice >= len(canciones):
                    indice = 0

                reproducir_actual()
                break

            elif comando == "a":

                indice -= 1

                if indice < 0:
                    indice = len(canciones) - 1

                reproducir_actual()
                break

            elif comando == "s":

                reproductor.detener()
                print("⏹ Detenido")
                break

            elif comando == "q":

                reproductor.detener()
                print("Saliendo...")
                sys.exit()

            else:

                print("Comando no válido.")

        # Si no hubo entrada, comprobamos la canción
        else:

            if not reproductor.reproduciendo():

                indice += 1

                if indice >= len(canciones):
                    indice = 0

                reproducir_actual()
                break
