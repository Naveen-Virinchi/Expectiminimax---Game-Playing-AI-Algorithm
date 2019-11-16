
from helper import *
import numpy as np
import time
import ai_IJK


#Returns the maximum value of the utility function
def MinimaxAB(board, node="+", deterministic = True):

	valid_nodes = ("+","-","c")
	if node not in valid_nodes:
		raise ValueError("Ivalid node argument - Valid inputs + , - , c")

	limit = 6
	start = time.clock()

	if deterministic:
		if node=="+":
			return Maximize(board=board, alpha=-np.inf, beta=np.inf, depth=limit, start=start)
		else:
			return Minimize(board=board,  alpha=-np.inf, beta=np.inf, depth=limit, start=start)

	else:
		if node=="+":
			return Maximize(board=board, alpha=-np.inf, beta=np.inf, depth=limit, start=start)
		elif node=="-":
			return Minimize(board=board,  alpha=-np.inf, beta=np.inf, depth=limit, start=start)
		else:
			return ExpectiMinimax(board=board,  alpha=-np.inf, beta=np.inf, depth=limit, start=start)


#Finds the largest utility for the Max Player
def Maximize(board, alpha, beta, depth, start):
	if board.isGameFull() or depth==0 or (time.clock()-start)>0.06:
		return Evaluate(board) # check Helper for Evaluateuation function

	maxUtility = -np.inf

	#The children for the Max player are the neighboring tiles
	for child in children(board):
		maxUtility = max(maxUtility, Minimize(board=child, alpha=alpha, beta=beta, depth=depth-1, start=start))

		if maxUtility >= beta: #pruning
			break

		alpha = max(maxUtility, alpha) #setting alpha from pruning in minimization step

	return maxUtility


#Finds the smallest utility for the Min Player
def Minimize(board, alpha, beta, depth, start):
	if board.isGameFull()  or depth==0 or (time.clock()-start)>0.06:
		return Evaluate(board)

	minUtility = np.inf

	#The children for the Min player include all random tile possibilities for the current state
	for child in children(board):
		minUtility = min(minUtility, Maximize(board=child,  alpha=alpha, beta=beta, depth=depth-1, start= start))

		if minUtility <= alpha: #pruning
			break

		beta = min(minUtility, beta) #setting beta from pruning in maximization step

	return minUtility


#Finds the average of utility for the child Player(Computer playing the game)
def ExpectiMinimax(board, alpha, beta, depth, start):
	if board.isGameFull() or depth==0 or (time.clock()-start)>0.06:
		return Evaluate(board) # check Helper for Evaluateuation function

	maxUtility = 0

	#The children for the Max player are the neighboring tiles
	for child in children(board):
		maxUtility = maxUtility + ((1/len(children(board))) * MinimaxAB(board=child, node=ai_IJK.player, deterministic=ai_IJK.deterministic))

	return maxUtility