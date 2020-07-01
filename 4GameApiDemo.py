#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 11:53:11 2020

@author: gauravbhadra
"""

'''
http://127.0.0.1:5000/game/registerMove?playerId=1&move=2

http://127.0.0.1:5000/game/state

http://127.0.0.1:5000/game/reset
'''
import time
import random
import requests

def start_game():
    player = 0
    while True:
        move = random.randint(1,10)
        #make move
        url = 'http://127.0.0.1:5000/game/registerMove?playerId=' + str(player) + '&move=' + str(move)
        resp = requests.get(url)
        print(resp)
        
        # test the board
        #url = 'http://127.0.0.1:5000/game/state'
        #resp = requests.get(url)
        #print(resp)
        
        
        time.sleep(2)
        player = player ^ 1
        
        

if __name__ == '__main__':
    start_game()