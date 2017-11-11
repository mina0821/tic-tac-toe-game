#Lab8_Q1_P2

from random import*

#Lab8_Q2

def statistics():
    #return games O-player won/ total games played
    o_win=0

    #calculating
    for i in range(50):
        #simulate the game without prints statement
        winner=simGame_auto("3",[" "," "," "," "," "," "," "," "," "])
        if winner=="Player O":
            o_win=o_win+1
    return o_win/50

def printIntro():
    print("There is a 3x3 borad, player X and O fill in an")
    print("empty position of the board in one turn. The")
    print("winner is the first player who fill a horizontal")
    print("or a vertical or a main diagonal line.")

#draw the state
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
    return "3",state
            
def simGame(mode,s):
    #return the winner
    turn="X"
    if mode=="3":
        print("X----> Computer\nO----> Computer")
        #when there is no one wins
        while not GameOver(s)[0]:
            #let the computer move
            if turn=="X":
                s=auto_move(s,turn)
                print("Player X make his move! Here is the current state.")
                draw_board(s)
                turn="O"
            #let the computer move
            elif turn=="O":
                s=auto_move(s,turn)
                print("Player O make his move! Here is the current state: ")
                draw_board(s)
                turn="X"
        #return the second output
        winner=GameOver(s)[1]
        return winner
    
def simGame_auto(mode,s):
    #return the winner
    turn="X"
    if mode=="3":
        #when there is no one wins
        while not GameOver(s)[0]:
            #let the computer move
            if turn=="X":
                s=auto_move(s,turn)
                turn="O"
            #let the computer move
            elif turn=="O":
                s=auto_move(s,turn)
                turn="X"
        #return the second output
        winner=GameOver(s)[1]
        return winner

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
