import Pieza
from pygame.locals import *
import queue
import TableroConceptual
import requests
import json
class Bot:
    def enviar_peticion(self,tablero:TableroConceptual,turno:Pieza.TipoBando,dificultad, quien_juega):


        print("Fen: ", tablero.notacion_fen(turno))
        #https://stockfish.online/api/stockfish.php?fen=r2q1rk1/ppp2ppp/3bbn2/3p4/8/1B1P4/PPP2PPP/RNB1QRK1 w - - 5 1&depth=13&mode=bestmove
        url=f'https://stockfish.online/api/stockfish.php?fen={tablero.notacion_fen(turno)}&depth={dificultad}&mode=bestmove'
        print("Enviar peticion: ", url)

        req = requests.get(url)

        #b'{"status":"ok","move":"d6d5"}'
        if req.status_code == 200:
            print("Respuesta: ", req.content)
            data = json.loads(req.content)
            print(data["data"][9:13])
            return data["data"][9:13]

        else:
            print("Error http get")
