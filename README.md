# The Game

IJK is a sliding tile game played on a 4x4 board by two players, lowercase (also known as -) and uppercase (+). The players take turns, starting with uppercase. At the start of each turn, a tile labeled a is added randomly somewhere on the board if it is lowercase’s turn, and an A is added if it is uppercase’s turn. A player’s turn consists of making one of ﬁve possible moves: Up, Down, Left, Right, or Skip. Skip means nothing further happens and the player forfeits their turn. Otherwise, all tiles are slid in the direction that the player selected until there are no empty spaces left in that direction. Then, pairs of letters that are the same, of the same case, and adjacent to each other in the direction of the movement are combined together to create a single tile of the subsequent letter and the same case. For example, if an A slides down and hits another A, the two merge and become a single B. Similarly, pairs of B’s merge to become a single C, and so on. For pairs of letters that are the same but with opposite case, e.g. A and a, the tiles merge to become the letter B if it is uppercase’s turn, or b if it is lowercase’s turn. The game ends when a K or k appears on the board, and the player of that case wins the game.

## Other Important Details

The game has two speciﬁc variants. In Deterministic IJK, the new a or A at the beginning of each turn is added to a predictable empty position on the board (which is a function of the current board state). In Non-deterministic IJK, the new a or A is added to a random position on the board. The rest of the rules are the same for the two variants.

## How to run this code?

Your goal is to write AI clode that plays these two variants of IJK well. We’ve prepared skeleton code to help you. You can run the code like this:

./IJK.py [uppercase-player] [lowercase-player] [mode]

where uppercase-player and lowercase-player are each either ai or human, and mode is either det for deterministic IJK or nondet for nondeterministic IJK. These commands let you set up various types of games. For example, if you (a human) want to play a deterministic game against the ai, you could type:

./IJK.py human ai det

Similarly, you can set up games between AIs or between humans.

# The Program

This algorithm assumes that there are two players. Min and Max. Both the players alternate in turns. The Max moves first. The aim of max is to maximize a heuristic score and that of min is to minimize the same. For every player, a minimax value is computed. This value is the best achievable payoff against his play. The move with the optimum minimax value is chosen by the player.

Usually, the number of nodes to be explored by this algorithm is huge. In order to optimize it, pruning is used.

Here, the 6x6 grid with a randomly placed "A" or "a" is the initial scenario in non deterministic. In deterministic THe "a" or "A" is placed on first available empty cell (depending upon whose turn it is) as you iterate through (i,j) when i -> [0-5] and j -> [0,5] The computer player (MAX) makes the first move. This move is chosen by the minimax algorithm.


While using the minimax algorithm, the MIN and MAX uses his move (UP, DOWN, RIGHT and LEFT) for finding the possible children nodes. All available moves are evaluated and the best move (the one with maxUtility) is chosen as the next move.

## Heuristic Function

Before we talk about the heuristic we need to think about how to quantify the state of the board. We converted all the alphabets to numbers as shown in the lists below (matched by respective indexes).


    capitalList = [" ","A","B","C","D","E","F","G","H","I","J","K"]

    smallList = [" ", "a","b","c","d","e","f","g","h","i","j","k"]

    numberList = [1,10,20,30,40,50,60,70,80,90,100,110]



We use these converted values (numbers) to operate with huristic function.
We explored two types of heuristic functions. Smoothness and Monotonicity, we chose Monotonicity as it gave better results on longer runs. This was one of the important design decision we took.

**Smoothness heuristic:**

We want to keep adjacent tiles as close in value as possible, so we will give penalties for big differences between them, just to minimize it.

**Monotonicity heuristic:**

This heuristic tries to ensure that the values of the tiles are all either increasing or decreasing along both the left/right and up/down directions. It will typically prevent smaller valued tiles from getting orphaned and will keep the board very organized, with smaller tiles cascading in and filling up into the larger tiles.

