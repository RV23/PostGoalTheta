# PostGoalTheta


Planned structure of PostGoalTheta()

1) Connection to Betfair API
a) Need to have StayAlive() functionality to handle getting booted out for inactivity

2) Connection to Livescore feeds
a) Needs to have StayAlive() functionality

3) Requests from Betfair
a) Currently playing games and games being played today (and save kick off times) GetGames()
b) 2-way odds for over x.5 goals for each game GetGameScoreOdds()
c) Some basic liquidity metrics for that market Getliquidity()

4) Requests from Livescore
a) The scores from each game GetScores()
b) Time remaining in game (can we find out extra time when announced?) GetTimes()

5) Response Handling from Betfair API 
a) Infer middle implied probablities from the odds and calculate implied theta decay (markettheta) OddsCalc()
b) Compare to database of games implying similar start of game odds and create "Comparable game sample group"
c) Save odds in an intragame time series column which creates a game and betting history for each game
d) Compare the liquidity metrics to our model's required specification and create boolean (liquid) to determine if liquidity on that game is satisfactory

6) Creating internal model parameters for the game
a) Look at the Comparable game sample group and calculate variable (threshhold) which is a threshhold jump in implied theta as defined by a standard deviation move on the Comparable game sample group after a goal has been scored. The standard deviation will need to be decided beforehand as our model's "profitable sell signal". The threshhold variable will be a function of both this as the distribution of the Comparable game sample group. 

7) Response Handling from Livescore
a) Refresh the score and create a "Has a goal just been scored" (recentgoal) boolean (in the last 1-2 minutes for example)

8) Deciding whether to bet
a) If recentgoal = true, run OddsCalc again and define (theta1) as new theta post goalscoring. If theta1 > theta + threshhold, and liquid = true then launch BettingModule()

9) Bettingmodule() (this section requires more thought and work)
a) Define optimal betting size given account balance (betsize)
b) Send at market lay request forstake = betsize
c) Create variable (matched) to identify if bet was successfully matched, if matched=false then rerun BettingModule() if threshhold criteria is still validated) 

10) Exiting strategy
a) Looking at sample population, determine a second threshhold (takeprofitThreshhold) which defines a take profit level once theta has realigned with Fairvalue 
b) If theta1- Fairvalue theta <takeprofitThreshhold then run BettingModule() for full size of bet at risk, and changing market lay request to a market back request to exit the position.

11) Creating progress report for tracking strategy performance
