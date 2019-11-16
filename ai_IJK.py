#!/usr/local/bin/python3

"""
This is where you should write your AI code!

Authors:  Naveen Virincheepuram/ naviri, Cale Erin/ cnearing, Leah Scherschel/ llschers

Based on skeleton code by Abhilash Kuhikar, October 2019
"""

import random
import numpy as np
from helper import *
from minimaxab import *
from logic_IJK import Game_IJK

# Suggests next move to be played by the current player given the current game
#
# inputs:
#     game : Current state of the game
#
# This function should analyze the current state of the game and determine the
# best move for the current player. It should then call "yield" on that move.

def next_move(game: Game_IJK)-> None:

	'''board: list of list of strings -> current state of the game
	   current_player: int -> player who will make the next move either ('+') or -'-')
	   deterministic: bool -> either True or False, indicating whether the game is deterministic or not
	'''

	board = game.getGame()
	player = game.getCurrentPlayer()
	deterministic = game.getDeterministic()

	moves = getAvailableMoves(game)
	maxUtility = -np.inf
	nextMove = -1

	for move in moves:
		child = getChild(game, move)
		utility = MinimaxAB(board=child, node=player, deterministic=deterministic)

		if utility >= maxUtility:
		   maxUtility = utility
		   nextMove = move

	yield nextMove
