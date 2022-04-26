import math
import random
import copy
import numpy as np
from termcolor import colored

from pyparsing import col

from src.classes.Player import Player

class AutoPlayer(Player):

    def __init__(self, co):
        self.co = co

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

    def printSymbol(self, number):
        if number==1:
            return colored('●', 'yellow')
        elif number==2:
            return colored('■', 'red')
        else: 
            return ' '

    def printBoard(self, board): 
        for lin in range(0,6):
            for col in range(0,7):
                print(self.printSymbol(board[lin][col])+" | ", end='')
            print('')    
        print('\n')

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


    def eval(self, playerCode, board):
        heat_map = np.zeros( (6,7) )
        board_score = 0
        for row in range(len(board)):
            for column in range(len(board[row])):
                heat_map[row][column] = self.calculateScore(row, column, board, playerCode)
        for row in heat_map:
            board_score += sum(row)
        
        print("BOARD")
        self.printBoard(board)
        print("SCORE -> ", board_score)

        return board_score

    def _min(self, board, move, alpha, beta, depth, playerCode):
        '''
        input:
        output:
        description:
        '''
        if depth == 0:
            return self.eval(playerCode, board), move
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
        if self.co < 2:
            isPossible = False
            while not(isPossible):
                number = random.randint(0, 6) 
                isPossible = self.isPossibleMove(board, number)
            self.co += 1
            return number
        _, action = self._max(board, None, -math.inf, math.inf, 5, playerCode)
        return action
        
