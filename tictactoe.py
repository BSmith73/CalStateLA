# Tic Tac Toe

import random
print("\u0001")
# This function prints out the game board. 
def drawBoard(board):
    
    # "board" is a list of 10 strings representing the board. 0 is not included in this list as it is not on a number pad.
    # This is the section of the assignment that required us to rename the string used to make this board "reversed." I just swapped the 789 seqeunce and the 123 sequence.
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])

#Defines which letter the player will use.
def inputPlayerLetter():
    
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    letter = ''
    # The use of the 'not' fucntion prevents the user from inputting anything other than X or O. If they type a different letter the boolean value will be true and restart the while loop.
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the list is the player's letter, the second is the computer's letter.
    # I have replaced the O with a smiley face because it's a fun easter egg.
    if letter == 'X':
        return ['X', '\u0001']
    else:
        return ['\u0001', 'X']

# Randomly choose the player who goes first. If 0 is chosen by randint the computer goes first, if anything else (e.g., 1) then the player starts. 
def whoGoesFirst():
    
    # We could double the player's odds of going first, if we change the range to (0,2) since anything not '0' would make the player go first.
    # This is the first step to display this string to the user once they select their letter.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

# To me it's odd to reference the list that we built above in the game board since we didn't actually put it all in a neat a tidy list. It saves code but still.
# The makemove function modifies the board list to be displayed later. 
def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # Checks if the player of computer has won by check if the board position matches the player/computer's letter in all winning conditions.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    #I don't understand how the code knows the change to bo and le.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the bottom ###Changed
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the top ###Changed
    (bo[7] == le and bo[4] == le and bo[1] == le) or # up the left side ###Changed
    (bo[8] == le and bo[5] == le and bo[2] == le) or # up the middle ###Changed
    (bo[9] == le and bo[6] == le and bo[3] == le) or # up the right side ###Changed
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal /
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal \

def getBoardCopy(board):
    # Make a copy of the board list (starts empty) and returns the updated board. append fucntion will allow moves to be updated.
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

#Defines a free space on the board as a " " to be used to check if the space can take a player/computer move.
def isSpaceFree(board, move):
    return board[move] == ' '

# Let the player type in their move.
# If a player does not type 1-9 then the loop repeats due to a short-circuit. 
# If the player types a number that does not have a freespace (defined above) then the loop repeats. 
#If the player types a valid number AND the space is free it changes the move to an integer. 
def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

# Returns a valid move from the passed list on the passed board.
def chooseRandomMoveFromList(board, movesList):
        
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
# Checks the number of things in the list possibleMoves. If it does not equal 0 then it will randomly choice one of the remaining options. 
# Thought: Would > 0 work?
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        # None is a special function that allows a loop to resolve neither true nor false.
        return None

#The 'AI' part
def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = '\u0001'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if computer can win in the next move
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    # Check if the player could win on their next move, and block them.
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print('Welcome to Tic Tac Toe!')

while True:
    # Show/Reset the Board
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
   #Starts the game offically.
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Player's turn.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            #Checks if player won.
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            #Checks if player did not win and the board is full.
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                #Starts Computer turn because the board is not full.
                else:
                    turn = 'computer'

        else:
            # Computer's turn.
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            #Checks if computer has won.
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            #Checks if the board is full.
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                #If board is not full then go back to player's turn code.
                else:
                    turn = 'player'

#If the game is completed and while loop is broken:
    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break
