# SportsAnalysis
## What are we doing?
We will be using Kenneth Massey's method of ranking teams. This method is currently being used by the Bowl Championship Series. 
## Why are we doing this?
Because it's fun. 
Also we prefer to use Massey's method because it can take many different features into account (things like home court advantage, injuries, etc.) as well as teams playing multiple games against eachother. 
## How are we doing this?
We are doing this by using Python. We will be using Numpy for the linear algebra, as well as other libraries for data entry/collection.
## Goals
I would want to use a full regular season as data, and then use the model to "predict"/weigh the winners of the playoff games individually (and by how much). 
## What data set will we use?
I am going to be using the Dinger City Winter 2022 season for my dataset. I chose this because mario superstar baseball is amazing and also its current.
Here is a link to a playlist containing all of the games. [Here is a Playlist](https://youtube.com/playlist?list=PL4KAbBInKJ-yDgWyqkUlH4Yyk1n6STYka)
We will be using only the regular season, including the tiebreaker game. 
### How is the data set up?
So we create a numpy matrix (gameMatrix), each game is represented by a row. The two teams play each other, and the winning team is represented by a 1, and a losing team is represented by a -1. The score is also recorded in a column matrix (scoreMatrix). 
After creating our matrix and including all of the games (regular season and tiebreaker), you begin to find the least squares solution by multiplying Game Matrix Transposed and Game Matrix (M). We then multiply our score matrix by the transpose of the game matrix (D). 
Finally we change the last row of M to be all 1s, and the final entry of D to be 0. Then we solve taking the inverse of M and multiplying it by D to get our answer. 
### Why did you just use score?
One of the good things about this model is that the score function can be "adjusted" to where it isn't just the score that matters. It can take home field advantage into account, to name one specific thing. I didn't include anything like this because the stages add an extra element of randomness, so some home stages would result in more varied outcomes than others (Mario Stadium being the least random). As well as that the members of the league all played ONLY on Mario Stadium for multiple seasons in a row, with this season being the most recent including other stadiums, so the idea of "home turf to defend" doesn't really exist. 
## Future Updates
In the future, I think it would be cool to add things like a SQL integration, as well as potentially a python script/tool that exports data from a csv file/spreadsheet and interprets it that way. 