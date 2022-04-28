import numpy as np
import datetime
from src.classes.RandomPlayer import RandomPlayer
from termcolor import colored

class FourInRowPop:

    def __init__(self, player1, player2):
        self.board = np.zeros( (6,7) )
        self.players = [player1, player2]
    
    def printSymbol(number):
        if number==1:
            return colored('●', 'yellow')
        elif number==2:
            return colored('■', 'red')
        else: 
            return ' '

    def printBoard(self): 
        for lin in range(0,6):
            for col in range(0,7):
                print(FourInRowPop.printSymbol(self.board[lin][col])+" | ", end='')
            print('')    
        print('\n')

    #
    # Only accepts player equal 1 or 2
    # and column between 0 and 6
    #
    def movement(self, player, column):
        print(column)
        try:
            if(player not in (1,2)):
                raise Exception('Only players 1 or 2')
            
            if column[0] == None: 
                # in this case the player is adding a new piece. 
                for i in range(5,-2,-1):
                    if (self.board[i,column[1]] == 0):
                        break
                if(i<0):
                    raise Exception('Player '+str(player)+', you can not play in a full column')
                self.board[i, column[1]] = player
            else:
                # the player is popping out a piece in column (column[1])
                if(self.board[5,column[1]] != player):
                    raise Exception('Player '+str(player)+', you can not pop out from an empty column nor pop out a piece that is not yours.')
                i = 5
                while (self.board[i,column[1]] != 0) and (i >= 1):
                    self.board[i,column[1]] = self.board[i-1, column[1]]
                    i = i - 1
                self.board[i-1,column[1]] == 0 

        except IndexError:
            raise Exception('Player '+str(player)+', you only can choose a column between 0 and 6')

    def endOfGame(self):
        # horizontally
        for i in range(6):
            current = None
            counter = 0
            for j in range(6):
                if ((self.board[i, j] in (1,2)) and (self.board[i, j] == self.board[i, j + 1])):
                    if (self.board[i, j]==current):
                        counter = counter + 1
                        current = self.board[i, j]
                    else:
                        counter = 1
                        current = self.board[i, j]
                else:
                    counter = 0
                if (counter==3):
                    return True
        # vertically
        for i in range(6):
            current=None
            counter = 0
            for j in range(5):
                if ((self.board[j, i] in (1,2)) and (self.board[j,i] == self.board[j+1,i])):
                    if(self.board[j,i]==current):
                        counter = counter + 1
                        current = self.board[j,i]
                    else:
                        counter = 1
                        current = self.board[j,i]
                else:
                    counter = 0
                if (counter == 3):
                    return True
        # "main" diagonal
        for k in range(-2,4):
            current = None
            counter = 0
            x = np.diag(self.board, k=k)
            for i in range(0,len(x)-1):
                if ((x[i] != 0) and (x[i] == x[i+1])):
                    if(x[i] == current):
                        counter = counter + 1
                        current = x[i]
                    else:
                        counter = 1
                        current = x[i]
                if (counter == 3):
                    return True
        # "anti" diagonal
        # [::-1] rotaciona as linhas da matriz
        temp = self.board[::-1]
        for k in range(-2,4):
            current = None
            counter = 0
            x = np.diag(temp, k=k)
            for i in range(0,len(x)-1):
                if ((x[i] != 0) and (x[i] == x[i+1])):
                    if(x[i] == current):
                        counter = counter + 1
                        current = x[i]
                    else:
                        counter = 1
                        current = x[i]
                if (counter == 3):
                    return True

        return False

    def isBoardFull(self):
        for lin in range(0,6):
            for col in range(0,7):
                if self.board[lin][col] == 0:
                    return False
        return True

    def game(self):
        k=1
        while ((not self.endOfGame()) != (self.isBoardFull())):
            k = (int)(not k)
            inicio = datetime.datetime.now()
            self.movement(k+1, self.players[k].move(k+1, self.board))
            dur = (datetime.datetime.now() -inicio).total_seconds()
            if(dur > 10):
                print('Player '+ self.players[k].name() + ' duration (seconds): '+ str(dur))
            self.printBoard()
        if self.endOfGame():
            if k+1 == 1:
                print(colored('Player number '+ str(k+1)+ ": " + self.players[k].name() + ' is the winner!', 'yellow'))
            else:
                print(colored('Player number '+ str(k+1)+ ": " + self.players[k].name() + ' is the winner!', 'red'))
            return self.players[k].name()
        else:
            print('It is a draw')
            return 'DRAW'

def main():
    #FourInRowPop(ManualPlayer(), RandomPlayer()).game()
    FourInRowPop(RandomPlayer(), RandomPlayer()).game()

if __name__ == '__main__':
    main()