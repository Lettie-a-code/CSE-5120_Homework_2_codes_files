"""
Created on Tue Oct 14 12:49:04 2025

@author: warre

chat GPT query I think there with a problem of the path that child nodes are generated because the Minimax value is 0, and Best Move for X; (2,1)
feedback:
The recursion ran successfully (no infinite loops, no missing returns
But the evaluation (get_scores) never saw a winning board — every terminal leaf ended up returning 0 (draw).
So your issue is not logic termination, but search path evaluation — i.e., your recursion never reaches a winner = 1 state.
The evaluation function (get_scores()) depends entirely on the class attribute self.winner, which is only set when is_terminal() is called.
https://chatgpt.com/c/68e83848-c6e8-832c-b81f-e65cf5cfdf3d
Additional Documentation
Debug-enhanced Minimax with alpha-beta pruning
Prints depth, move, and scores to help trace recursion.
"""

from GameStatus_5120 import GameStatus

def minimax(game_state: GameStatus, depth: int, maximizingPlayer: bool,
            alpha=float('-inf'), beta=float('inf'), indent: str = ""):
    """
    Debug version of minimax that prints move exploration at each depth.
    """
    terminal = game_state.is_terminal()
    if (depth == 0) or terminal:
        score = game_state.get_scores(terminal)
        print(f"{indent}↳ [BASE] Depth={depth}, Winner={game_state.winner}, Score={score}")
        return score, None

    best_move = None
    if maximizingPlayer:
        maxEval = float('-inf')
        print(f"{indent}MAX depth={depth}, α={alpha}, β={beta}")
        for move in game_state.get_moves():
            print(f"{indent}→ Exploring move {move} for X")
            child = game_state.get_new_state(move)
            eval_score, _ = minimax(child, depth - 1, False, alpha, beta, indent + "   ")
            print(f"{indent}← Move {move} score={eval_score}")
            if eval_score > maxEval:
                maxEval = eval_score
                best_move = move
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                print(f"{indent}PRUNE (α={alpha}, β={beta}) after move {move}")
                break
        print(f"{indent}✔ MAX depth={depth} best_move={best_move}, score={maxEval}")
        print("This is the value of maxEval: ", maxEval, "\n")
        return maxEval, best_move

    else:
        minEval = float('inf')
        print(f"{indent}MIN depth={depth}, α={alpha}, β={beta}")
        for move in game_state.get_moves():
            print(f"{indent}→ Exploring move {move} for O")
            child = game_state.get_new_state(move)
            eval_score, _ = minimax(child, depth - 1, True, alpha, beta, indent + "   ")
            print(f"{indent}← Move {move} score={eval_score}")
            if eval_score < minEval:
                minEval = eval_score
                best_move = move
            beta = min(beta, eval_score)
            if beta <= alpha:
                print(f"{indent}PRUNE (α={alpha}, β={beta}) after move {move}")
                break
        print(f"{indent}✔ MIN depth={depth} best_move={best_move}, score={minEval}")
        print("This is the value of minEval: ", minEval, "\n")
        return minEval, best_move
