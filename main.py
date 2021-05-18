import random
import json
import os
from mensages import dic


JUGADAS = ["piedra",  "papel", "tijera", "lagarto", "spock"]
VICTORIA = [['piedra', 'papel'], ['papel', 'tijera'], ['tijera', 'piedra'], ['lagarto', 'piedra'], ['spock ', 'piedra'], ['spock', 'lagarto'], ['lagarto', 'tijera']]

SAVEFILE = 'data.json'
SAVE_ON_EXIT = True
SAVE_EACH_CYCLE = False


def salvaPuntuacion():
    with open(SAVEFILE, 'w') as outfile:
        json.dump(puntuacion, outfile)
    print(dic["salvada"])


def leerPuntuacion():
    if os.path.isfile(SAVEFILE):
        with open(SAVEFILE) as json_file:
            puntuacion = json.load(json_file)
        print(dic["cargada"])
    else:
        puntuacion = {
            "empatadas": 0,
            "perdidas": 0,
            "ganadas": 0
        }
        print(dic["nueva"])

    return puntuacion


def listarJugadas():
    contador = 1
    for jugada in JUGADAS:
        print(f"  {contador}) - {jugada.capitalize()}")
        contador += 1
    print(dic['salirOpt'].format(**{'i': contador}))


def usuarioElijeNumero():
    opcion = None
    listarJugadas()

    while opcion not in list(range(1, len(JUGADAS) + 2)):
        try:
            opcion = int(input(dic["elijes"]))
        except ValueError:
            print(dic['error'])

    opcion -= 1

    return opcion
    print("opcion")




def imprimirOpciones(pc, usuario):
    if [pc, usuario] in VICTORIA:
        usuarioGana("Ganaste")
    elif pc == usuario:
        usuarioEmpata("empate")
    else:
        usuarioPierde("perdiste")

    print(puntuacion)
    if SAVE_EACH_CYCLE:
        salvaPuntuacion()


def usuarioGana(msg):
    print(msg)
    print("\n")
    puntuacion["ganadas"] += 1


def usuarioPierde(msg):
    print(msg)
    print("\n")
    puntuacion["perdidas"] += 1


def usuarioEmpata(msg):
    print(msg)
    print("\n")
    puntuacion["empatadas"] += 1


def comprobarCodigoSalida(opcion):
    if opcion == len(JUGADAS):
        print(dic["salir"])
        if SAVE_ON_EXIT:
            salvaPuntuacion()
        exit()


puntuacion = leerPuntuacion()
print(puntuacion)

while True:
    opcionPc = random.randrange(0, len(JUGADAS))
    opcionUser = usuarioElijeNumero()
    comprobarCodigoSalida(opcionUser)
    imprimirOpciones(JUGADAS[opcionPc], JUGADAS[opcionUser])
