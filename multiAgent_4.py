
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 13:38:38 2025

#get_scores() is returning the correct leaf evaluation values (-1->0 wins, 1 for X wins, 0 for draw)
#then the recursion propages those values up via the line
and each MAX/MIN layer uses either
Prunes appear early 
Root stays 0 when there is a draw
root's 0 means best possible outcome with perfect play is a draw'
"""

"""
Minimax with alpha-beta pruning and principal variation tracing.
Shows the sequence of best moves leading to the final evaluation.
"""

from GameStatus_5120 import GameStatus

# Global path tracker
path_trace = []

def minimax(game_state: GameStatus, depth: int, maximizingPlayer: bool,
            alpha=float('-inf'), beta=float('inf'), indent: str = ""):
    global path_trace

    terminal = game_state.is_terminal()
    if (depth == 0) or terminal:
        score = game_state.get_scores(terminal)
        print(f"{indent}↳ [BASE] Depth={depth}, Winner={game_state.winner}, Score={score}")
        return score, None

    best_move = None

    # --- MAX player (X) ---
    if maximizingPlayer:
        maxEval = float('-inf')
        print(f"{indent}MAX depth={depth}, α={alpha}, β={beta}")
        for move in game_state.get_moves():
            child = game_state.get_new_state(move)
            eval_score, _ = minimax(child, depth - 1, False, alpha, beta, indent + "   ")
            if eval_score > maxEval:
                maxEval = eval_score
                best_move = move
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                print(f"{indent}PRUNE at depth={depth} after move {move} (α={alpha}, β={beta})")
                break
        print(f"{indent}✔ RETURN MAX depth={depth} → best_move={best_move}, score={maxEval}")
        path_trace.append((depth, 'MAX', best_move, maxEval))
        return maxEval, best_move

    # --- MIN player (O) ---
    else:
        minEval = float('inf')
        print(f"{indent}MIN depth={depth}, α={alpha}, β={beta}")
        for move in game_state.get_moves():
            child = game_state.get_new_state(move)
            eval_score, _ = minimax(child, depth - 1, True, alpha, beta, indent + "   ")
            if eval_score < minEval:
                minEval = eval_score
                best_move = move
            beta = min(beta, eval_score)
            if beta <= alpha:
                print(f"{indent}PRUNE at depth={depth} after move {move} (α={alpha}, β={beta})")
                break
        print(f"{indent}✔ RETURN MIN depth={depth} → best_move={best_move}, score={minEval}")
        path_trace.append((depth, 'MIN', best_move, minEval))
        return minEval, best_move


def print_principal_path():
    """Prints the condensed path of chosen moves."""
    print("\n🔍 Principal Path (Best Move Sequence):")
    for level in sorted(path_trace, key=lambda x: x[0], reverse=True):
        d, player, move, val = level
        print(f"Depth {d:<2} | {player:<3} chose move {move} with score {val}")
    print("----------------------------------------------------")
    if path_trace:
        print(f"Final Evaluation: {path_trace[0][3]}  (from root depth {path_trace[0][0]})")
        
        
        
print_principal_path()
