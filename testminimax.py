def draw_board(state):
    #draw out the state
    for i in range(0,9,3):
        print("-------")
        print("|",end="")
        for j in range(3):
            print(state[j+i],end="|")
        print()
    print("-------")
            
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

def legal_pos(state):
    #return the state after the move
    pos=[]
    #serach for the empty square
    for i in range(len(state)):
        if state[i]==" ":
            pos.append(i)
    return pos

def sts(state,turn):
    #return a list of all legal move of a state
    sts=[]
    #a copy of state
    temp=list(state)
    for pos in legal_pos(state):
        temp[pos]=turn
        sts.append(temp)
        temp=list(state)
    return sts

#swich the player for the next turn
def switch(turn):
    if turn=="X":
        return "O"
    else:
        return "X"

def prints(s,v):
    #prints out the state and value
    print("state=[",end="")
    print(",".join(s),end="")
    print("], Value="+str(v))
            
def minimax(S,player,turn):
    #return the value of the current state
    #player -> who wish to win
    #turn -> who play next
    '''minimax(player,board)
    if(game over in current board position)
        return winner
    children = all legal moves for player from this board
    if(max's turn)
        return maximal score of calling minimax on all the children
    else (min's turn)
        return minimal score of calling minimax on all the children'''
    if GameOver(S)[0]:
        player="Player "+player
        if GameOver(S)[1]==player:
            return 1
        elif GameOver(S)[1]=="No one":
            return 0
        else:
            return -1
        
    if player==turn:
        #store all the values of the children
        values=[]
        #go through every states in the sts
        #using "sts" function to build up all legal moves
        for item in sts(S,turn):
            #append the value in the list
            values.append(minimax(item,player,switch(turn)))
        return max(values)
                          
    else:
        values=[]
        for item in sts(S,turn):
            values.append(minimax(item,player,switch(turn)))
        return min(values)

#ask for the initial state
state=input("Enter initial state: ")
state=state.split(",")

#draw out the inputs
print("\nYour initial state is below.")
draw_board(state)

#ask for the player
p=input("Enter player name (X or O): ")
print("\n")

def test(S,player,turn):
    prints(S,minimax(S,player,turn))
    #return the value of the current state
    #player -> who wish to win
    #turn -> who play next
    '''minimax(player,board)
    if(game over in current board position)
        return winner
    children = all legal moves for player from this board
    if(max's turn)
        return maximal score of calling minimax on all the children
    else (min's turn)
        return minimal score of calling minimax on all the children'''
    if GameOver(S)[0]:
        player="Player "+player
        if GameOver(S)[1]==player:
            return 1
        elif GameOver(S)[1]=="No one":
            return 0
        else:
            return -1
        
    if player==turn:
        #store all the values of the children
        values=[]
        #go through every states in the sts
        #using "sts" function to build up all legal moves
        for item in sts(S,turn):
            #append the value in the list
            values.append(test(item,player,switch(turn)))
        return max(values)
                          
    else:
        values=[]
        for item in sts(S,turn):
            values.append(test(item,player,switch(turn)))
        return min(values)

test(state,p,p)
