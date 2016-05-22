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

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(4):
    print "Turn ", turn+1
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or     guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        if turn == 3:
            print "Game Over"
            
        # Print (turn + 1) here!
        print_board(board)
        
'''

To Add:


1. Make multiple battleships: you'll need to be careful because you need to make sure that you don’t place battleships on top of each other on the game board. You'll also want to make sure that you balance the size of the board with the number of ships so the game is still challenging and fun to play.

2. Make battleships of different sizes: this is trickier than it sounds. All the parts of the battleship need to be vertically or horizontally touching and you’ll need to make sure you don’t accidentally place part of a ship off the side of the board.

3. Make your game a two-player game.

Use functions to allow your game to have more features like rematches, statistics and more!

'''
