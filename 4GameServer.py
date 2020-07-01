#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 11:34:15 2020

@author: gauravbhadra
"""

import logging
import flask
from GameEngine import RowGame
from flask import request, jsonify, Blueprint
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

NUM_COLS = 10
NUM_ROWS = 10
NUM_PLAYERS = 2

thisGame = RowGame( x = NUM_ROWS, y = NUM_COLS, players = NUM_PLAYERS)

DEFAULT_RET = """<h1>4 in a Row Game API</h1>
             <p>/game/state to get status </p>
             <p>/game/registerMove?playerId=1&move=2 </p>"""

@app.route('/', methods=['GET'])
def home():
    return 

@app.route('/game', methods=['GET'])
def game():
    return thisGame.getState()


@app.route('/game/state', methods=['GET'])
def getState():
    return_json = {}
    return_json['isWon'] = thisGame.getWinningStatus()
    return_json['board'] = thisGame.getState()
    if return_json['isWon']:
        return_json['winner'] = thisGame.getWinner()
        return_json['nextPlayer'] = None
    else:
        return_json['winner'] = None
        return_json['nextPlayer'] = thisGame.getNextPlayer()
        
    return jsonify( return_json )



@app.route('/game/registerMove', methods=['GET'])
def registerMove():
    if 'playerId' in request.args and 'move' in request.args:
        playerId = int(request.args['playerId'])
        move = int(request.args['move'])
        logging.info('Player:', playerId, ' made move:', str(move))        
        thisGame.registerMove( playerId, move )
        
        return "Move made successfully"
    else:
        logging.error("Player info or move not provided")
        return "ERROR: Please provide player info and move"            

        
        
        
errors = Blueprint('errors', __name__)
        
@errors.app_errorhandler(Exception)
def handle_error(error):
    message = [str(x) for x in error.args]
    status_code = error.status_code
    success = False
    response = {
        'success': success,
        'error': {
            'type': error.__class__.__name__,
            'message': message
        }
    }

    return jsonify(response), status_code
@app.route('/game/reset', methods=['GET'])
def refresh():
    try:
        thisGame.resetGame( x = NUM_ROWS, y = NUM_COLS, players = NUM_PLAYERS)
        return "Game reset successfully"
    except:
        return "ERROR: could not reset the game"    


app.run()

'''
cd Downloads
./ngrok http 5000
'''