# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 12:01:00 2025

corrected code 
Problem: always getting a Minimax value at position 0.
citations:
When prompted with: "Please evaluate multiAgents.py.  I am not getting an
expected output".  The ChatFPT response "In your uploaded file multiAgents.py
the structure is problemative because the return statement ends the function-the 
folllowing for loop will nexver execute.  
(https://chatgpt.com/c/68e83848-c6e8-832c-b81f-e65cf5cfdf3d)
https://docs.python.org/3/reference/simple_stmts.html#the-return-statement)\   

@author: warre
"""
from GameStatus_5120 import GameStatus

def minimax(game_state: GameStatus, depth: int, maximizingPlayer: bool,
            alpha=float('-inf'), beta=float('inf')):
    
    # --- Base case ---
    terminal = game_state.is_terminal()
    if (depth == 0) or terminal:
        newScores = game_state.get_scores(terminal)
        return newScores, None

    best_move = None

    # --- MAX Player (X) ---
    if maximizingPlayer:
        maxEval = float('-inf')
        for move in game_state.get_moves():
            child = game_state.get_new_state(move)
            eval_score, _ = minimax(child, depth - 1, False, alpha, beta)
            
            if eval_score > maxEval:
                maxEval = eval_score
                best_move = move

            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break  # alpha-beta pruning
        return maxEval, best_move

    # --- MIN Player (O) ---
    else:
        minEval = float('inf')
        for move in game_state.get_moves():
            child = game_state.get_new_state(move)
            eval_score, _ = minimax(child, depth - 1, True, alpha, beta)
            
            if eval_score < minEval:
                minEval = eval_score
                best_move = move

            beta = min(beta, eval_score)
            if beta <= alpha:
                break  # alpha-beta pruning
        return minEval, best_move
