seasons=["2020-21","2021-22","2022-23"]

unused_columns=["xP","opponent_team","expected_assists","expected_goal_involvements","expected_goals",
                "expected_goals_conceded","element_type_ex","team_h_score","team_a_score","element" , "round" ,"fixture","starts" ]

#stats that you want to use their values for the last few games to predict a

no_last_stats=3 #number of last gameweek stats to use for prediction

history_stats=["assists","bonus","bps","clean_sheets","creativity","goals_conceded","goals_scored","ict_index","influence","minutes",
               "own_goals","penalties_missed","penalties_saved","red_cards","saves","selected","threat","total_points","transfers_in","transfers_out","value","match_result"]
               
last_features=[f"last {no_last_stats} {stat}" for stat in history_stats]

mean_features=["assists","bonus","bps","clean_sheets","creativity","goals_conceded",
     "goals_scored","ict_index","influence","minutes"
     ,"own_goals","penalties_missed","penalties_saved",
     "red_cards","saves","selected","threat","total_points"
     ,"transfers_in","transfers_out","value","match_result"]

std_features=["bps","creativity","ict_index","influence","minutes","selected","threat","total_points","transfers_in","transfers_out","value"]              



dropped_columns = [
    "season",
    "opponent",
    "match_result",
    "position",
    "assists",
    "penalties_missed",
    "bonus",
    "bps",
    "clean_sheets",
    "creativity",
    "goals_conceded",
    "goals_scored",
    "ict_index",
    "influence",
    "own_goals",
    "penalties_saved",
    "red_cards",
    "saves",
    "selected",
    "threat",
    "transfers_balance",
    "transfers_in",
    "transfers_out",
    "yellow_cards"
]  # "value",


forward_statistics =['value', 'was_home', 'last_season_position', 'percent_value',       
       'position rank', 'goals_scored_ex', 'assists_ex', 'total_points_ex',
       'minutes_ex', 'goals_conceded_ex', 'creativity_ex', 'influence_ex', 
       'threat_ex', 'bonus_ex', 'bps_ex', 'ict_index_ex', 'now_cost_ex', 'GW', 'opponent_last_season_position',
        'mean assists 3','mean bonus 3', 'mean bps 3','mean creativity 3', 'mean goals_scored 3',
       'mean ict_index 3', 'mean influence 3', 'mean minutes 3', 'mean penalties_missed 3',  'mean threat 3',
       'mean total_points 3','mean value 3', 'mean match_result 3', 'std bps 3', 'std creativity 3',
       'std ict_index 3', 'std influence 3', 'std minutes 3',
       'std threat 3', 'std total_points 3', 'std value 3']

leak_columns = [
    "name",
    "team",
]  # columns that shouldnt be used in training fir fear of data leakage


midfielder_statistics =['value', 'was_home', 'last_season_position', 'percent_value',       
       'position rank', 'goals_scored_ex', 'assists_ex', 'total_points_ex',
       'minutes_ex', 'goals_conceded_ex', 'creativity_ex', 'influence_ex', 
       'threat_ex', 'bonus_ex', 'bps_ex', 'ict_index_ex', 'now_cost_ex', 'GW', 'opponent_last_season_position',
        'mean assists 3','mean bonus 3', 'mean bps 3','mean creativity 3', 'mean goals_scored 3',
       'mean ict_index 3', 'mean influence 3', 'mean minutes 3', 'mean penalties_missed 3',  'mean threat 3',
       'mean total_points 3','mean value 3', 'mean match_result 3', 'std bps 3', 'std creativity 3',
       'std ict_index 3', 'std influence 3', 'std minutes 3',
       'std threat 3', 'std total_points 3', 'std value 3']

goalkeeper_statistics = ['value', 'was_home', 'last_season_position', 'percent_value',       
       'position rank', 'total_points_ex', 'minutes_ex', 'goals_conceded_ex', 
       'bonus_ex', 'bps_ex', 'ict_index_ex', 'clean_sheets_ex',
       'red_cards_ex', 'now_cost_ex', 'GW', 'opponent_last_season_position',
       'mean bonus 3', 'mean bps 3', 'mean clean_sheets 3', 'mean goals_conceded 3', 
       'mean ict_index 3',  'mean minutes 3',
       'mean own_goals 3',  'mean penalties_saved 3',
        'mean saves 3',  'mean threat 3',
       'mean total_points 3',
       'mean value 3', 'mean match_result 3', 'std bps 3',
       'std ict_index 3', 'std influence 3', 'std minutes 3',
       'std threat 3', 'std total_points 3', 'std value 3']


