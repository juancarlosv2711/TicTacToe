'''
Created on 15 Jun 2019

@author: juanvelasquez
'''
"""Tic Tac Toe."""

position = "global"

def main():
    """Default Constructor."""
    positionarray()
    players = startgame()
    dinamics(players[0], players[1])

def boardempty():
    """Board is empty."""
    print('    (0) (1) (2)')
    print(' (0)   |   |   ')
    print('    -----------')
    print(' (1)   |   |   ')
    print('    -----------')
    print(' (2)   |   |   ')
    

def makingboard():
    """Pulling board together."""
    board = ""
    
    board = boardcolumn() + '\n'
    for rowboard in range(3): #going down each row
        if rowboard < 2:
            board += boardrow(rowboard)
            board += horizontal(rowboard) + "\n"
            board += divisionline()
        else:
            board += boardrow(rowboard)
            board += horizontal(rowboard)
        board += "\n"
    print(board) 
def horizontal(row):
    """Horizontal on the board."""
    board = ""
    for x in range(3): #going horizontal 'x' means each horizontal space
        if x < 2:
            print(mark(position[row][x]))
            board += mark(position[row][x]) + "|"
        else:
            board += mark(position[row][x])
    
    return board

def boardcolumn():
    """Making top board."""
    columnumber = "   "
    for column in range(1,4):
        columnumber += ' ({})' .format(column)
    
    return columnumber
        
def boardrow(numrow):
    """Making row numbers."""
    numrow += 1
    row = '({})' .format(numrow)
    numrow = numrow + 1
    return row


def mark(position):
    """Inserting mark on the board
        position = 0 spot is free
        position = X spot is played by x player
        position = O spot has been played by 0 player."""
    stringreturn = ""
    if position == 0:
        stringreturn = "   "
        return stringreturn
    elif position == 'X':
        stringreturn = ' X '
        return stringreturn
    elif position == 'O':
        stringreturn = ' O '
        return stringreturn

def positionarray():
    """Initilalizing position array."""
    
    global position
    position = [[0 for column in range(3)] for row in range(3)]
   

def divisionline():
    """Line division."""
    line = "    -----------"
    return line


def startgame():
    """Start of the game."""
    #variables
    flag = True
    playerOne = ""
    playerTwo = ""
    
    print('TicTacToe Game!!!')
    
    while (flag):
        playerOne = input('Player One = select (X) or (O) to select your mark: ').upper()
        if playerOne == 'O':
            playerTwo = 'X'
            flag = False
        elif playerOne == 'X':
            playerTwo = 'O'
            flag = False
        else:
            print('Please enter just X or O!!!')
            
    print('Great!!! Player one has selected {} and Player Two will be the mark {}'.format(playerOne, playerTwo))
    input('Press enter to start the game')
    players = [playerOne, playerTwo]
    return players
    
def dinamics(playerOne, playerTwo):
    """Rounds of the game.""" 
    #variables
    flag = True
    flagtwo = True
    flagthree = True
    while(flag):
        counter = 1
        print('Round {}!!!'.format(counter))
        makingboard()
        while(flagtwo):
            print('Player one choose coordinates')
            coordinaterow = int(input('Row number'))
            coordinatecolumn = int(input('Column number'))
            info = validatingcoordinates(coordinaterow, coordinatecolumn, playerOne)
            if info == 1:
                flagthree = True
                flagtwo = False
            elif info == 0:
                print('Position has been played already choose a different coordinate')
                flagtwo = True
            else:
                print('Choose a coordinate within the board')
                flagtwo = True
        makingboard()
        while(flagthree):
            print('Player two choose coordinates')
            coordinaterow = int(input('Row number'))
            coordinatecolumn = int(input('Column number'))
            info = validatingcoordinates(coordinaterow, coordinatecolumn, playerTwo)
            if info == 1:
                flagtwo = True
                flagthree = False
            elif info == 0:
                print('Position has been played already choose a different coordinate')
                flagtwo = True
            else:
                print('Choose a coordinate within the board')
                flagtwo = True
        makingboard()
         
def validatingcoordinates(row, column, marker):
    """checking coordinate is within game frame."""
    
    row = row - 1
    column = column - 1
    if row <= 2 and column <= 2:
        if position[row][column] == 0:
            position[row][column] = marker
            return 1 #succesfull
        else:
            return 0 #position has been played
    else:
        return 2 #out of bundaries
    
main()
    