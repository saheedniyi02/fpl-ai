import requests


def get_player_fixture_info(id, gameweek):
    player_info = requests.get(
        f"https://fantasy.premierleague.com/api/element-summary/{id}/"
    ).json()
    fixture = player_info["fixtures"][gameweek - 1]
    home_team = get_team_name(fixture["team_h"])
    away_team = get_team_name(fixture["team_a"])
    kickoff_time = fixture["kickoff_time"]
    is_home = fixture["is_home"]
    return home_team, away_team, kickoff_time, is_home


def get_team_name(id):
    general_information = requests.get(
        "https://fantasy.premierleague.com/api/bootstrap-static/"
    ).json()
    teams = general_information["teams"]
    for team in teams:
        if team["id"] == id:
            return team["name"]


def get_player_position(element_type):
    general_information = requests.get(
        "https://fantasy.premierleague.com/api/bootstrap-static/"
    ).json()
    positions = general_information["element_types"]
    for position in positions:
        if position["id"] == element_type:
            return position["singular_name_short"]


my_teams = []
home_teams = []
away_teams = []
kickoff_times = []
is_homes = []
positions = []
costs = []
names = []
ids = []
general_info = requests.get(
    f"https://fantasy.premierleague.com/api/bootstrap-static/"
).json()
player_infos = general_info["elements"]
gameweek = 1
for player_info in player_infos:
    id = player_info["id"]
    name = player_info["first_name"] + " " + player_info["second_name"]
    team_id = player_info["team"]
    cost = player_info["now_cost"]
    element_type = player_info["element_type"]
    my_team = get_team_name(team_id)
    position = get_player_position(element_type)
    print(id, my_team, position, name, cost)
    home_team, away_team, kickoff_time, is_home = get_player_fixture_info(id, gameweek)
    ids.append(id)
    names.append(name)
    costs.append(cost)
    positions.append(position)
    my_teams.append(my_team)
    home_teams.append(home_team)
    away_teams.append(away_team)
    kickoff_times.append(kickoff_time)
    is_homes.append(is_home)

import pandas as pd

df = pd.DataFrame()
df["id"] = ids
df["name"] = names
df["cost"] = costs
df["position"] = positions
df["home_team"] = home_teams
df["away_team"] = away_teams
df["kickoff_time"] = kickoff_times
df["is_home"] = is_homes
df["team_x"] = my_teams
df.to_csv("datasets/week1.csv")
