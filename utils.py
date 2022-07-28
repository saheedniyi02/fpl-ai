from config import *
import numpy as np
import pandas as pd
from scipy import stats


def check_win(data):
    list_win = []
    for index in data.index:
        result = data["result_difference"].loc[index]
        is_home = data["was_home"].loc[index]
        if result == 0:
            list_win.append("draw")
        elif result > 0 and is_home == True:
            list_win.append("loss")
        elif result < 0 and is_home == True:
            list_win.append("win")
        elif result > 0 and is_home == False:
            list_win.append("win")
        elif result < 0 and is_home == False:
            list_win.append("loss")
    return list_win


def remove_neg(val):
    if val > 0:
        return val
    else:
        return -val


def deque_and_queue(stats, value):
    # if -1 in stats:
    #  return stats
    # deque
    stats = stats[1:]
    stats.append(value)
    return stats


def get_last_stats(data, stat, name, no_last_stats=short_term_stats):
    name_df = data[data["name"] == name]
    seasons = ["2020-21", "2021-22"]
    name_df_dict = {}
    for season in seasons:
        name_df_season = name_df[name_df["season_x"] == season]
        list_stats = []
        stats_x = []
        for value in name_df_season[stat]:
            if len(stats_x) < no_last_stats:
                list_stats.append(np.array(stats_x))
                stats_x.append(value)
            else:
                list_stats.append(np.array(stats_x))
                stats_x = deque_and_queue(stats_x, value)
        name_df_season[f"last {no_last_stats} {stat}"] = list_stats
        name_df_dict[season] = name_df_season
    return pd.concat(name_df_dict.values())


def get_all_players_last_stats(data, stat, no_last_stats=short_term_stats):
    players_df = []
    for player in data["name"].unique():
        data_player = get_last_stats(data, stat, player, no_last_stats)
        players_df.append(data_player)
    # print(pd.concat(players_df))
    return pd.concat(players_df)


def clean_minutes(val):
    if val > 0:
        return 1
    else:
        return 0


def find_mode(vals):
    try:
        if -1 in vals:
            return -1
        return stats.mode(vals)[0][0]
    except IndexError:
        return np.nan


def find_mean(vals):
    try:
        if -1 in vals:
            return -1
        return np.mean(vals)
    except:
        return np.nan


def find_max(vals):
    try:
        if -1 in vals:
            return -1
        return np.max(vals)
    except:
        return np.nan


def find_std(vals):
    try:
        if -1 in vals:
            return -1
        return np.std(vals)
    except:
        return np.nan


def find_value_count(vals, to_count):
    try:
        if -1 in vals:
            return -1
        values, count = np.unique(vals, return_counts=True)
        index = np.where(values == to_count)[0][0]
        return count[index]

    except:
        return -2


def get_2020_21_season_pos(club):
    if club == "Man City":
        return 1
    elif club == "Man Utd":
        return 2
    elif club == "Liverpool":
        return 3
    elif club == "Chelsea":
        return 4
    elif club == "Leicester":
        return 5
    elif club == "West Ham":
        return 6
    elif club == "Spurs":
        return 7
    elif club == "Arsenal":
        return 8
    elif club == "Leeds":
        return 9
    elif club == "Everton":
        return 10
    elif club == "Aston Villa":
        return 11
    elif club == "Newcastle":
        return 12
    elif club == "Wolves":
        return 13
    elif club == "Crystal Palace":
        return 14
    elif club == "Southampton":
        return 15
    elif club == "Brighton":
        return 16
    elif club == "Burnley":
        return 17
    else:
        return 20


def get_2019_20_season_pos(club):
    if club == "Liverpool":
        return 1
    elif club == "Man City":
        return 2
    elif club == "Man Utd":
        return 3
    elif club == "Chelsea":
        return 4
    elif club == "Leicester":
        return 5
    elif club == "Spurs":
        return 6
    elif club == "Wolves":
        return 7
    elif club == "Arsenal":
        return 8
    elif club == "Sheffield Utd":
        return 9
    elif club == "Burnley":
        return 10
    elif club == "Southampton":
        return 11
    elif club == "Everton":
        return 12
    elif club == "Newcastle":
        return 13
    elif club == "Crystal Palace":
        return 14
    elif club == "Brighton":
        return 15
    elif club == "West Ham":
        return 16
    elif club == "Aston Villa":
        return 17
    else:
        return 20


