import pandas as pd
import numpy as np
from utils import (
    get_opp_team,
    check_win,
    get_last_season_pos,
    create_features,
    mean_features,
    std_features,
    get_players_last_stats_test,
    clean_opponent,
)
from config import unused_columns, history_stats, no_last_stats
import warnings

warnings.filterwarnings("ignore")


def calculate_ratio_team_value(name, df=None):
    """Calculate the ratio of player value to team value"""
    team = df[df["name"] == name]["team"].iloc[0]
    total_value = df[df["team"] == team]["value"].sum()
    value = df[df["name"] == name]["value"].iloc[0]
    return value * 100 / total_value


def calculate_position_rank(name, df=None):
    """Calculate the number of players with a higher  value"""
    value = df[df["name"] == name]["value"].iloc[0]
    position = df[df["name"] == name]["position"].iloc[0]
    team = df[df["name"] == name]["team"].iloc[0]
    return df[
        (df["value"] > value) & (df["position"] == position) & (df["team"] == team)
    ]["value"].shape[0]


gameweek = 2
old_gameweek_results = []
for i in range(1, gameweek):
    result = pd.read_csv(f"datasets/2023-24/results/GW{i}.csv", index_col=0)
    result.columns = [
        "element",
        "fixture",
        "opponent_team",
        "total_points",
        "was_home",
        "kickoff_time",
        "team_h_score",
        "team_a_score",
        "round",
        "minutes",
        "goals_scored",
        "assists",
        "clean_sheets",
        "goals_conceded",
        "own_goals",
        "penalties_saved",
        "penalties_missed",
        "yellow_cards",
        "red_cards",
        "saves",
        "bonus",
        "bps",
        "influence",
        "creativity",
        "threat",
        "ict_index",
        "starts",
        "expected_goals",
        "expected_assists",
        "expected_goal_involvements",
        "expected_goals_conceded",
        "value",
        "transfers_balance",
        "selected",
        "transfers_in",
        "transfers_out",
        "id",
        "name",
        "cost",
        "position",
        "home_team",
        "away_team",
        "team",
    ]
    year = "2023-24"
    previous_year = "2022-23"
    result["xP"] = 0
    result["GW"] = i
    result["match_result"] = check_win(result)
    result["opponent"] = get_opp_team(result)
    result["last_season_position"] = result["team"].apply(get_last_season_pos(year))
    result["opponent_last_season_position"] = result["opponent"].apply(
        get_last_season_pos(year)
    )
    result["percent_value"] = result["name"].apply(
        calculate_ratio_team_value, args=(result,)
    )
    result["position rank"] = result["name"].apply(
        calculate_position_rank, args=(result,)
    )

    player_prev_stats = pd.read_csv(
        f"https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/{previous_year}/cleaned_players.csv"
    )
    player_prev_stats["name"] = (
        player_prev_stats["first_name"] + " " + player_prev_stats["second_name"]
    )
    player_prev_stats.drop(["first_name", "second_name"], axis=1, inplace=True)
    player_prev_stats.columns = player_prev_stats.columns + "_ex"
    result = pd.merge(
        result, player_prev_stats, left_on="name", right_on="name_ex", how="left"
    )
    result.drop(unused_columns, axis=1, inplace=True)
    old_gameweek_results.append(result)

# print(old_gameweek_results[0]["opponent"].value_counts())
current_fixture = pd.read_csv(
    f"datasets/2023-24/fixtures/GW{gameweek}.csv", index_col=0
)
current_fixture.columns = [
    "id",
    "name",
    "value",
    "position",
    "home_team",
    "away_team",
    "kickoff_time",
    "was_home",
    "team",
]


current_fixture["opponent"] = get_opp_team(current_fixture)
# print(current_fixture["opponent"].value_counts())
current_fixture["last_season_position"] = current_fixture["team"].apply(
    get_last_season_pos(year)
)
current_fixture["opponent_last_season_position"] = current_fixture["opponent"].apply(
    get_last_season_pos(year)
)
current_fixture["percent_value"] = current_fixture["name"].apply(
    calculate_ratio_team_value, args=(current_fixture,)
)
current_fixture["position rank"] = current_fixture["name"].apply(
    calculate_position_rank, args=(current_fixture,)
)


# check_win not posible because it's only fixtures we have for now
# merge last season data
player_prev_stats = pd.read_csv(
    f"https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/{previous_year}/cleaned_players.csv"
)

player_prev_stats["name"] = (
    player_prev_stats["first_name"] + " " + player_prev_stats["second_name"]
)

player_prev_stats.drop(["first_name", "second_name"], axis=1, inplace=True)
player_prev_stats.columns = player_prev_stats.columns + "_ex"
current_fixture = pd.merge(
    current_fixture, player_prev_stats, left_on="name", right_on="name_ex", how="left"
)

current_fixture["GW"] = gameweek
old_gameweek_results.append(current_fixture)
data = pd.concat(old_gameweek_results)
data = data.sort_values(["name", "kickoff_time"], ascending=True)


data["season"] = year
data.drop(["name_ex", "id", "home_team", "away_team"], axis=1, inplace=True)


for stat in history_stats:
    print(stat)
    data = get_players_last_stats_test(data, stat)

data = create_features(data, mean_features, std_features)
data.drop(
    [f"last {no_last_stats} {stat}" for stat in history_stats], axis=1, inplace=True
)


# save cleaned files
for i in range(1, gameweek + 1):
    data_gw = data[data["GW"] == i]
    data_gw.to_csv(f"cleaned_dataset/2023-24/GW{i}.csv")
