# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 17:24:46 2025

@author: Elizaheth
A program that takes a tree and creates a minimax function to find the value of the root 
Goal: Understand how recursion propagates values up the tree
"""

# --- Example tree structure ---
#Use a dictionary to store value pairs (parent->children)
tree = {
    'A': ['B', 'C', 'D'],    # Root node
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': ['I', 'J'],
    'E': [3, 5],
    'F': [6, 9],
    'G': [1, 2],
    'H': [0, 7],
    'I': [4, 8],
    'J': [5, 2]
}
"""
Minimax Function-parameters: position->holds the current node position,
depth->holds the depth of the tree or the number of recusions, maximizingStatus
->bool holds pos. for max and neg for min
"""
def minimax(position, depth, maximizingStatus):
    # Base case: if depth is 0 or position has no children
    #isinstance checks if the position is a int or float
    if depth == 0 or isinstance(position, (int, float)):
        return position  # terminal value (leaf)

    # If position is a label, retrieve its children
    children = tree.get(position, [])
    
    # If children are terminal (numbers), just return max/min of them
    if all(isinstance(c, (int, float)) for c in children):
        return max(children) if maximizingStatus else min(children)
    
    # --- Maximizing Player  ---
    # If maximizingStatus == boolean positive(max)
    if maximizingStatus:
        #Declare maxEval and assign neg. infinity
        maxEval = float('-inf')
        #Iterate through the the children of the current position:
        for child in children:
        #for child,y in children.items():
            #Assign eval to minimax function
            eval = minimax(child, depth - 1, False)
            #stubs
           #print (child,y)
            print("\n Value after each iteration: ", eval)
            
            """
            After each iteration assign maxEval by comparing last recurssion 
            to maxEval
            """
            maxEval = max(maxEval, eval)
            
        return maxEval
     
    # --- Minimizing Player  ---
    else: # If maximizingStatus == boolean negative(max)
        #Declare minEval and assign pos. infinity
        minEval = float('inf')
        #Iterate through the the children of the current position:
        for child in children:
            #Assign eval to minimax function
            eval = minimax(child, depth - 1, True)
            """
            After each iteration assign minEval by comparing last recurssion 
            to minEval
            """
            minEval = min(minEval, eval)
        return minEval


# --- Run the algorithm ---
root_value = minimax('A', 3, True)
print("The minimax value of the root (A) is:", root_value)