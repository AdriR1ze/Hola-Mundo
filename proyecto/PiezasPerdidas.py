# /* Piece.py

import pygame

class Pieza:
    def __init__(self, posicion, color, board):
        self.pos = posicion
        self.x = posicion[0]
        self.y = posicion[1]
        self.color = color
        self.has_moved = False

    def get_moves(self, board):
        output = []
        for direction in self.get_possible_moves(board):
            for square in direction:
                if square.occupying_piece is not None:
                    if square.occupying_piece.color == self.color:
                        break
                    else:
                        output.append(square)
                        break
                else:
                    output.append(square)
        return output