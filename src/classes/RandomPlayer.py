from random import randint
from src.classes.Player import Player

class RandomPlayer(Player):

    def isPossibleMove(self, board, column):
        '''
        input: game board [matriz (6 x 7)]
        output: boolean
        description: check if the column is 
            not full and the column is 
            inside the board
        '''
        isFullColumn = board[0][column] != 0
        insideBoard = column < 7 and column >=0
        return insideBoard and not(isFullColumn) 

    def name(self):
        return "Random"

    def move(self, player_code, board):
        isPossible = False
        while not(isPossible):
            number = randint(0, 6) 
            isPossible = self.isPossibleMove(board, number)
        return number


