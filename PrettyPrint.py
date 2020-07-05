#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 20:07:41 2020

@author: gauravbhadra
"""

from pandas import DataFrame

def printMatrix( matrix ):
    print('\n\n')
    if type(matrix) == list and len(matrix) >= 1 and type(matrix[0]) == list:
        df = DataFrame( matrix )
        df.replace(-1, '.', True)
        print( df )
    else:
        print( matrix )
        
    print('\n\n')