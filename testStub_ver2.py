# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 12:21:35 2025

@author: warre
Small test file added to check what Minimax value I will get
"""

from GameStatus_5120 import GameStatus
from multiAgent import minimax
from multiAgent import negamax

# X = +1, O = -1, 0 = empty
board = [
    [1, -1,  1],
    [0, -1,  0],
    [0,  0,  0]
]

game = GameStatus(board, turn_O=False)
score, move = minimax(game, depth=9, maximizingPlayer=True)

print("Minimax value:", score)
print("Best move for X:", move)

# Print the principal path (trace of chose moves)

score, move = negamax(game, depth=9, color=1)
print("\nNegamax value:", score)
print("Best move for X:", move)