defender_statistics =['value', 'was_home', 'last_season_position', 'percent_value',       
       'position rank', 'goals_scored_ex', 'assists_ex', 'total_points_ex',
       'minutes_ex', 'goals_conceded_ex', 'creativity_ex', 'influence_ex', 
       'threat_ex', 'bonus_ex', 'bps_ex', 'ict_index_ex', 'clean_sheets_ex',
       'yellow_cards_ex','now_cost_ex', 'GW', 'opponent_last_season_position', 'mean assists 3',
       'mean bonus 3', 'mean bps 3', 'mean clean_sheets 3',
       'mean creativity 3', 'mean goals_conceded 3', 'mean goals_scored 3',
       'mean ict_index 3', 'mean influence 3', 'mean minutes 3',
       'mean own_goals 3', 'mean penalties_missed 3', 'mean penalties_saved 3',
       'mean red_cards 3',  'mean threat 3','mean total_points 3',
       'mean value 3', 'mean match_result 3', 'std bps 3', 'std creativity 3',
       'std ict_index 3', 'std influence 3', 'std minutes 3',
       'std threat 3', 'std total_points 3', 'std value 3']

position_stats = {
    "FWD": forward_statistics,
    "GK": goalkeeper_statistics,
    "GKP": goalkeeper_statistics,
    "DEF": defender_statistics,
    "MID": midfielder_statistics,
}


"""mode_features = ["result", "clean_sheets", "minutes"]
mean_features = [
    "bonus",
    "bps",
    "assists",
    "creativity",
    "goals_scored",
    "ict_index",
    "influence",
    "value",
    "threat",
    "result_difference",
    "goals_conceded",
    "total_points",
]
std_features = [
    "assists",
    "creativity",
    "goals_scored",
    "ict_index",
    "influence",
    "threat",
    "goals_conceded",
    "result_difference",
    "value",
    "bps",
    "total_points",
]"""

gkp_mean_features = [
    "bonus",
    "bps",
    "ict_index",
    "influence",
    "value",
    "penalties_saved",
    "saves",
    "threat",
    "result_difference",
    "goals_conceded",
    "total_points",
]

gkp_std_features = [
    "ict_index",
    "influence",
    "penalties_saved",
    "saves",
    "threat",
    "goals_conceded",
    "result_difference",
    "value",
    "total_points",
]

week1_missing = [
    "assists",
    "bonus",
    "bps",
    "clean_sheets",
    "creativity",
    "element",
    "fixture",
    "goals_conceded",
    "goals_scored",
    "ict_index",
    "influence",
    "minutes",
    "opponent_team",
    "own_goals",
    "penalties_missed",
    "penalties_saved",
    "red_cards",
    "round",
    "saves",
    "selected",
    "team_a_score",
    "team_h_score",
    "threat",
    "total_lpoints",
    "transfers_balance",
    "transfers_in",
    "transfers_out",
    "yellow_cards",
    "result_difference",
    "result",
]
short_term_stats = 3
long_term_stats = 9
no_plotted_players = 10
x_ticks = 90

"""['value', 'was_home', 'last_season_position', 'percent_value',       
       'position rank', 'goals_scored_ex', 'assists_ex', 'total_points_ex',
       'minutes_ex', 'goals_conceded_ex', 'creativity_ex', 'influence_ex', 
       'threat_ex', 'bonus_ex', 'bps_ex', 'ict_index_ex', 'clean_sheets_ex',
       'red_cards_ex', 'yellow_cards_ex',
       'now_cost_ex', 'GW', 'opponent_last_season_position', 'mean assists 3',
       'mean bonus 3', 'mean bps 3', 'mean clean_sheets 3',
       'mean creativity 3', 'mean goals_conceded 3', 'mean goals_scored 3',
       'mean ict_index 3', 'mean influence 3', 'mean minutes 3',
       'mean own_goals 3', 'mean penalties_missed 3', 'mean penalties_saved 3',
       'mean red_cards 3', 'mean saves 3',  'mean threat 3',
       'mean total_points 3',
       'mean value 3', 'mean match_result 3', 'std bps 3', 'std creativity 3',
       'std ict_index 3', 'std influence 3', 'std minutes 3',
       'std threat 3', 'std total_points 3', 'std value 3']"""