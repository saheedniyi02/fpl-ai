
## MACHINE LEARNING + Fantasy Premier league ([@fpl__ai](https://twitter.com/fpl__AI))

#### Can machine learning models be used to  predict FPL points of players?

I decided to build a machine learning project to check if this is possible, and to check the quality of the predictions. A twitter account created to monitor the results of the model can be found [here](https://twitter.com/fpl__AI) .

Source code can be found [here](https://github.com/saheedniyi02/fpl-ai) <br>

#### Data used?
Finding FPL data was pretty hard for me at first , I checked data from Opta stats and any popular football stats platform you could think of but I couldn't get, after searching deeply I came across a [GitHub repository for FPL data](https://github.com/vaastav/Fantasy-Premier-League) and thankfully the data had FPL data from 2016/17. I also discovered that FPL has an [API](https://medium.com/@frenzelts/fantasy-premier-league-api-endpoints-a-detailed-guide-acbd5598eb19) that gives access to fantasy football data, for the current season.

Data from the github repository was used to train the model, the fpl API will be used to get data for every gameweek (Gameweek 1 data already collected) in the current season.<br><br>

#### Data Cleaning and data preparation:

#### Train Data

Although the FPL repository has data from 2016/17, I discovered there were many missing Gameweeks for the 2016/17, 2017/18, 2018/19,2019/20 seasons respectively.

So I used only the 2020/21 and 2021/22 data, although there were some missing Gameweeks for some clubs in those years also,it's still better than nothing.

The data in the columns were presented in such a way that each column has information and statistics in a matchday for every player and the "total_points" from that match day is the target I am interested in.<br>


#### Data wrangling done:
-I dropped rows with duplicate values of name,season and gameweek.

-I extracted gameweek values from only 2020/21 and 2021/22 seasons.

-I also arranged the columns in ascending order of “name” and “kickoff_time” such that consecutive matches by a player will be grouped together, in ascending order of the dates.

-I created a new feature which checks the result of the current match (whether a win,draw or loss).

-I converted the minutes column to a categorical column, of class 1 if the player played and class 0 if the player didn't play.

-I created a new feature that checks if a player receives bonus points or not for a particular match and I dropped the previous “bonus” feature.

-I added new features from the total stats by a player from the previous season (goals_scored,assists,,clean_sheets, total_points, threats and other important features ) and team (last season’s position), new players to the league will have missing values for those columns, newly promoted teams will have a position of 20.

-I splitted the dataset into each position, (Goalkeepers, defenders, midfielders and forwards).

-I created two types of features; long term and short term features, the features were numpy arrays. The array contains the values of a particular stats from previous match days, the long term stats feature considered the last 9 features prior to every match day in the datapoints, the short term stats considered the last 3 matches.

The aim of this feature is to capture the **players form, short term and long term.**

-I calculated the mean, standard deviation and mode of some of these lists ,lists that were empty(from the first match in a season) were given values of -1 , and then I dropped the long term and short term features.

-I also dropped the important results/ columns from the current Gameweek I’m trying to predict on, this is to prevent any possible data leakage when building the model. I dropped the name and team features, to ensure that the model only makes predictions based on the form of players and not on names of players and teams.

-I did almost the same cleaning on the test dataset (data from gameweek 1 of the new season) also.<br>

#### Train test split:
I splitted the data based on the gameweeks to ensure all gameweeks are well represented in the train and test results.<br><br>

#### Modeling

I built **2 different models** for each position **(Goalkeepers, defenders, midfielders and forwards).**

The **first model is a classification model that predicts whether a player will start or not.**

The **second model is a regression model that predicts the total points of players that played.**
The **reason for this approach is a lot of players don’t play games at all ** and just predicting the points of all the players directly means our test dataset will have many **0’s which will strongly affect the quality of our regression model.**<br>

**Goalkeeper models**: Random Forest Classifier and Random Forest Regressor.<br>
Evaluation results.<br>
Accuracy_score: 0.94<br>
F1_score :0.89<br>
Mean_squared_error:2.801 points.<br>

**Defender models**: Random Forest Classifier and Gradient Boosting Regressor.<br>
Accuracy score: 0.82<br>
f1 score: 0.78<br>
Root_mean_squared_error:  2.718.<br>


**Midfielder models**: Random Forest Classifier and Random Forest Regressor.<br>
Evaluation results.<br>
Accuracy score: 0.82<br>
f1 score: 0.82<br>
Root_mean_squared_error: 2.700<br>


**Forwards models**: Random Forest Classifier and Gradient Boosting Regressor.<br>
Evaluation results.<br>
Accuracy_score: 0.82<br>
F1_score :  0.79<br>
Mean_squared_error: 3.057<br>




#### PLOTS
I scaled down the predicted points from the model **into values between 0 and 1**, I then created **bar plots** for the top 10 players (with the highest predicted points) in each position, using **plotly**.
![Top Goalkeepers for gameweek 1](https://github.com/saheedniyi02/fpl-ai/blob/main/plots/goalkeepers.png)
Goalkeepers
![Top Defenders for gameweek 1](https://github.com/saheedniyi02/fpl-ai/blob/main/plots/defenders.png)
Defenders
![Top Midfielders for gameweek 1](https://github.com/saheedniyi02/fpl-ai/blob/main/plots/midfielders.png)
Midefielders
![Top Fowards for gameweek 1](https://github.com/saheedniyi02/fpl-ai/blob/main/plots/forwards.png)
Forwards

 #### Building my team: 

I used **PuLP,a linear optimization and discrete programming package in python, to build my team (credits to this [article](https://towardsdatascience.com/how-to-build-a-fantasy-premier-league-team-with-data-science-f01283281236?gi=5bfd5d33d2f7) ).**

I built my team following the **FPL constraints.**
-2 goalkeepers,5 defenders, 5 midfielders and 3 forwards.
-A team value of maximum of 100 , I used 99 though, the 1 Extra is reserved to make future transfers easier. The values of players in the data was multiplied by 10 (default from FPL api, so the team value used in the solution is 1000, 990)
-Maximum of 3 players from each team.
-The team that had the highest total predicted points

**The team selections for gameweek 1 can be seen below.**
<br>
![Teams](https://github.com/saheedniyi02/fpl-ai/blob/main/plots/Screenshot_20220805-104913.png) <br>
![Starting line up](https://github.com/saheedniyi02/fpl-ai/blob/main/plots/Screenshot_20220805-104933.png)


#### I intend on making predictions for every game week and I will be documenting the models prediction here @fpl__AI.

#### Flaws of the model:

-The premier league introduced the 5 substitution rule for the 2022/23 football season the means that a lot of players who previously stayed on the bench in many matches will have more chances of playing.

-I observed the model does not think too highly of new players coming into the league.
