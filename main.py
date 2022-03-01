#Matthew Stauffer
#Sports Analysis
#To do:
#Create file reading system
#Create model/write code to do the math
#Add data file
import numpy as np
import pandas as pd
#The order will be Nick, Andrew, Jason, Dennis, Joey, then Tyler
gameMatrix=np.array(
    [1,-1,0,0,0,0],[0,0,1,-1,0,0],[0,0,0,0,1,-1], #Round 1
    [0,-1,1,0,0,0],[0,0,0,1,0,-1],[-1,0,0,0,1,0], #Round 2
    [1,0,0,0,0,-1],[0,0,-1,0,1,0],[0,1,0,-1,0,0], #Round 3
    [0,-1,0,0,1,0],[0,0,1,0,0,-1],[-1,0,1,0,0,0], #Round 4
    [1,0,-1,0,0,0],[0,1,0,0,0,-1],[0,0,0,1,-1,0], #Round 5
    [-1,1,0,0,0,0],[0,0,-1,1,0,0],[0,0,0,0,1,-1], #Round 6
    [0,1,-1,0,0,0],[0,0,0,1,0,-1],[-1,0,0,0,1,0], #Round 7
    [1,0,0,0,0,-1],[0,0,-1,0,1,0],[0,1,0,-1,0,0], #Round 8
    [0,-1,0,0,1,0],[0,0,-1,0,0,1],[-1,0,0,1,0,0], #Round 9
    [-1,0,1,0,0,0], #Round 10
    [1,0,-1,0,0,0] #Tiebreaker
    )
scoreMatrix=np.array(
    [1],[8],[2], #Round 1
    [4],[2],[3], #Round 2
    [2],[3],[5], #Round 3
    [2],[2],[2], #Round 4
    [1],[10],[6], #Round 5
    [1],[1],[5], #Round  6
    [6],[6],[10], #Round 7
    [9],[1],[1], #Round 8
    [14],[1],[10], #Round 9
    [1], #Round 10
    [3] #Tiebreaker
    )
aTranspose=np.transpose(gameMatrix)
#The formula which we will be using will be A'Ax=A'b, where A'A is a matrix M, and A'b is a matrix D.
D = np.multiply(aTranspose, scoreMatrix)
M = np.multiply(aTranspose, gameMatrix)