# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 17:19:22 2025

@author: elizabeth
first tic tac toe game
"""
def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_win(board, player):
    """Checks if the given player has won."""
    win_conditions = [
        # Horizontal
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        # Vertical
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        # Diagonal
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def check_draw(board):
    """Checks if the game is a draw."""
    return all(cell != ' ' for cell in board)

def play_game():
    """Runs the Tic-Tac-Toe game."""
    board = [' '] * 9  # Initialize an empty board
    current_player = 'X'
    game_over = False

    while not game_over:
        print_board(board)
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if not (0 <= move <= 8) or board[move] != ' ':
                print("Invalid move. Please choose an empty spot between 1 and 9.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        board[move] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            game_over = True
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()
