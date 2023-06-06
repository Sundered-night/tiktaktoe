
from play_game import printBoard



global board = ["-", "-", "-",
                "-", "-", "-",
                "-", "-", "-"]

global currentplayer = "X"
global winner = None
global gamerunning = True

def playerInput(board):
    inp = int(input("Select a spot 1-9: "))
    if board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Oops player is already at that spot.")
        
# switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"