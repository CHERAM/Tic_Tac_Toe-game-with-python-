import random

def showBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])
    
def checkMove(board,pos):
    if board[pos]==' ':
        return True
    return False

def makeMove(board,value,pos):
    board[pos]=value
    
def winCheck(board,value):
    if (board[1]== value and board[2]==value and board[3] == value or
    board[4]==value and board[5]==value and board[6] == value or
    board[7]==value and board[8]==value and board[9] == value or 
    board[1]==value and board[5]==value and board[9] == value or
    board[3]==value and board[5]==value and board[7] == value or
    board[1]==value and board[4]==value and board[7] == value or
    board[2]==value and board[5]==value and board[8] == value or
    board[3]==value and board[6]==value and board[9] == value ):
        return True
    
def drawCheck(board):
    for i in range(1,10):
        if board[i]== ' ':
            return False
    return True
    
def playerSelect():
    return(random.randint(1,2))

def player_choice(board, marker):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not checkMove(board, int(position)):
        position = input("player "+str(player)+"choose your next position: (1-9)")
    return int(position)
def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

print("Welcome to Tic Tac Toe!!!!!!")
player = playerSelect()
print("player " + str(player) +" goes first")
while True:
    board={1:' ',2:' ',3:' ',
       4:' ',5:' ',6:' ',
       7:' ',8:' ',9:' '}
    player = playerSelect()
    print("player " + str(player) +" goes first")
    player_1 = "X"
    player_2 = "O"
    showBoard(board)
    game_on = True
    while game_on:
        if player == 1:
            pos = player_choice(board, player)
            makeMove(board,player_1,pos)
            showBoard(board)
            if winCheck(board,player_1):
                print("-----------------player 1 has won the game--------------")
                game_on = False
            else:
                if drawCheck(board):
                    print("the game is draw")
                    break
                else:
                    player = 2

        else:
            pos = player_choice(board, player)
            makeMove(board,player_2,pos)
            showBoard(board)
            if winCheck(board,player_2):
                print("------------------player 2 has won the game----------------")
                game_on = False
            else:
                if drawCheck(board):
                    print("the game is draw")
                    break
                else:
                    player = 1

    
    if not replay():
        break
   
            
        
    
    
