#Lab8_Q1
from random import*

def printIntro():
    print("There is a 3x3 borad, player X and O fill in an")
    print("empty position of the board in one turn. The")
    print("winner is the first player who fill a horizontal")
    print("or a vertical or a main diagonal line.")

def draw_board(state):
    for i in range(0,9,3):
        print("-------")
        print("|",end="")
        for j in range(3):
            print(state[j+i],end="|")
        print()
    print("-------")
    
def formating(state):
    #check the number of element
    if len(state)!=9:
        print("Incorrect formating! Check the number of element.")
        return False
    #check element
    for i in range(9):
        if state[i]!="X" and state[i]!="O" and state[i]!=" ":
            print("Incorrect formating! Check the element.")
            return False
    return True

def getInputs():
    #return the game mode and the initial state

    #ask for the initial state
    print("\nPlase tell me the initial state in the form of list.")
    print("eg.X,O, , ,X,O,X, ,O")
    print("space represents that this position is empty. Must have 9 elements.")
    
    state=input("Enter initial state: ")
    state=state.split(",")
    #check if the user enter the correct state
    while not formating(state):
        state=input("Enter initial state: ")
        state=state.split(",")

    #draw out the inputs
    print("\nYour initial state is below.")
    draw_board(state)
    return "1",state
            
def simGame(mode,state):
    #return the winner
    turn="X"
    if mode=="1":
        print("X----> Player\nO----> Computer")
        #1-player
        #when there is no one wins
        while not GameOver(state)[0]:
            #let the player move
            if turn=="X":
                state=player_move(state,turn)
                print("You make your move! Here is the current state.")
                draw_board(state)
                turn="O"
            #let the computer move
            elif turn=="O":
                state=auto_move(state,turn)
                print("Computer make his move! Here is the current state: ")
                draw_board(state)
                turn="X"
        #return the second output
        return GameOver(state)[1]
        
    elif mode=="2":
        #2-player
        #when there is no one wins
        while not GameOver(state)[0]:
            #let the player X move
            if turn=="X":
                state=player_move(state,turn)
                print("Player X make the move! Here is the current state.")
                draw_board(state)
                turn="O"
            #let the player O move
            elif turn=="O":
                state=player_move(state,turn)
                print("Player O make the move! Here is the current state: ")
                draw_board(state)
                turn="X"
        #return the second output
        return GameOver(state)[1]

def GameOver(state):
    if state[0]==state[3]==state[6]=="X":
        return True,"Player X"
    elif state[0]==state[3]==state[6]=="O":
        return True,"Player O"
    elif state[1]==state[4]==state[7]=="X":
        return True,"Player X"
    elif state[1]==state[4]==state[7]=="O":
        return True,"Player O"
    elif state[2]==state[5]==state[8]=="X":
        return True,"Player X"
    elif state[2]==state[5]==state[8]=="O":
        return True,"Player O"
    elif state[0]==state[1]==state[2]=="X":
        return True,"Player X"
    elif state[0]==state[1]==state[2]=="O":
        return True,"Player O"
    elif state[3]==state[4]==state[5]=="X":
        return True,"Player X"
    elif state[3]==state[4]==state[5]=="O":
        return True,"Player O"
    elif state[6]==state[7]==state[8]=="X":
        return True,"Player X"
    elif state[6]==state[7]==state[8]=="O":
        return True,"Player O"
    elif state[0]==state[4]==state[8]=="X":
        return True,"Player X"
    elif state[0]==state[4]==state[8]=="O":
        return True,"Player O"
    elif state[2]==state[4]==state[6]=="X":
        return True,"Player X"
    elif state[2]==state[4]==state[6]=="O":
        return True,"Player O"
    for i in range(9):
        if state[i]==" ":
            return False," "
    return True,"No one"

def pos2i(pos):
    #row1
    if pos[0]==1:
        #rcol1
        if pos[1]==1:
            return 0
        #col2
        elif pos[1]==2:
            return 1
        #col3
        elif pos[1]==3:
            return 2
    #row2
    if pos[0]==2:
        #col1
        if pos[1]==1:
            return 3
        #col2
        elif pos[1]==2:
            return 4
        #col3
        elif pos[1]==3:
            return 5

    #row3
    if pos[0]==3:
        #col1
        if pos[1]==1:
            return 6
        #col2
        elif pos[1]==2:
            return 7
        #col3
        elif pos[1]==3:
            return 8

def pos_format(pos):
    if pos[0]==1 or pos[0]==2 or pos[0]==3:
        return True
    elif pos[1]==1 or pos[1]==2 or pos[1]==3:
        return True
    else:
        return False
def player_move(state,turn):
    #return the state after the move
    print("\neg. (1,2) standards for the square at row 1 and column 2")
    pos=eval(input("\nPlayer "+turn+" plase give me the position of your mark: "))
    while not pos_format(pos):
        print("Incorrect position!")
        pos=eval(input("\nPlayer "+turn+" plase give me the position of your mark: "))

    #conver the pos to an corresponding integer
    i=pos2i(pos)
    
    while state[i]!=" ":
        print("You cannot make this move! try again.")
        print("\neg. (1,2) standards for the square at row 1 and column 2")
        pos=eval(input("\nPlayer "+turn+" plase give me the position of your mark: "))
        while not pos_format(pos):
            pos=eval(input("\nPlayer "+turn+" plase give me the position of your mark: "))
        i=pos2i(pos)
    state[i]=turn
    return state

def auto_move(state,turn):
    #return the state after the move
    pos=[]
    #serach for the empty square
    for i in range(len(state)):
        if state[i]==" ":
            pos.append(i)
    state[choice(pos)]=turn
    return state

def main():
    #print an introduction
    printIntro()
    #ask for inputs: player mode, initial state
    mode,state=getInputs()
    #simulate games
    winner=simGame(mode,state)
    #print the result
    print(winner,"wins the game!")

