import Pieza
from pygame.locals import *
import queue
import TableroConceptual
import requests
class Bot:
    def enviar_peticion(self,tablero:TableroConceptual,turno:Pieza.TipoBando):
        url=f'https://www.chessdb.cn/cdb.php?action=querybest&board={tablero.notacion_fen(turno)}&json=1'
        print("Enviar peticion: ", url)
        req = requests.get(url)
        if req.status_code == 200:
            print(req.content)
        else:
            print("Error http get")
