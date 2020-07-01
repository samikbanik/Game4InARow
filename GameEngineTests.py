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
        sampleGame = RowGame(5, 5, 2)
        
        sampleGame.state = [
                                [ -1, -1, -1, -1, -1 ],
                                [ -1, -1, -1, -1, -1 ],
                                [ -1, 0, -1, -1, -1 ],
                                [ -1, 0, -1, -1, -1 ],
                                [ -1, 0, -1, -1, -1 ],
                                [ -1, 0, -1, -1, -1 ],
                            ]
    
if __name__ == '__main__':
    unittest.main()