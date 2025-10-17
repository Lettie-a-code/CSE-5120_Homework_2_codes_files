# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 11:33:03 2025

@author: warre
Appended my Connect Child to Minamax file with the given stub first version
"""

# multiAgents.py
from GameStatus_5120 import GameStatus

def minimax(game_state: GameStatus, depth: int, maximizingPlayer: bool, alpha=float('-inf'), beta=float('inf')):
    terminal = game_state.is_terminal()
    
    if (depth == 0) or terminal:
        newScores = game_state.get_scores(terminal)
        return newScores, None
        for move in game_state.get_moves():
            child = game_state.get_new_state(move)
    best_move = None

    if maximizingPlayer:
        maxEval = float('-inf')
        for child in game_state.get_children():
            eval_score, _ = minimax(child, depth - 1, False, alpha, beta)
            if eval_score > maxEval:
                maxEval = eval_score
                best_move = child
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
        return maxEval, best_move

    else:
        minEval = float('inf')
        for child in game_state.get_children():
            eval_score, _ = minimax(child, depth - 1, True, alpha, beta)
            if eval_score < minEval:
                minEval = eval_score
                best_move = child
            beta = min(beta, eval_score)
            if beta <= alpha:
                break
        return minEval, best_move