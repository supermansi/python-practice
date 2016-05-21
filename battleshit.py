'''

Battleship - a one player game
There is a 5 X 5 grid with a ship hidden in one of the cells. You have 10 guesses to find the ship before it sinks!

'''
from random import randint

board = []

for i in range(5):
    board.append(['O']*5) #['O']represents a list so we append a list as an element to the list (2D)
    

def print_board(board):
    for i in board:
        print " ".join(i) #"-".join(list) will remove the [] and '' and join the elements by -
        
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
