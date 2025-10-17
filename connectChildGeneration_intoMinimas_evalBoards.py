# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 11:57:06 2025

@author: Elizabeth
connect Child into a working minimas
"""

import copy
#S.1Board Representation

#Board Respresentation
board = [
    ['X', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
#S.2 Win/Draw Detection
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
    # no winner
    return None
#S.2- b Add a function to see if the board is full:
    
def is_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

#S.3 tep 3 Scoring Evaluation

def evaluate(board):
    winner = check_winner(board)
    if winner == 'X':   # MAX wins
        return 1
    elif winner == 'O': # MIN wins
        return -1
    else:
        return 0        # draw or ongoing
    
#S.4 – Child Generation (you already know this)

def get_valid_moves(board):
    moves = []
    for r in range(3):
        for c in range(3):
            if board[r][c] == ' ':
                moves.append((r, c))
    return moves

def generate_children(board, player):
    children = []
    for (r, c) in get_valid_moves(board):
        new_board = copy.deepcopy(board)
        new_board[r][c] = player
        children.append(new_board)
    return children
#5 – Full Minimax Function
def minimax(board, depth, maximizingPlayer):
    score = evaluate(board)

    # --- Base cases ---
    if score == 1 or score == -1 or is_full(board) or depth == 0:
        return score

    # --- MAX Player ('X') ---
    if maximizingPlayer:
        maxEval = float('-inf')
        for child in generate_children(board, 'X'):
            eval = minimax(child, depth - 1, False)
            maxEval = max(maxEval, eval)
        return maxEval

    # --- MIN Player ('O') ---
    else:
        minEval = float('inf')
        for child in generate_children(board, 'O'):
            eval = minimax(child, depth - 1, True)
            minEval = min(minEval, eval)
        return minEval
    
#tub
test_board = [
    ['X', 'O', 'X'],
    [' ', 'O', ' '],
    [' ', ' ', ' ']
]

value = minimax(test_board, depth=5, maximizingPlayer=True)
print("Minimax value of this position:", value)
