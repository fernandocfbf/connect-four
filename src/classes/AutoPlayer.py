import math
import random
import copy
import numpy as np
from termcolor import colored

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

    def movement(self, player, board, column):
        result_board = np.matrix(board)
        for i in range(5,-2,-1):
            if (board[i,column] == 0):
                break
        if(i<0):
            return None
        result_board[i, column] = player
        return result_board

    def sucessors(self, playerCode, board):
        '''
        input: player code [int], game board [matriz (6 x 7)]
        output: all possible sucessors states [list]
        description: checks all possible next states for
            the game, and return in a list
        '''
        suc = []
        for i in range(0,7):
            b = self.movement(playerCode, board, i)
            if(b is not None):
                suc.append({'board':b, 'action':i})
        return suc

    def calculateScore(self, x, y, board, playerCode):
        round_positions = [ 
        [-1, -1],[0, -1],[1, -1],
        [-1,  0],        [1,  0],
        [-1,  1],[0,  1],[1,  1]
        ]

        score = 0
        for pos in round_positions:
            new_x = x + pos[0]
            new_y = y + pos[1]
            if (new_x >= 0 and new_x <= 6) and (new_y >= 0 and new_y <= 5):
                if int(board[x][y]) == playerCode:
                    if int(board[new_y][new_x]) == playerCode:
                        score += 1
                    elif int(board[new_y][new_x]) == self.getOpponentCode(playerCode):
                        score -= 1
        return score

    def calculateHeapMap(self, playerCode, board):
        heat_map = np.zeros((6,7))
        board_list = copy.deepcopy(board).tolist()
        board_score = 0
        for row in range(len(board_list)):
            for column in range(len(board_list[row])):
                heat_map[row][column] = self.calculateScore(row, column, board_list, playerCode)
        for row in heat_map:
            board_score += sum(row)
        return board_score

    def _max(self, board, move, alpha, beta, depth, playerCode):
        '''
        input:
        output:
        description:
        '''
        if depth == 0:
            return self.calculateHeapMap(playerCode, board), move
        for mv in self.sucessors(playerCode, board):
            new_alpha, new_move = self._min(mv["board"], mv["action"], alpha, beta, depth-1, playerCode)
            if (new_alpha > alpha):
                alpha = new_alpha
                move = new_move
            if (alpha >= beta):
                break
        return alpha, move
    
    def _min(self, board, move, alpha, beta, depth, playerCode):
        '''
        input:
        output:
        description:
        '''
        if depth == 0:
            return self.calculateHeapMap(playerCode, board), move
        for mv in self.sucessors(playerCode, board):
            new_beta, new_move = self._max(mv["board"], mv["action"], alpha, beta, depth-1, playerCode)
            if (new_beta < beta):
                beta = new_beta
                move = new_move
            if (beta <= alpha):
                break
        return beta, move

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
        _, action = self._max(board, None, -math.inf, math.inf, 5, playerCode)
        return action
        
