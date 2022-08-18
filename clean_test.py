import pandas as pd
import numpy as np
from utils import get_opp_team
from config import *
from utils import (
    get_2021_22_season_pos,
    position_stats,
    get_all_players_last_stats_test,
    check_win,
    remove_neg,clean_minutes,create_features
)

import warnings

warnings.filterwarnings("ignore")


week1 = pd.read_csv("datasets/week1_results.csv",index_col=0)
week2 = pd.read_csv("datasets/week2.csv",index_col=0)

week2.columns = [
    "id",
    "name",
    "value",
    "position",
    "home_team",
    "away_team",
    "kickoff_time",
    "was_home",
    "team_x",
]
week1["GW"] = 1
week2["GW"] = 2

train = pd.read_csv("datasets/cleaned_merged_seasons.txt", index_col=0)


test = pd.concat([week1, week2])
test=test.sort_values(["name", "kickoff_time"], ascending=True)
test = get_opp_team(test)
test = test.drop("id",axis=1)
test["index"]=[i for i in range(test.shape[0])]
test=test.set_index("index")

test["kickoff_time"] = pd.to_datetime(test["kickoff_time"])
# print(test["team_a_score"].value_counts())
# print(test["team_h_score"].value_counts())
test["team_a_score"] = test["team_a_score"].fillna(0)
test["team_h_score"] = test["team_h_score"].fillna(0)
test["result_difference"] = (test["team_a_score"] - test["team_h_score"]).astype("i")
test["result_difference"] = test["result_difference"].apply(remove_neg)
test["result"] = check_win(test)
test["minutes"] = test["minutes"].apply(clean_minutes)
test["bonus"] = test["bonus"].apply(clean_minutes)
test["team_last_position"] = test["team_x"].apply(get_2021_22_season_pos)
test["opponent_last_position"] = test["opp_team_name"].apply(get_2021_22_season_pos)

players_stats_21_22 = pd.read_csv("datasets/cleaned_players_21_22_2.csv", index_col=0)
players_stats_21_22.drop(
    ["season_name", "element_code", "start_cost", "end_cost"]
    + players_stats_21_22_dropped,
    axis=1,
    inplace=True,
)

players_stats_21_22.columns = players_stats_21_22.columns + "_ex"

test = pd.merge(
    test, players_stats_21_22, left_on="name", right_on="name_ex", how="left"
)
test["season_x"] = "2022-23"
for i in train.columns:
    if i not in test.columns:
        print(i)
        
for i in test.columns:
    if i not in train.columns:
        print(i) 


test.drop(["away_team", "home_team"], axis=1, inplace=True)
for position in ["DEF", "GKP", "FWD", "MID"]:
    print(position)
    data_position = test[test["position"].isin([position])]
    for stat in position_stats[position]:
        data_position = get_all_players_last_stats_test(data_position, stat)
        data_position = get_all_players_last_stats_test(
            data_position, stat, long_term_stats
        )
    if position != "GKP":
        data_position = create_features(
            data_position, mode_features, mean_features, std_features
        )

    else:
        data_position = create_features(
            data_position, mode_features, gkp_mean_features, gkp_std_features
        )
    data_position["kickoff_hour"] = data_position["kickoff_time"].dt.hour
    data_position.drop(droppped_columns, axis=1, inplace=True)
    data_position.drop(
        [
            f"last {no_last_stats} {stat}"
            for stat in position_stats[position]
            for no_last_stats in [short_term_stats, long_term_stats]
        ],
        axis=1,
        inplace=True,
    )
    print(data_position["total_points"])
    data_position.to_csv(f"cleaned_dataset/test_{position}.csv")
