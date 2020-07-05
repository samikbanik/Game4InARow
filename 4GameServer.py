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


def getGameMetrics():
    return_json = {}
    return_json['isWon'] = thisGame.getWinningStatus()
    return_json['board'] = thisGame.getState()
    if return_json['isWon']:
        return_json['winner'] = thisGame.getWinner()
        return_json['nextPlayer'] = None
        return_json['nextMoveNumber'] = None
    else:
        return_json['winner'] = None
        return_json['nextPlayer'] = thisGame.getNextPlayer()
        return_json['nextMoveNumber'] = thisGame.getNextMoveNumber()
        
    return return_json

@app.route('/game/state', methods=['GET'])
def getState():
    return jsonify( getGameMetrics() )


def checkWinningStatus():    
    return_json = {}
    if thisGame.getWinningStatus():
        return_json[ 'status' ] = 400
        return_json[ 'error' ] = "Game already won"
        return jsonify( return_json )
    return (thisGame.getWinningStatus(),  return_json)
           
           
def checkCorrectPlayer( player ):
    return_json = {}
    if thisGame.getNextPlayer() != player:
        return_json[ 'status' ] = 400
        return_json[ 'error' ] = "Not player:" + str(player) + "'s turn"
        return jsonify( return_json )
    return (thisGame.getNextPlayer() == player,  return_json)


@app.route('/game/registerMove', methods=['GET'])
def registerMove():
    return_json = {}
    try:
        if 'playerId' in request.args and 'move' in request.args:
            playerId = int(request.args['playerId'])
            #check winning status
            status  = checkWinningStatus() 
            if status[0]:
                return jsonify( status[1] )
            
            #check player's turn                                    
            status  = checkCorrectPlayer( playerId )                        
            if not status[0]:
                return jsonify( status[1] )
            
            
            move = int(request.args['move'])
            logging.info('Player:', playerId, ' made move:', str(move))        
            thisGame.registerMove( playerId, move )
            
            #TODO: gaurav.bhadra: make the json: and refactor
            return jsonify( getGameMetrics() )
        else:
            return_json = {}
            logging.error("Player info or move not provided")
            return_json[ 'status' ] = 400
            return_json[ 'error' ] = "Player info or move not provided"
            return jsonify( return_json )
    except Exception as e:
        return_json = {}
        return_json[ 'status' ] = 400
        return_json[ 'error' ] = str(e)
        return jsonify( return_json )
        
        
        
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
        return jsonify( getGameMetrics() )
    except Exception as e:
        return_json = {}
        return_json[ 'status' ] = 400
        return_json[ 'error' ] = str(e)
        return jsonify( return_json )  


app.run()

'''
cd Downloads
./ngrok http 5000
'''