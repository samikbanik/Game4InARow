#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 19:26:16 2020

@author: gauravbhadra
"""
PLAYER = 1
DEPTH = 4

import time
#import random
import requests
from GameEngine import RowGame
from PrettyPrint import printMatrix

class MinimaxSolver:
    def __init__( self ):
        pass
    
    def undo( self, game, player, col ):
        game._unTrickleMove( player, col )
    
    def findNextMove( self, state ):
        '''
        inputs: 2D array of current state of the board
        return: int <1 to columns> the best possible next move
        '''
        COLUMNS = len(state[0])
        #odd levels will be max, even levels will be min 
        game = RowGame( COLUMNS, COLUMNS, 2, state )
        
        max_won = 0
        winning_col = 1
        
        for i in range(1, COLUMNS+1):
            #make the move. this is player 1's turn 
            self.game_won =False
            self.winner = None
        
            game.registerMove( 1, i )
            numWins = 0
            if game.getWinner() == 1:
                printMatrix( game.state )
                return i
            
            for j in range(1, COLUMNS+1):
                #make the move. this is player 0's turn 
                game.registerMove( 0, j )
                
                for k in range(1, COLUMNS+1):
                    #make the move. this is player 1's turn     
                    game.registerMove( 1, k )
                
                    for l in range(1, COLUMNS+1):
                        #make the move. this is player 0's turn     
                        game.registerMove( 0, l )

                        for m in range(1, COLUMNS+1):
                            #make the move. this is player 1's turn     
                            game.registerMove( 1, m )
                    
                            if game.getWinningStatus():
                                if game.getWinner() == 1:
                                    numWins += 1
                                else:
                                    numWins -= 1 
                                
                            self.undo( game, 1, m )
                            
                        self.undo( game, 0, l )
                        
                    self.undo( game, 1, k )
                    
                self.undo( game, 0, j ) 
                
            self.undo( game, 1, k )
            
            if numWins > max_won:
                max_won = numWins
                winning_col = i

            print(max_won, winning_col)                
        return winning_col
                

    
    # #player 1 is max
    # def max( self ):
    #     '''
    #     inputs: self.state

    #     Returns
    #     -------
    #     -1 = loss
    #     0  = indeterminate
    #     1  = win

    #     '''
        
        
       
    # #player 0 is min
    # def min( self ):
    #     '''
    #     inputs: self.state

    #     Returns
    #     -------
    #     -1 = win
    #     0  = indeterminate
    #     1  = loss
        
    #     '''
        
    #     minv = 2
        
        
        
        
    
    
def start_game( solver ):
    while True:
        current_state = requests.get('http://127.0.0.1:5000/game/state').json()
        next_player = current_state['nextPlayer']
        state = current_state['board']
        if next_player == PLAYER:
            move = solver.findNextMove( state )
            url = 'http://127.0.0.1:5000/game/registerMove?playerId=' + str(PLAYER) + '&move=' + str(move)
            resp = requests.get( url )
        
        time.sleep(1)

if __name__ == '__main__':
    
    solver = MinimaxSolver()
        