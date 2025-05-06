import numpy as np
import random

board = np.zeros((3,3), dtype="int")
turn = 1
move = 9

def play_turn():
    if(turn ==1):
        x = (input(f"What is player {turn}'s x position?"))
        y = (input(f"What is player {turn}'s y position?"))
    else:
        x = random.randint(0,2)
        y = random.randint(0,2)
    try: 
        if board[y, x]==0:   
            board[y, x]=turn 
        else:                              
            if(turn == 1):                     
                print("The board already contains")
            play_turn() 
    except IndexError:     
        print("Input error")  
        play_turn()  

def check_win():
    if any(np.sum(board, 1)==3) or any(np.sum(board, 0)==3) or sum(np.diag(board))==3 or sum(np.diag(board[::-1]))==3:
        return True
    if any(np.sum(board, 1)==-3) or any(np.sum(board, 0)==-3) or sum(np.diag(board))==-3 or sum(np.diag(board[::-1]))==-3:
        return True
    return False

while move >0:
    print(board)
    play_turn()   

    if check_win():
#         b

        print (f"Player {turn} has won!")
        break

#         c

    turn = turn*-1
    move = move -1
