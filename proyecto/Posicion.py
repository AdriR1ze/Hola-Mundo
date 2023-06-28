
def Casilla(QueQuiere):
        ListaDeNumeros = ["1", "2", "3", "4", "5", "6", "7", "8"]
        ListaDeLetras = ["A", "B", "C", "D", "E", "F", "G", "H"]
        posicion = {}
        for letra in ListaDeLetras:
            for numero in ListaDeNumeros:
                posicion[letra + numero] = letra + numero
        return posicion[QueQuiere]





