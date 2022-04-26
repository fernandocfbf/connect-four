import math
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

    def _min(self, board, move, alpha, beta, depth, playerCode):
        '''
        input:
        output:
        description:
        '''
        if depth == 0:
            return random.randint(0, 10), move
        for mv in self.sucessors(playerCode, board):
            new_beta, new_move = self._max(board, mv, alpha, beta, depth-1, playerCode)
            if (new_beta < beta):
                beta = new_beta
                move = new_move
            if (beta <= alpha):
                break
        return beta, move
    
    def _max(self, board, move, alpha, beta, depth, playerCode):
        '''
        input:
        output:
        description:
        '''
        if depth == 0:
            return random.randint(0, 10), move
        for mv in self.sucessors(playerCode, board):
            new_alpha, new_move = self._min(board, mv, alpha, beta, depth-1, playerCode)
            if (new_alpha > alpha):
                alpha = new_alpha
                move = new_move
            if (alpha >= beta):
                break
        return alpha, move

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
        _, action = self._max(board, None, -math.inf, math.inf, playerCode, 1)
        return action
        
