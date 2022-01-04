# tic tac toe is played on a 3x3 board, so we can use arrays of length 3 for the board

"""

LOGIC 

tic tac toe board
[
    [-,-,-],
    [-,-,-],
    [-,-,-]
]

user input : 1 - 9 for the respective spots on the board
invalid input : already taken spot / non-existent spot
add the input to the board if not invalid
check if user already won -> rows / columns / diagonals
toggle between users upon successful moves
have to have loop running if no one has won yet (while loop)

"""

# Code 

# Building the Board 
# 2D Array - List containing 3 lists of length 3

board = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

def print_board(board):

    # To iterate through indexes in board (for each row)
    for row in board:

        # To iterate through inner arrays (for each individual slot)
        for slot in row:
            print(slot, end=" ")

        # Creates a new line after every slot in one row (3x)
        print()

# Quit function 
# Quits out of game if user decides to stop playing
def quit(user_input):
    if user_input.lower() == "q":
        print("Thanks for playing")
        return True
    else: return False
 
# To check if value entered is a number   
def isNum(user_input):
    if not user_input.isnumeric():
        print("This is not a valid number")
        return False
    else:
        return True

# Checking if the value entered is between the range of 1 - 9
def bounds(user_input):
    if user_input > 9 or user_input < 1:
        print("This number is not on the board and is out of bounds")
        return False
    else:
        return True

# Combines both requirements of bounds() and isNum
# To check if value entered is actually a number 1 - 9
def checkInput(user_input):
    
    # Check if is number
    if not isNum(user_input):
        return False
    user_input = int(user_input)        # Converts from string type to integer type
    
    # Check if number is within 1 - 9
    if not bounds(user_input):
        return False
    
    return True
    
# Loop for Game to keep running 

# Infinite loop until break;
while True:
    print_board(board)
    user_input = input("Please enter a position 1 - 9 or enter \"q\" to quit: ")

    # Quit loop
    # If quit() is true, this branch runs
    if quit(user_input):
        break
    if not checkInput(user_input):
        print("Please try again")
        continue                            # Reruns the loop from the beginning of the loop instead of starting again