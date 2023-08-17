import pandas as pd
from utils import check_win, get_last_season_pos

"""Code to get and Merge all gameweek data for all players since 2016/17 season"""

years = ["2020-21", "2021-22", "2022-23"]
previous_years = ["2019-20", "2020-21", "2021-22"]
gws = [f"gw{i}" for i in range(1, 39)]


def calculate_ratio_team_value(name):
    """Calculate the ratio of player value to team value"""
    team = df[df["name"] == name]["team"].iloc[0]
    total_value = df[df["team"] == team]["value"].sum()
    value = df[df["name"] == name]["value"].iloc[0]
    return value * 100 / total_value


def calculate_position_rank(name):
    """Calculate the number of players with a higher  value"""
    value = df[df["name"] == name]["value"].iloc[0]
    position = df[df["name"] == name]["position"].iloc[0]
    team = df[df["name"] == name]["team"].iloc[0]
    return df[
        (df["value"] > value) & (df["position"] == position) & (df["team"] == team)
    ]["value"].shape[0]


list_dfs = []

for i, year in enumerate(years):
    print(year)

    # get previous_seasons_data
    player_prev_stats = pd.read_csv(
        f"https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/{previous_years[i]}/cleaned_players.csv"
    )
    player_prev_stats["name"] = (
        player_prev_stats["first_name"] + " " + player_prev_stats["second_name"]
    )
    player_prev_stats.drop(["first_name", "second_name"], axis=1, inplace=True)
    player_prev_stats.columns = player_prev_stats.columns + "_ex"

    # get opponent_team
    teams = pd.read_csv(
        f"https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/{year}/teams.csv",
        encoding="latin-1",
    )[["id", "name"]]
    teams.columns = ["opponent_team", "opponent"]

    # opponents position last season
    teams["opponent_last_season_position"] = teams["opponent"].apply(
        get_last_season_pos(year)
    )

    for gameweek in range(1, 39):
        print(gameweek)
        df = pd.read_csv(
            f"https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/{year}/gws/gw{gameweek}.csv",
            encoding="latin-1",
        )

        # teams position last season
        df["last_season_position"] = df["team"].apply(get_last_season_pos(year))

        # calculate percentage value to team
        df["percent_value"] = df["name"].apply(calculate_ratio_team_value)
        df["position rank"] = df["name"].apply(calculate_position_rank)

        # chek if the result was a win or not
        df["match_result"] = check_win(df)

        # merge previous_season_data
        df = pd.merge(
            df, player_prev_stats, left_on="name", right_on="name_ex", how="left"
        )
        df["season"] = year
        df.drop("name_ex", axis=1, inplace=True)
        df["GW"] = gameweek

        # merge opponent team
        df = pd.merge(df, teams, on="opponent_team", how="left")
        list_dfs.append(df)


all_data = pd.concat(list_dfs)
all_data.to_csv("datasets/previous_seasons.csv")
