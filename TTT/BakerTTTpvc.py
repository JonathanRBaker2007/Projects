#import statements
import random as r

#global var
gameBoard=[[" "," "," "],
          [" "," "," "],
          [" "," "," "]]

#functions
def printboard(board):
     for row in range(3):
          print(f"{board[row][0]}|{board[row][1]}|{board[row][2]}")
          if row!=2:
               print("-"*5)
     print()

def checkForWinner(board):
     #horizontal checking
     for r in range(len(board)):
          #if leftOne == middleOne    and middleOne  == rightOne   and leftOne not " "
          if(board[r][0]==board[r][1] and board[r][1]==board[r][2] and board[r][0]!=" "):
               # print("winner winnder chicken dinner")
               # printboard(board)
               return True
     
     #vertical checking 
     if(board[0][r]==board[1][r] and board[1][r]==board[2][r] and board[0][r]!=" "):
               # print("winner winnder chicken dinner")
               # printboard(board)
               return True
     #diagonally
     if board[0][0]==board[1][1] and board[0][0]==board[2][2] and board[0][0]!=" " and board[1][1]!=" " and board[2][2]!=" ":
     #    print("Winner!")
     #    printboard(board)
        return True
        

     if board[0][2]==board[1][1] and board[0][2]==board[2][0] and board[0][2]!=" " and board[1][1]!=" " and board[2][0]!=" ":
     #    print("Winner!")   
     #    printboard(board)     
        return True
     
     return False
     
def checkForCAT(board):
     #CAT or Tie or Scratch
     # if there are no more " " in each row
     for row in board:
          if " " in row:
               return False
     return True


def spotIsTaken(symbol,board,row,col):
     if board[row][col] == " ":
          board[row][col]=symbol
          return False
     return True

#main loop
print("Welcome to Tic Tac Toe!")

symbol="X"
#keep looping until a winner if found or a tie
while(symbol!="Q"):
     #print the gameBoard
     printboard(gameBoard)
     
     #player take a turn
     goodSpot=False      #goodSpot will determine if valid input and spot not taken
     while not goodSpot:
          row=int(input("row: "))-1
          col=int(input("col: "))-1
          if row in range(3) and col in range(3):
               #check if spot taken
               if spotIsTaken(symbol,gameBoard,row,col):
                    print("Spot Taken")
               else:
                    goodSpot=True 
                    if checkForWinner(gameBoard) or checkForCAT(gameBoard):
                         print("Winner!")   
                         printboard(gameBoard)  
                         break
                    symbol = "O"      #this will break the loop
     
     #check for a winner or CAT
     
     
     #swap turns
     goodSpot=False
     while symbol=="O":
          row=r.randint(0,2)
          col=r.randint(0,2)
          if row in range(3) and col in range(3):
               #check if spot taken
               if spotIsTaken(symbol,gameBoard,row,col):
                    print("CPU has to go again")
               else:
                    goodSpot=True 
                    if checkForWinner(gameBoard) or checkForCAT(gameBoard):
                         print("Winner!")   
                         printboard(gameBoard)
                         break
                    symbol = "X"

     if checkForWinner(gameBoard) or checkForCAT(gameBoard):
          symbol="Q"