def get_opp_team(test_data):
    opp_teams = []
    home_teams = test_data["home_team"]
    away_teams = test_data["away_team"]
    my_teams = test_data["team_x"]
    for id in test_data.index:
        my_team = my_teams.iloc[id]
        home_team = home_teams.iloc[id]
        away_team = away_teams.iloc[id]
        if my_team == home_team:
            opp_teams.append(away_team)
        else:
            opp_teams.append(home_team)
    test_data["opp_team_name"] = opp_teams
    return test_data


def get_2021_22_season_pos(club):
    if club == "Man City":
        return 1
    elif club == "Liverpool":
        return 2
    elif club == "Chelsea":
        return 3
    elif club == "Spurs":
        return 4
    elif club == "Arsenal":
        return 5
    elif club == "Man Utd":
        return 6
    elif club == "West Ham":
        return 7
    elif club == "Leicester":
        return 8
    elif club == "Brighton":
        return 9
    elif club == "Wolves":
        return 10
    elif club == "Newcastle":
        return 11
    elif club == "Crystal Palace":
        return 12
    elif club == "Brentford":
        return 13
    elif club == "Aston Villa":
        return 14
    elif club == "Southampton":
        return 15
    elif club == "Everton":
        return 16
    elif club == "Leeds":
        return 17
    else:
        return 20


def get_last_stats_test(data, stat, name, no_last_stats=short_term_stats):
    name_df = data[data["name"] == name]
    list_stats = []
    stats_x = []
    for value in name_df[stat]:
        if len(stats_x) < no_last_stats:
            list_stats.append(np.array(stats_x))
            stats_x.append(value)
        else:
            list_stats.append(np.array(stats_x))
            stats_x = deque_and_queue(stats_x, value)
    name_df[f"last {no_last_stats} {stat}"] = list_stats
    return name_df


def get_all_players_last_stats_test(data, stat, no_last_stats=short_term_stats):
    players_df = []
    for player in data["name"].unique():
        data_player = get_last_stats_test(data, stat, player, no_last_stats)
        players_df.append(data_player)
    # print(pd.concat(players_df))
    return pd.concat(players_df)


def create_features(data, mode_features, mean_features, std_features):
    for no_last_stats in [short_term_stats, long_term_stats]:
        for mode_feature in mode_features:
            data[f"mode {mode_feature} {no_last_stats}"] = [
                find_mode(values)
                for values in data[f"last {no_last_stats} {mode_feature}"]
            ]
        for mean_feature in mean_features:
            data[f"mean {mean_feature} {no_last_stats}"] = [
                find_mean(values)
                for values in data[f"last {no_last_stats} {mean_feature}"]
            ]
        for std_feature in std_features:
            data[f"std {mode_feature} {no_last_stats}"] = [
                find_std(values)
                for values in data[f"last {no_last_stats} {std_feature}"]
            ]
        data[f"count {no_last_stats} result win"] = [
            find_value_count(values, "win")
            for values in data[f"last {no_last_stats} result"]
        ]
        data[f"count {no_last_stats} result loss"] = [
            find_value_count(values, "loss")
            for values in data[f"last {no_last_stats} result"]
        ]
        data[f"count {no_last_stats} result draw"] = [
            find_value_count(values, "draw")
            for values in data[f"last {no_last_stats} result"]
        ]
        data[f"count {no_last_stats} yellow_cards 1"] = [
            find_value_count(values, 1)
            for values in data[f"last {no_last_stats} yellow_cards"]
        ]
        data[f"count {no_last_stats} was_home True"] = [
            find_value_count(values, True)
            for values in data[f"last {no_last_stats} was_home"]
        ]
        data[f"count {no_last_stats} bonus 1"] = [
            find_value_count(values, 1)
            for values in data[f"last {no_last_stats} bonus"]
        ]
        data[f"count {no_last_stats} minutes 1"] = [
            find_value_count(values, 1)
            for values in data[f"last {no_last_stats} minutes"]
        ]
        return data


