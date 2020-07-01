#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 20:09:07 2020

@author: gauravbhadra
"""

TARGET = 4

class RowGame: 
    def __init__( self, x, y, players):
        '''
        board is represented by a n * n matrix, where the it is stored graphically
        
        rounds is a list of lists which stores the history of the game, 
        round [3]: []
        '''
        assert x >= 5, "Rows cannot be less than 5"
        assert y >= 5, "Columns cannot be less than 5"
        
        assert players >= 2, "Cannot play with less than 2 players"
        
        self.rows = x
        self.columns = y
        self.state = [[-1 for _ in range( self.columns )] for _ in range( self.rows ) ] 
        self.roundNumber = 0 
        self.nextPlayer = 0
        self.players = players
        self.rounds = []
        self.game_won =False
        self.winner = None

        
    def getGameHistory( self ):
        return self.rounds
        
    
    def getNextPlayer( self ):
        return self.nextPlayer
    
    def getState( self ):
        return self.state
    
    def getWinningStatus( self ):
        return self.game_won
    
    def getWinner( self ):
        return self.winner
    
    def resetGame( self, x, y, players ):
        self.__init__( x, y, players)
        
    def checkFinished( self ):
        return (self.game_won, self.winner) 
        
        
    
    def _validateMove( self, col_num ):
        return self.state[0][col_num -1] == -1 and self._checkWithinBounds(0, col_num-1)
    
    def _trickleMove( self, player, col_num):
        row = 0
        while(row < self.rows and self.state[row][col_num-1] == -1):
            row+=1
        row-=1
        self.state[row][col_num -1] = player
        return row
        
        
    def _checkWithinBounds( self, row_num, col_num):
        '''
        Helper method to check if row_num and col_num are inside the board
        '''
        if row_num < 0 or row_num >= self.rows:
            return False
        if col_num < 0 or col_num >= self.columns:
            return False
        return True
    
    def _checkIfWon( self, row_num, col_num):
        if self.state[row_num][col_num] == -1:
            return False
    
            
        def _checkTarget( count, currentVal ):
            if currentVal == -1:
                return False
            
            if count == TARGET:
                self.winner = currentVal
                self.game_won = True
                return True
            return False
                
        #check that row 
        count = 0
        currentVal = self.state[row_num][0]
        for c in range(self.columns):
            if self.state[row_num][c] == currentVal:
                count +=1
                if _checkTarget(count, currentVal ):
                    return True
            else:
                count = 1
                currentVal = self.state[row_num][c]
        
        
        # check that column
        count = 0
        currentVal = self.state[0][col_num]
        for r in range(self.rows):
            if self.state[r][col_num] == currentVal:
                count +=1
                if _checkTarget(count, currentVal ):
                    return True
            else:
                count = 1
                currentVal = self.state[r][col_num]
        
        
        #check opp diag
        currentVal = self.state[row_num][col_num] 
        count = 1

        i = 1
        while self._checkWithinBounds(row_num + i, col_num + i) and self.state[row_num + i][col_num + i] == currentVal:
            count += 1
            i+=1
                        
        i = -1
        while self._checkWithinBounds(row_num + i, col_num + i) and self.state[row_num + i][col_num + i] == currentVal:
            count += 1
            i-=1
                                   
        if _checkTarget(count, currentVal ):
            return True
        

        #check leading diag        
        currentVal = self.state[row_num][col_num] 
        count = 1

        i = 1
        while self._checkWithinBounds(row_num - i, col_num + i) and self.state[row_num - i][col_num + i] == currentVal:
            count += 1
            i+=1
            
            
        i = -1
        while self._checkWithinBounds(row_num - i, col_num + i) and self.state[row_num - i][col_num + i] == currentVal:
            count += 1
            i-=1
            
                       
        if _checkTarget(count, currentVal ):
            return True
                
                
        return False
    
            
    def _checkIfGameDrawn( self ):
        '''
        Helper method to check if the game is inconclusive
        Currently checks top row ot see if no more moves are permitted
        TODO: Implement smarter logic to see if game can still be won to highlight this faster
        '''
        for i in range(self.columns):
            if self.state[0][i] == -1:
                return False
        return True
            
    
    def registerMove( self, player, col_num):
        assert self.nextPlayer == player, "Not the player's turn; Expected Player:" + str(self.nextPlayer) + "Player played: " + str(player)
        
        assert self._validateMove( col_num ), "Not  Valid move"
        
        assert not self.game_won, "Game already completed"
        
        row_num = self._trickleMove(  player, col_num)
        
        self._saveInHistory( player, col_num )
        # change player 
        self.nextPlayer = self.nextPlayer ^ 1

        
        if self.nextPlayer == 0:
            self.roundNumber += 1 
            
        self._checkIfWon( row_num, col_num)
        self._checkIfGameDrawn()
            
        
    def _saveInHistory( self, player, move_row ):
        if player == 0:
            self.rounds.append([move_row])
        else: 
            self.rounds[-1].append(move_row)
        

'''  
if __name__  == '__main__':
    runcell(0, '/Users/gauravbhadra/spyder_bk/GameEngine.py')
    g = RowGame( 6, 6, 2)
    
    g.registerMove( 0, 2)

''' 
    
    