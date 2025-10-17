"""
Created on Thu Oct 16 10:00:02 2025
@author: Elizabeth
wrote pseudocode
change turns child_game_state_get_new_state(move)
integrate alpha-Beta pruning source=negama(child,depth-1, -beta, -alpha)
chatGPT query: I am trying to write code for a negamax algorithm: 
->Could you please give me feedback on my NegaMax pseudocode algorithm., 
->and show my how to incorporate into my muliAgent file.
->https://chatgpt.com/c/68e83848-c6e8-832c-b81f-e65cf5cfdf3d
"Eval (game_position) is just your existing get_scores"
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
        #print(f"{indent}↳ [BASE] Depth={depth}, Winner={game_state.winner}, Score={score}")
        return score, None

    best_move = None

    # --- MAX player (X) ---
    if maximizingPlayer:
        maxEval = float('-inf')
        #print(f"{indent}MAX depth={depth}, α={alpha}, β={beta}")
        for move in game_state.get_moves():
            child = game_state.get_new_state(move)
            eval_score, _ = minimax(child, depth - 1, False, alpha, beta, indent + "   ")
            if eval_score > maxEval:
                maxEval = eval_score
                best_move = move
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                #print(f"{indent}PRUNE at depth={depth} after move {move} (α={alpha}, β={beta})")
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
                #print(f"{indent}PRUNE at depth={depth} after move {move} (α={alpha}, β={beta})")
                break
        print(f"{indent}✔ RETURN MIN depth={depth} → best_move={best_move}, score={minEval}")
        path_trace.append((depth, 'MIN', best_move, minEval))
        return minEval, best_move
    
def negamax(game_state: GameStatus, depth: int, alpha=float('-inf'), beta=float('inf'),
            color=1, indent=""):
    """
    Negamax search with alpha-beta pruning.
    color = +1 for X (maximizing), -1 for O (minimizing)
    Returns: (score, best_move)
    """
    terminal = game_state.is_terminal()
    if depth == 0 or terminal:
        score = color * game_state.get_scores(terminal)
        print(f"{indent}↳ [BASE] Depth={depth}, Color={color}, Winner={game_state.winner}, Score={score}")
        return score, None

    max_score = float('-inf')
    best_move = None

    for move in game_state.get_moves():
        child = game_state.get_new_state(move)
        eval_score, _ = negamax(child, depth - 1, -beta, -alpha, -color, indent + "   ")
        eval_score = -eval_score  # flip sign for the current player

        print(f"{indent}Move {move} at depth={depth}, eval={eval_score}, α={alpha}, β={beta}")

        if eval_score > max_score:
            max_score = eval_score
            best_move = move

        alpha = max(alpha, eval_score)
        if alpha >= beta:
            print(f"{indent}PRUNE at depth={depth} on move {move} (α={alpha}, β={beta})")
            break

    print(f"{indent}✔ RETURN NEGAMAX depth={depth} → best_move={best_move}, score={max_score}")
    return max_score, best_move

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
