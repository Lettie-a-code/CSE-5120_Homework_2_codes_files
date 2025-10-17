"""
Created on Thu Oct 16 11:44:00 2025

@author: warre
large_board_tic_tac_toe lets see how draw_game(self) function works
"""

import pygame
from GameStatus_5120 import GameStatus
from multiAgent import minimax, negamax
import sys, random

mode = "player_vs_ai" # default mode for playing the game (player vs AI)

class RandomBoardTicTacToe:   
    def __init__(self, size = (600, 600)):

        self.size = self.width, self.height = size
        # Define some colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)

        # Grid Size
        self.GRID_SIZE = 4
        self.OFFSET = 5

        self.CIRCLE_COLOR = (140, 146, 172)
        self.CROSS_COLOR = (140, 146, 172)

        # This sets the WIDTH and HEIGHT of each grid location
        self.WIDTH = self.size[0] / self.GRID_SIZE - self.OFFSET
        self.HEIGHT = self.size[1] / self.GRID_SIZE - self.OFFSET

        # This sets the margin between each cell
        self.MARGIN = 5

        pygame.init()
        # self.game_reset()
    #draw game
    def draw_game(self):
        #initialized property
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Tic Tac Toe Random Grid")
        self.screen.fill(self.BLACK)

        for row in range(self.GRID_SIZE):
            for col in range(self.GRID_SIZE):
                rect = pygame.Rect(
                    col * (self.WIDTH + self.MARGIN) + self.MARGIN,
                    row * (self.HEIGHT + self.MARGIN) + self.MARGIN,
                    self.WIDTH,
                    self.HEIGHT,
                )
                pygame.draw.rect(self.screen, self.WHITE, rect)

        pygame.display.update()

    def change_turn(self):
        #if self.game_state.turn_O:
        #self_game_state does not exist yet in the constructor
        if hasattr(self, "game_state") and self.game_state.turn_O:
            pygame.display.set_caption("Tic Tac Toe - O's turn")
        else:
            pygame.display.set_caption("Tic Tac Toe - X's turn")
      

    def is_game_over(self):

        """
        #YOUR CODE HERE TO SEE IF THE GAME HAS TERMINATED AFTER MAKING A MOVE. YOU SHOULD USE THE IS_TERMINAL()
        #FUNCTION FROM GAMESTATUS_5120.PY FILE (YOU WILL FIRST NEED TO COMPLETE IS_TERMINAL() FUNCTION)
        
        #YOUR RETURN VALUE SHOULD BE TRUE OR FALSE TO BE USED IN OTHER PARTS OF THE GAME
        """
    

    def move(self, move):
        self.game_state = self.game_state.get_new_state(move)


    def play_ai(self):
        """
        YOUR CODE HERE TO CALL MINIMAX OR NEGAMAX DEPENDEING ON WHICH ALGORITHM SELECTED FROM THE GUI
        ONCE THE ALGORITHM RETURNS THE BEST MOVE TO BE SELECTED, YOU SHOULD DRAW THE NOUGHT (OR CIRCLE DEPENDING
        ON WHICH SYMBOL YOU SELECTED FOR THE AI PLAYER)
        
        THE RETURN VALUES FROM YOUR MINIMAX/NEGAMAX ALGORITHM SHOULD BE THE SCORE, MOVE WHERE SCORE IS AN INTEGER
        NUMBER AND MOVE IS AN X,Y LOCATION RETURNED BY THE AGENT
        """
        
        self.change_turn()
        pygame.display.update()
        terminal = self.game_state.is_terminal()
        """ USE self.game_state.get_scores(terminal) HERE TO COMPUTE AND DISPLAY THE FINAL SCORES """



    def game_reset(self):
        self.draw_game()
        #Reset both the visual board and internal state
        #Reset internal board logic.  Tracks logical moves (for AI and win detection later)
        self.board = [['' for _ in range(self.GRID_SIZE)] for _ in range(self.GRID_SIZE)]
        #Determines whose turn it is.
        self.current_player = 'X'  # Start new game with X
        #Handles visual reset only
        self.draw_game()
        # 3 Optional: show reset message. Gives you quick feedback in Spyder console
        print("✅ Game board has been reset.")        
        #pygame.display.update()  handled in draw game () module

    def play_game(self, mode = "player_vs_ai"):
        done = False

        clock = pygame.time.Clock()


        while not done:
            for event in pygame.event.get():  # User did something
                """
                YOUR CODE HERE TO CHECK IF THE USER CLICKED ON A GRID ITEM. EXIT THE GAME IF THE USER CLICKED EXIT
                """
                
                """
                YOUR CODE HERE TO HANDLE THE SITUATION IF THE GAME IS OVER. IF THE GAME IS OVER THEN DISPLAY THE SCORE,
                THE WINNER, AND POSSIBLY WAIT FOR THE USER TO CLEAR THE BOARD AND START THE GAME AGAIN (OR CLICK EXIT)
                """
                    
                """
                YOUR CODE HERE TO NOW CHECK WHAT TO DO IF THE GAME IS NOT OVER AND THE USER SELECTED A NON EMPTY CELL
                IF CLICKED A NON EMPTY CELL, THEN GET THE X,Y POSITION, SET ITS VALUE TO 1 (SELECTED BY HUMAN PLAYER),
                DRAW CROSS (OR NOUGHT DEPENDING ON WHICH SYMBOL YOU CHOSE FOR YOURSELF FROM THE gui) AND CALL YOUR 
                PLAY_AI FUNCTION TO LET THE AGENT PLAY AGAINST YOU
                """
                
                # if event.type == pygame.MOUSEBUTTONUP:
                    # Get the position
                    
                    # Change the x/y screen coordinates to grid coordinates
                    
                    # Check if the game is human vs human or human vs AI player from the GUI. 
                    # If it is human vs human then your opponent should have the value of the selected cell set to -1
                    # Then draw the symbol for your opponent in the selected cell
                    # Within this code portion, continue checking if the game has ended by using is_terminal function
                    
            # Update the screen with what was drawn.
            pygame.display.update()

        pygame.quit()

#tictactoegame = RandomBoardTicTacToe()
#class just draw the grid and exit
#->To keep the window open, add a event loop test function (temporary)
    def wait_for_exit(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()
