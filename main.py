#Matthew Stauffer
#Sports Analysis
#To do:
#Create file reading system
#Create model/write code to do the math
#Add data file
import numpy as np
import pandas as pd
#The order will be Nick, Andrew, Jason, Dennis, Joey, then Tyler
names = ["Nick", "Andrew", "Jason", "Dennis", "Joey", "Tyler"]
gameMatrix=np.matrix([
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
    ])
scoreMatrix=np.matrix([
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
    ])
aTranspose=np.transpose(gameMatrix)
#The formula which we will be using will be A'Ax=A'b, where A'A is a matrix M, and A'b is a matrix D.
D = np.matmul(aTranspose, scoreMatrix)
M = np.matmul(aTranspose, gameMatrix)

#Here we create copies of the matricies for later usage.
copyOfD = np.matrix.copy(D)
copyOfM = np.matrix.copy(M)

#Now we apply the massey method, where we exchange the last in M for all 1s, and the last entry in D as 0.
for i in range(6):
    M[5,i]=1
D[5,0]=0

#Finally now we can solve and find our team rankings. 
teamRankings=np.matmul(np.linalg.inv(M),D)
#We squeeze and convert to an array to easily extract the rankings.
teamRankings = np.squeeze(np.asarray(teamRankings))

for i in range(6):
    print("%s's rank is %f" % (names[i],teamRankings[i]))