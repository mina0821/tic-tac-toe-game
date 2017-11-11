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

def getInputs():
    #return the game mode and the initial state
    #ask for the game mode
    print("\nPlease choose 0-player, 1-player or a 2-player mode.")
    print("Enter 1 below if you choose 1-player. 2 for 2-player. etc.")
    
    mode=input("Please tell me the game mode: ")

    #ask for the initial state
    print("\nPlase tell me the initial state in the form of list.")
    print("eg.X,O, , ,X,O,X, ,O")
    print("space represents that this position is empty. Must have 9 elements.")
    
    state=input("Enter initial state: ")
    state=state.split(",")

    #draw out the inputs
    print("\nYour initial state is below.")
    draw_board(state)
    return mode,state

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
            
def minimax(S,player,turn,alpha,beta):
    #return the value of the current state
    #player -> who wish to win
    #turn -> who play next
    #alpha -> initially - infinity
    #beta -> initially + infinity
    '''alpha-beta(player,board,alpha,beta)
    if(game over in current board position)
        return winner

    children = all legal moves for player from this board
    if(max's turn)
        for each child
            score = alpha-beta(other player,child,alpha,beta)
            if score > alpha then alpha = score (we have found a better best move)
            if alpha >= beta then return alpha (cut off)
        return alpha (this is our best move)
    else (min's turn)
        for each child
            score = alpha-beta(other player,child,alpha,beta)
            if score < beta then beta = score (opponent has found a better worse move)
            if alpha >= beta then return beta (cut off)
        return beta (this is the opponent's best move)'''
    
    if GameOver(S)[0]:
        player="Player "+player
        if GameOver(S)[1]==player:
            return 1
        elif GameOver(S)[1]=="No one":
            return 0
        else:
            return -1
        
    #using "sts" function to build up all legal moves
    children=sts(S,turn)
    
    if player==turn:
        #go through every states
        for item in children:
            score=minimax(item,switch(player),turn,alpha,beta)
            if score > alpha:
                alpha=score
            elif alpha >= beta:
                return alpha
        return alpha
                          
    else:
        for item in children:
            score=minimax(item,switch(player),turn,alpha,beta)
            if score < beta:
                beta=score
            elif alpha >= score:
                return beta
        return beta

def TreeBuild(S,player,turn):
    #return a list of info from S
    #[game board,value,whose move,move]

    #add game board
    result=list(S)
    #append value
    result.append(minimax(S,player,turn,-100,100))
    #whose move
    result.append(turn)

    values=[]
    moves=[]
    sts=[]
    #a copy of state
    temp=list(S)
    for pos in legal_pos(S):
        temp[pos]=turn
        #append the state and pos
        sts.append((temp,pos))
        temp=list(S)

    for i in range(len(sts)):
        #go through all the possible next move
        #append the value resulting from the next move
        values.append(minimax(sts[i][0],player,switch(turn),-100,100))
        #append the moves
        moves.append(sts[i][1])

    if player==turn:
        #get the index
        inx=values.index(max(values))
    else:
        inx=values.index(min(values))
        
    #append the corresponding pos
    result.append(moves[inx])
    return result

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
                state=auto_move(state,"O",turn)
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
    
    elif mode=="0":
        #0-player
        #when there is no one wins
        while not GameOver(state)[0]:
            #let the player X move
            if turn=="X":
                state=auto_move(state,"X",turn)
                print("Player X make the move! Here is the current state.")
                draw_board(state)
                turn="O"
            #let the player O move
            elif turn=="O":
                state=auto_move(state,"O",turn)
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

def player_move(state,turn):
    #return the state after the move
    print("\neg. (1,2) standards for the square at row 1 and column 2")
    pos=eval(input("\nPlayer "+turn+" plase give me the position of your mark: "))
    #convert the pos to an corresponding integer
    i=pos2i(pos)

    state[i]=turn
    return state

def auto_move(state,player,turn):
    #return the state after the move
    pos=TreeBuild(state,player,turn)[-1]
    state[pos]=turn
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

