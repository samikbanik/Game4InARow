#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 23:51:12 2020

@author: gauravbhadra
"""
import unittest
from GameEngine import RowGame


class GameEngineTests(unittest.TestCase):
    def setUp( self ):
        self.sampleGame = RowGame(6, 5, 2)
        
        self.sampleGame.state = [
                                [ -1, -1, -1, -1, -1 ],
                                [ -1, -1, -1, -1, -1 ],
                                [ -1, -1, -1, -1, 1 ],
                                [ -1, -1, -1, 1, -1 ],
                                [ -1, -1, 1, -1, -1 ],
                                [ -1, 1, -1, -1, -1 ],
                            ]
    def test__checkIfWon( self ):
        returnValue = self.sampleGame._checkIfWon(2, 4)
        
        self.assertEqual( returnValue, True )
    
if __name__ == '__main__':
    unittest.main()