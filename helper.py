
import copy

# Return All Available Moves
def getAvailableMoves(game, dirs = ['U','L','D','R']):
	availableMoves = []

	for x in dirs:
		gameCopy = copy.deepcopy(game)
		if gameCopy.makeMove(x):
			availableMoves.append(x)

	return availableMoves

#Gets the Child of a node in a particular direction
def getChild(game, dir):
	temp = copy.deepcopy(game)
	temp.makeMove(dir)
	return temp

#Gets all the Children of a node
def children(board):
	children = []
	for move in getAvailableMoves(board):
		children.append(getChild(board, move))
	return children

#converts alphabets into numbers to do numeric calculation
def convertBoard(board):
	capitalList = [" ","A","B","C","D","E","F","G","H","I","J","K"]
	smallList = [" ", "a","b","c","d","e","f","g","h","i","j","k"]
	numberList = [1,10,20,30,40,50,60,70,80,90,100,110]

	listBoard = numBoard = list(board.getGame())

	for i in range(6): #converting the board to numbers by matching index
		for j in range(6):
			try:
				numBoard[i][j] = numberList[capitalList.index(listBoard[i][j])]
			except ValueError:
				try:
					numBoard[i][j] = numberList[smallList.index(listBoard[i][j])]
				except ValueError:
					raise ValueError

	return(numBoard)

#Evaluates the heuristic. The heuristic used here is a gradient function
def Evaluate(board):
	import math
	import numpy as np

	if board.isGameFull():
		return -np.inf

	monotonicWeights =  [
						[[ 5, 4, 3, 2, 1, 0],[ 4, 3, 2, 1, 0, -1],[ 3, 2, 1, 0, -1, -2],[ 2, 1, 0, -1, -2, -3],[ 1, 0, -1, -2, -3, -4],[ 0, -1, -2, -3, -4, -5]], #top left
						[[ 0, 1, 2, 3, 4, 5],[ -1, 0, 1, 2, 3, 4],[ -2, -1, 0, 1, 2, 3],[ -3, -2, -1, 0, 1, 2],[ -4, -3, -2, -1, 0, 1],[ -5, -4, -3, -2, -1, 0]], #top right
						[[ 0, -1, -2, -3, -4, -5],[ 1, 0, -1, -2, -3, -4],[ 2, 1, 0, -1, -2, -3],[ 3, 2, 1, 0, -1, -2],[ 4, 3, 2, 1, 0, -1],[ 5, 4, 3, 2, 1, 0]], #bottom left
						[[ -5, -4, -3, -2, -1, 0],[ -4, -3, -2, -1, 0, 1],[ -3, -2, -1, -0, 1, 2],[ -2, -1, 0, 1, 2, 3],[ -1, 0, 1, 2, 3, 4],[ 0, 1, 2, 3, 4, 5]] #bottom right
						]

	values = [0,0,0,0]

	for i in range(4):
		for x in range(6):
			for y in range(6):
				values[i] += int(monotonicWeights[i][x][y]) * int(convertBoard(board)[x][y])


	return max(values)


