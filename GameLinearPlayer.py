#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 18:41:00 2020

@author: gauravbhadra
"""


import time
#import random
import requests

def start_game():
    player = 1
    while True:
        move = 1
        
        next_player = requests.get('http://127.0.0.1:5000/game/state').json()['nextPlayer']
        if next_player == player:
            url = 'http://127.0.0.1:5000/game/registerMove?playerId=' + str(player) + '&move=' + str(move)
            resp = requests.get(url)
        
            if resp != 200: 
                move+=1
                # test the board        
        
        time.sleep(1)

if __name__ == '__main__':
    start_game()