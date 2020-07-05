#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 19:36:17 2020

@author: gauravbhadra
"""

import unittest
from GameMinimax import MinimaxSolver
from PrettyPrint import printMatrix

class MinimaxSolverTests(unittest.TestCase):
    def setUp( self ):
        self.solver = MinimaxSolver()
        self.state = [
            
                                [ -1, -1, -1, -1, -1,    -1, -1, -1, -1, -1 ],
                                [ -1, -1, -1, -1, -1,    -1, -1, -1, -1, -1 ],
                                [ -1, -1, -1, -1, -1,    -1, -1, -1, -1, -1 ],
                                [ -1, -1, -1, -1, -1,    -1, -1, -1, -1, -1 ],
                                [ -1, -1, -1, -1, -1,    -1, -1, -1, -1, -1 ],
                                [ -1, -1, -1, -1, -1,    -1, -1, -1, -1, -1 ],
                                [ -1, -1, -1, -1, -1,     -1, -1, -1, -1, -1 ],
                                [ -1, -1, -1,  1,  0,     -1, -1, -1, -1, -1 ],
                                [ -1, -1,  1,  0,  1,     -1, -1, -1, -1, -1 ],
                                [ -1,  1,  0,  0,  0,     -1, -1, -1, -1, -1 ],
                            ]
    def test__checkIfWon( self ):
        returnValue = self.solver.findNextMove( self.state)
        #print(1)
        printMatrix( self.state )
        print(returnValue)
        #self.assertEqual( returnValue, True )
    
if __name__ == '__main__':
    unittest.main()
