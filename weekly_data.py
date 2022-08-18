import requests
import pandas as pd


def get_player_fixture_info(id):
    player_info = requests.get(
        f"https://fantasy.premierleague.com/api/element-summary/{id}/"
    ).json()
    fixture = player_info["fixtures"][0]
    home_team = get_team_name(fixture["team_h"])
    away_team = get_team_name(fixture["team_a"])
    kickoff_time = fixture["kickoff_time"]
    is_home = fixture["is_home"]
    return home_team, away_team, kickoff_time, is_home


def get_gameweek_result(id, gameweek):
    "returns a dictionary of the statistics from the gameweek"
    gameweek_results = requests.get(
        f"https://fantasy.premierleague.com/api/element-summary/{id}/"
    ).json()
    return gameweek_results["history"][gameweek - 1]


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


general_info = requests.get(
    f"https://fantasy.premierleague.com/api/bootstrap-static/"
).json()
player_infos = general_info["elements"]
gameweek = 2


gameweek_fixture = pd.read_csv(f"datasets/week{gameweek}.csv")


def get_previous_fixture(matchday, name):
    # load week's fixture
    global gameweek_fixture
    gameweek_fixture_ = gameweek_fixture[gameweek_fixture["name"] == name]
    return (
        gameweek_fixture_["home_team"],
        gameweek_fixture_["away_team"],
        gameweek_fixture_["kickoff_time"],
        gameweek_fixture_["is_home"],
    )


# week 2 results
all_players = []
gameweek = 2
for player_info in player_infos:
    try:
        id = player_info["id"]
        print(id)
        name = player_info["first_name"] + " " + player_info["second_name"]
        team_id = player_info["team"]
        cost = player_info["now_cost"]
        element_type = player_info["element_type"]
        my_team = get_team_name(team_id)
        position = get_player_position(element_type)
        gameweek_result = get_gameweek_result(id, gameweek)
        home_team, away_team, kickoff_time, is_home = get_previous_fixture(
            gameweek, name
        )
        gameweek_result["id"]=id
        gameweek_result["name"] = name
        
        gameweek_result["cost"] = cost
        gameweek_result["position"] = position
        gameweek_result["home_team"] = home_team
        gameweek_result["away_team"] = away_team
        gameweek_result["team_x"] = my_team
        gameweek_result["opponent_team"] = get_team_name(
            gameweek_result["opponent_team"]
        )
        all_players.append(gameweek_result)

    except:
        continue

    # get x week result
print(all_players)
df = pd.DataFrame(all_players)
print(df)
df.to_csv(f"datasets/week{gameweek}_results.csv")


# WEEK 3 fixtures
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


# week2
for player_info in player_infos:
    id = player_info["id"]
    print(id)
    name = player_info["first_name"] + " " + player_info["second_name"]
    team_id = player_info["team"]
    cost = player_info["now_cost"]
    element_type = player_info["element_type"]
    my_team = get_team_name(team_id)
    position = get_player_position(element_type)
    home_team, away_team, kickoff_time, is_home = get_player_fixture_info(id)
    ids.append(id)
    names.append(name)
    costs.append(cost)
    positions.append(position)
    my_teams.append(my_team)
    home_teams.append(home_team)
    away_teams.append(away_team)
    kickoff_times.append(kickoff_time)
    is_homes.append(is_home)


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
df.to_csv("datasets/week3.csv")