[Reference for monotonicity](http://cs229.stanford.edu/proj2016/report/NieHouAn-AIPlays2048-report.pdf)

Based on observations and expertise, it is concluded that the game is heading in the positive direction if the highest valued tile is in the corner and the other tiles are linearly decreases as it moves away from the highest tile. Thus, there are four different best possibilities : Maximum tile is at the (1) Down -left (2) Top-left (3) Top-Right and (4) Down-Right corner. In order to compute the score, we can multiply the current configuration with a gradient (weighted) matrix associated with each of the possible cases. The gradient matrix designed for this case is as given.

    [[ 5, 4, 3, 2, 1, 0],[ 4, 3, 2, 1, 0, -1],[ 3, 2, 1, 0, -1, -2],[ 2, 1, 0, -1, -2, -3],[ 1, 0, -1, -2, -3, -4],[ 0, -1, -2, -3, -4, -5]], #top left

    [[ 0, 1, 2, 3, 4, 5],[ -1, 0, 1, 2, 3, 4],[ -2, -1, 0, 1, 2, 3],[ -3, -2, -1, 0, 1, 2],[ -4, -3, -2, -1, 0, 1],[ -5, -4, -3, -2, -1, 0]], #top right

    [[ 0, -1, -2, -3, -4, -5],[ 1, 0, -1, -2, -3, -4],[ 2, 1, 0, -1, -2, -3],[ 3, 2, 1, 0, -1, -2],[ 4, 3, 2, 1, 0, -1],[ 5, 4, 3, 2, 1, 0]], #bottom left

    [[ -5, -4, -3, -2, -1, 0],[ -4, -3, -2, -1, 0, 1],[ -3, -2, -1, -0, 1, 2],[ -2, -1, 0, 1, 2, 3],[ -1, 0, 1, 2, 3, 4],[ 0, 1, 2, 3, 4, 5]] #bottom right

The first element is when the highest score is at the top left, second is for top-right, then bottom-left and bottom-right. You can see that the number corresponding to the highest tile is always the largest and others decrease linearly in a monotonic fashion. The sides diagonal to it is always awarded the least score.


*The final score of the configuration is the maximum of the four products (Gradient * Configuration )*

We’ve created the Utility and Evaluation Function that is used by Minimax algorithm. Although the performance is good, the Minimax algorithm is so slow. To mend it, we use pruning to the algorithm. The pattern of the actions is same and it’s faster without using pruning. Even so, the Minimax Alpha Beta Pruning has its flaw. It can only consider and see the movement n (depth) turns onward that n needs to be small. If n is large, it will be computationally expensive to choose an action. We need some algorithm that consider further turns and need to be faster. Then n (depth) we used in our case was 6.

## How our program works?

Please note the values used in the description below are assumed values considered for explanation purpose. These are not the actual values of the output.

Initialize Alpha to -inf and Beta to Inf. Alpha will be updated if its in the Maximizer turn and Beta is update if its Minimizer turn. They will be passed to the child of the state/node.

Expand A (the initial state) possible action. It will produce B,C,D state. start from the first index (B)

It’s minimizer B turn. Expand B possible action, go into the child and check its score. Update Beta as minimum as possible. We will find Beta = 3 = min(3,12,8,inf). Alpha is still -inf.

It’s assumed that the depth is 2, return the minimum score (which is 3) to the A. Now it’s back to Maximizer turn A, update the Alpha = 3 = max(-inf,3). Then we go to C state/node, the second child:

Now go to state C, the minimizer turn C with the passed Alpha parameters 3. In C, we find that the first child’s score that the C found is 2. Update the Beta = 2 = min(inf,2). The maximizer has already found better move, which is scored at 3. So, don’t bother check another possible action in the C. This is the pruning process. Return the best score (it’s 2). To make it simpler if beta ≤ alpha then prune it.

Maximizer Turn A: calculate max(alpha, 2) = alpha. Check the last child C.

Minimizer Turn C : Calculate min(inf,14) , update beta to 14 and check if beta ≤ alpha (14 ≤ 3) and it’s not pruned. Calculate the next child. beta ≤ alpha (5 ≤ 3) and it’s not pruned. At last, check beta ≤ alpha (2 ≤ 3) it should be pruned. Since there are not any child after this node. No node that can be pruned. It can be pruned if the child that returned 2 is found at first. After this, return 2 to A.

Maximizer Turn A, calculate max(alpha,2) = alpha. Then it’s done. return 3 as best score that has been found in the tree.

## Folder Structure

**ai_IJK** : Implements the Minimax algorithm and chooses the next move the max Utility



**minimaxab** : Implements the Minimax algorithm with pruning (Depth limit is set as 6) for deterministic and Expectiminimax for non deterministic



**helper** : All utility functions created for this game are written here. This includes the eval function which evaluates the heuristic score for a given configuration

