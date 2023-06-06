from tictactoe.declare_winner import checkIfWin , checkIfTie
from tictactoe.play_game import printBoard
from tictactoe.new_player import playerInput,switchPlayer

global board = ["-", "-", "-",
                "-", "-", "-",
                "-", "-", "-"]

global currentplayer = "X"
global winner = None
global gamerunning = True

while gamerunning == True:
    printBoard(board)
    playerInput(board)
    checkIfWin(board)
    checkIfTie(board)
    switchPlayer()
    computer(board)
    checkIfWin(board)
    checkIfTie(board)
    
    
    

