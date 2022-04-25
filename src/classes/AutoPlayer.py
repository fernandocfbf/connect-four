import random

from src.classes.Player import Player

class AutoPlayer(Player):

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
    
    def getOpponentCode(self, playerCode):
        '''
        input: player code [int]
        output: opponent code [int]
        description: creturn the opponent code [int]
        '''
        if playerCode == 1:
            return 2
        return 1

    def sucessors(self, playerCode, board):
        '''
        input: player code [int], game board [matriz (6 x 7)]
        output: all possible sucessors states [list]
        description: checks all possible next states for
            the game, and return in a list
        '''
        res = list()
        for column in range(0, 7):
            check = self.isPossibleMove(board, column)
            if check:
                res.append(column)
        return res

    def _min(self, move):
        return -1
    
    def _max(self, move):
        return 1

    def minimax(self, board, depth):
        '''
        input
        output:
        description:
        '''
        alpha, beta, action = None
        for move in self.sucessors(board):
            move_score = self._min(move)

            if alpha == None:
                alpha = move
                action = move_score

            elif move_score > alpha:
                alpha = move
                action = move_score
        return action

    #@Override
    def name(self):
        '''
        input: 
        output: string
        description: returns player name
        '''
        return "AutoPlayer"
    
    #@Override
    def move(self, playerCode, board):
        isPossible = False
        while not(isPossible):
            number = random.randint(0, 6) 
            isPossible = self.isPossibleMove(board, number)
        return number

        
