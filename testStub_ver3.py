# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 10:58:59 2025

@author warren
full call that creates a text file
"""

from GameStatus_5120 import GameStatus
from multiAgent import minimax
from multiAgent import negamax 
from multiAgent import print_principal_path, write_principal_path_to_file

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

# Optional: print and save the principal path
#print_principal_path()
write_principal_path_to_file("miniMax_debug_trace.txt")

