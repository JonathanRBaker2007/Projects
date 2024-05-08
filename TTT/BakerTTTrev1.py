from operator import truediv


artboard ='''
    |   |   
-------------
    |   |   
-------------
    |   |   
'''

currentBoard=[["","",""],
              ["","",""],
              ["","",""]]

symbol = "x"
def printboard(board):
    #i= each row
    print()
    for i in range(3):
        print(f"{board[i][0]}|{board[i][1]}|{board[i][2]}")
        if i!=2:
            print("-"*5)
    print()
        
def checkForWinner(board):
    global winner
    
    for r in range(len(board)):
        if(board[r][0]==board[r][1] and board[r][1]==board[r][2] and board[r][0]!=""):
            winner = True
            print("WInner!")
        if(board[0][r]==board[1][r] and board[1][r]==board[2][r] and board[0][r]!=""):
            winner = True
            print("WInner!")
    
    if board[0][0]==board[1][1] and board[0][0]==board[2][2] and board[0][0]!="" and board[1][1]!="" and board[2][2]!="":
        winner = True
        print("Winner!")

    if board[0][2]==board[1][1] and board[0][2]==board[2][0] and board[0][2]!="" and board[1][1]!="" and board[2][0]!="":
        winner = True
        print("Winner!")
        



def checkForTie(board):
    global winner
    for row in board:
        if "" in row:
            winner = False
        else:
            winner = True
            print("Tie :(")
            

def userTurn():
    global symbol
    if symbol =="x":
        
        if len(currentBoard[r][c]) != 1:
            currentBoard[r][c]=(symbol)
            symbol = "o"
        else:
            print("spot taken")
    elif symbol == "o":
        if len(currentBoard[r][c]) != 1:
            currentBoard[r][c] =(symbol)
            symbol = "x"
        else:
            print("spot taken")

#program loop
winner = False


while winner == False or symbol =="q":
    printboard(currentBoard)
    r=int(input("Row: "))-1
    c=int(input("Col: "))-1
    if r in range(3) and c in range(3):
        pass
    else:
        r=int(input("Row: "))-1
        c=int(input("Col: "))-1

    userTurn()
    checkForTie(currentBoard)

    checkForWinner(currentBoard)
