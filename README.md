
## MACHINE LEARNING + Fantasy Premier league ([@fpl__ai](https://twitter.com/fpl__AI))

#### Can machine learning models be used to  predict FPL points of players?

I decided to build a machine learning project to check if this is possible, and to check the quality of the predictions. A twitter account created to monitor the results of the model can be found [here](https://twitter.com/fpl__AI) .

Source code can be found [here](https://github.com/saheedniyi02/fpl-ai) <br>

### Data used?
Finding FPL data was pretty hard for me at first , I checked data from Opta stats and any popular football stats platform you could think of but I couldn't get, after searching deeply I came across a [GitHub repository for FPL data](https://github.com/vaastav/Fantasy-Premier-League) and thankfully the data had FPL data from 2016/17. I also discovered that FPL has an [API](https://medium.com/@frenzelts/fantasy-premier-league-api-endpoints-a-detailed-guide-acbd5598eb19) that gives access to fantasy football data, for the current season.

Data from the github repository ( 2022/23, 2021/2022 and 2020/21 seasons) were used to train the model, the fpl API will be used to get data for every gameweek (Gameweek 1 data already collected) in the current season.<br><br>



### Getting and cleaning Train Data

* [**merged_previous_seasons.py**](https://) 

The data for each player in each gameweek from the 2022/23, 2021/2022 and 2020/21 seasons were downloaded and merged together, new features were also added like the total stats (points, bonus points, goals,saves and co) the player ammassed for the previous seasons, also a new feature that represents the position on the final EPL table the player's team and every opponent the player play agains had in the season before. Another interesting feature added is a column that shows the percentage a player's value contributed to the teams total value for every gameweek ,and  a column that shows how many players are more valuable than a player in his position for his team.

### Cleaning previous season data
* [**clean_previous_seasons.py**](https://) 
Some unused columns were dropped *["xP","opponent_team","expected_assists","expected_goal_involvements","expected_goals","expected_goals_conceded","element_type_ex","team_h_score","team_a_score","element" , "round" ,"fixture","starts" ]* mainly because they had many missing values or don't have much relevance. 
Some set of historical features of type **list** for some columns (*history_stats* in the [*config.py* file]()) were created, this list had the value of a stat the player had in the last 3 gameweeks, for example, **last 3 assists, last 3 goals,last 3 bps, last 3 saves.**

I then calculated the mean and std of some of these historical features (*mean_features* and *std_features* in the [*config.py* file]()). Finally the *last 3 stats* features were dropped.

### Get next gameweek fixtures
* [**weekly_fixtures.py**](https://) 
This file basically scrapes test data for the next gameeweek (players,teams , costs,home team ,away team, kick off time and co) from the [FPL api](https://fantasy.premierleague.com/api/bootstrap-static/).

### Clean next gameweek fixtures
* [**weekly_fixtures.py**](https://) 
This file cleans the scraped the data for the next gameweek and prepares it for modelling, features showing the last season position of a players team, the opposition they are facing, the percentage a player's value contributed to the teams total value for the gameweek, and  a feature that shows how many players are more valuable than a player in his position for his team are added (as was done in the *merge_previous_seasons.py* file). The overall values the player had for some features in the last season (2022/23 season) were added.




### Modeling
* [**train_model.py**](https://) 

I built **2 different models** for each position **(Goalkeepers, defenders, midfielders and forwards).**

The **first model is a classification model that predicts whether a player will start or not.**

The **second model is a regression model that predicts the total points of players that played.**
The **reason for this approach is a lot of players don’t play games at all ** and just predicting the points of all the players directly means our test dataset will have many **0’s which will strongly affect the quality of our regression model.**<br>





### PLOTS
I then created **bar plots** for the top 10 players (with the highest predicted points) in each position, using (**matplotlib**)[https://].
![Top Goalkeepers for gameweek 1](https://github.com/saheedniyi02/fpl-ai/blob/main/plots/goalkeepers.png)
Goalkeepers
![Top Defenders for gameweek 1](https://github.com/saheedniyi02/fpl-ai/blob/main/plots/defenders.png)
Defenders
![Top Midfielders for gameweek 1](https://github.com/saheedniyi02/fpl-ai/blob/main/plots/midfielders.png) 
Midefielders
![Top Fowards for gameweek 1](https://github.com/saheedniyi02/fpl-ai/blob/main/plots/forwards.png)
Forwards



#### I intend on making predictions for every game week and I will be documenting the models prediction and progress here [@fpl__ai](https://twitter.com/fpl__AI).

### Possible Flaws Of the model :

-I observed the model does not think highly of new players coming into the league.


## Folders
* ![**datasets folder**](https://)
The folder contains the raw uncleaned data webscraped directly from the FPL API and this FPL data page. The fixtures and results subfolder contain the fixtures and results from the fixtures for each gameweek in the current season (2023/24).

* ![**cleaned_datasets folder**](https://)
This folder contains the cleaned CSV files from the datasets folder, new features have been created and some unuseful features have been removed. 

* ![**predicted_dataset folder**](https://)
This folder contains the predictions made on the starting players and points by the model for every gameweek.

**This repo will be updated weekly**