def clean_train():
    train_data = pd.read_csv(
        "cleaned_merged_seasons.txt",
        index_col=0,
        low_memory=False,
    )
    train_data = train_data[train_data["season_x"].isin(["2021-22", "2020-21"])]
    train_data = train_data.sort_values(["name", "kickoff_time"], ascending=True)
    train_data["kickoff_time"] = pd.to_datetime(train_data["kickoff_time"])
    train_data["result_difference"] = (
        train_data["team_a_score"] - train_data["team_h_score"]
    ).astype("i")
    train_data["result_difference"] = train_data["result_difference"].apply(remove_neg)
    train_data["result"] = check_win(train_data)
    train_data["minutes"] = train_data["minutes"].apply(clean_minutes)
    train_data["bonus"] = train_data["bonus"].apply(clean_minutes)

    # split data into season
    train_data_20_21 = train_data[train_data["season_x"].isin(["2020-21"])]
    train_data_21_22 = train_data[train_data["season_x"].isin(["2021-22"])]
    train_data_20_21["team_last_position"] = train_data_20_21["team_x"].apply(
        get_2019_20_season_pos
    )
    train_data_20_21["opponent_last_position"] = train_data_20_21[
        "opp_team_name"
    ].apply(get_2019_20_season_pos)
    train_data_21_22["team_last_position"] = train_data_21_22["team_x"].apply(
        get_2020_21_season_pos
    )
    train_data_21_22["opponent_last_position"] = train_data_21_22[
        "opp_team_name"
    ].apply(get_2020_21_season_pos)

    # load_extra stats
    players_stats_19_20 = pd.read_csv("cleaned_players_19_20.txt")
    players_stats_20_21 = pd.read_csv("cleaned_players_20_21.txt")

    players_stats_19_20["name"] = (
        players_stats_19_20["first_name"] + " " + players_stats_19_20["second_name"]
    )
    players_stats_20_21["name"] = (
        players_stats_20_21["first_name"] + " " + players_stats_20_21["second_name"]
    )
    players_stats_19_20.drop(player_stats_19_20_dropped, axis=1, inplace=True)
    players_stats_20_21.drop(player_stats_20_21_dropped, axis=1, inplace=True)
    players_stats_19_20.columns = players_stats_19_20.columns + "_ex"
    players_stats_20_21.columns = players_stats_20_21.columns + "_ex"
    train_data_20_21 = pd.merge(
        train_data_20_21,
        players_stats_19_20,
        left_on="name",
        right_on="name_ex",
        how="left",
    )
    train_data_21_22 = pd.merge(
        train_data_21_22,
        players_stats_20_21,
        left_on="name",
        right_on="name_ex",
        how="left",
    )
    data = pd.concat([train_data_20_21, train_data_21_22])
    data = data.sort_values(by="kickoff_time")
    for position in ["DEF", "GK", "FWD", "MID"]:
        data_position = data[data["position"].isin([position])]
        for stat in position_stats[position]:
            data_position = get_all_players_last_stats(data_position, stat)
            data_position = get_all_players_last_stats(
                data_position, stat, long_term_stats
            )
        if position != "GK":
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
        data_position.to_csv(f"train_{position}.csv")


def clean_firstmatchday():
    test_data = pd.read_csv("week1.csv", index_col=0)
    test_data.columns = [
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
    test_data = get_opp_team(test_data)
    test_data = test_data.set_index("id")
    test_data["kickoff_time"] = pd.to_datetime(test_data["kickoff_time"])
    test_data["team_last_position"] = test_data["team_x"].apply(get_2021_22_season_pos)
    test_data["opponent_last_position"] = test_data["opp_team_name"].apply(
        get_2021_22_season_pos
    )
    players_stats_21_22 = pd.read_csv(
        "cleaned_players_21_22_2.csv", index_col=0
    )
    players_stats_21_22.drop(
        ["season_name", "element_code", "start_cost", "end_cost"], axis=1, inplace=True
    )
    players_stats_21_22.drop(players_stats_21_22_dropped, axis=1, inplace=True)
    players_stats_21_22.columns = players_stats_21_22.columns + "_ex"
    test_data = pd.merge(
        test_data, players_stats_21_22, left_on="name", right_on="name_ex", how="left"
    )
    test_data["season_x"] = "2022-23"
    test_data["GW"] = 1
    for i in week1_missing:
        if i not in test_data.columns:
            test_data[i] = 0
    test_data.drop(["away_team", "home_team"], axis=1, inplace=True)
    for position in ["DEF", "GKP", "FWD", "MID"]:
        data_position = test_data[test_data["position"].isin([position])]
        for stat in position_stats[position]:
            print(stat)
            data_position = get_all_players_last_stats_test(data_position, stat)
            data_position = get_all_players_last_stats_test(
                data_position, stat, long_term_stats
            )
        if position != "GKP":
            print(data_position.columns)
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
        data_position.to_csv(f"test_{position}.csv")
