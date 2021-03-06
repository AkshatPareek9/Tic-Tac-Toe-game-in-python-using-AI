#for wait I used the import time
import time

board = [' ' for x in range(10)]       

#insert letter X and O
def insertLetter(letter,pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '


#print the design of board

def printBoard(board):
    
    print('\t ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('\t------------')
    print('\t ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('\t------------')
    print('\t ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

#horizontally and vertically and diagonally same letter occurs then that letter has won the game
def IsWinner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))


#all the players move contain in this function

def playerMove():
    run = True
    while run:
        move = input("\n\tPlease select a position to enter the X between 1 to 9:\t")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X' , move)
                else:
                    print('\n\tSorry, this space is occupied')
            else:
                print('\n\tPlease type a number between 1 and 9.')

        except:
            print('\n\tPlease type a number')

#randomly select the position for computer move by artificial intelligent mind
def computerMove():
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0  ]
    move = 0

    for let in ['O' , 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            
            if IsWinner(boardcopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1 , 3 , 7 , 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

#RANDOMLY POSITION IS SELECTED
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def main():
    print("\n\tWELCOME TO THE GAME\n\n\tTIC - TAC - TOE\n")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(IsWinner(board , 'O')):
            playerMove()
            printBoard(board)
            
        else:
            print("\n\tSorry you loose..!!\n")
            time.sleep(3)
            break

        if isBoardFull(board):
            print("\n\tTie game..!!")
            time.sleep(3)
            break
            
        if not(IsWinner(board , 'X')):
            move = computerMove()
            if move == 0:
                print(" ")
            else:
                insertLetter('O' , move)
                print('\n\tComputer placed an O on position ' , move , ':')
                printBoard(board)
                
        else:
            print("\n\tHURRAY!! .... YOU WON THE GAME!!")
            time.sleep(3)
            break


#PROGRAM STARTS FROM HERE
#MAIN PART IS THIS 

print("\n\tHELLO EVERYONE.... THIS IS THE BEGINNING OF THE GAME....\n")
x = input("\n\tDo you want to play? (y/n): \t")

#game loaded to play
while True:
    if x.lower() == 'y':
        print("\n\n\tLOADING....")
        time.sleep(3)
        board = [' ' for x in range(10)]                 
        print('\n\t----------------------------------------')
        main()
    else:
        break
    x = input("\n\tDo you want to play again? (y/n): \t")        
    
