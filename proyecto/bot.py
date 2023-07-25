import Pieza
from pygame.locals import *
import queue
import TableroConceptual
import requests
import json
class Bot:
    def enviar_peticion(self,tablero:TableroConceptual,turno:Pieza.TipoBando):
        contador=0
        url=f'https://www.chessdb.cn/cdb.php?action=querybest&board={tablero.notacion_fen(turno)}&json=1'
        print("Enviar peticion: ", url)
        req = requests.get(url)

        #b'{"status":"ok","move":"d6d5"}'
        if req.status_code == 200:
            print(req.content)
            data = json.loads(req.content)
            return data["move"]

        else:
            print("Error http get")
