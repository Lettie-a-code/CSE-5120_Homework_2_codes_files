# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 11:57:06 2025

@author: Elizabeth
connect Child into a working minimas
"""

import copy
#S.1 Board Representation
board = [
    ['X', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

#S.2.a  Win_Draw Detection
def check_winner(board):
    # check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    # check columns
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] != ' ':
            return board[0][c]
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

#S2.b Add a function to see if the board is full
def is_full(board):
    return all(' ' not in row for row in board)

#S.3 Scoring Function (Evaluation)
def evaluate(board):
    winner = check_winner(board)
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    return 0

#S4 Child Generation
def get_valid_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']


def generate_children(board, player):
    children = []
    for (r, c) in get_valid_moves(board):
        new_board = copy.deepcopy(board)
        new_board[r][c] = player
        children.append(new_board)
    return children

#SFull Minimax Function
def minimax(board, depth, maximizingPlayer):
    score = evaluate(board)
    print("This is the score: ", score, ".  This the depth", depth, "\n")
    #print(".  This the depth", depth, "\n")
    if score in (1, -1) or is_full(board) or depth == 0:
        return score

    if maximizingPlayer:
        maxEval = float('-inf')
        for child in generate_children(board, 'X'):
            eval = minimax(child, depth - 1, False)
            maxEval = max(maxEval, eval)
        return maxEval
    else:
        minEval = float('inf')
        for child in generate_children(board, 'O'):
            eval = minimax(child, depth - 1, True)
            minEval = min(minEval, eval)
        return minEval


# --- Test ---
test_board = [
    ['X', 'O', 'X'],
    [' ', 'O', ' '],
    [' ', ' ', ' ']
]

value = minimax(test_board, depth=5, maximizingPlayer=True)
print("Minimax value of this position:", value)
