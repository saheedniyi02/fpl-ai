import requests

#general_information=requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")
#general_information=general_information.json()
#player_infos=general_information["element_types"]
#print(player_infos)

def get_player_fixture_info(id,gameweek):
	player_info=requests.get(f"https://fantasy.premierleague.com/api/element-summary/{id}/").json()
	fixture=player_info["fixtures"][gameweek-1]
	home_team=fixture["team_h"]
	away_team=fixture["team_a"]
	kickoff_time=fixture["kickoff_time"]
	is_home=fixture["is_home"]

def get_team_name(id):
	general_information=requests.get("https://fantasy.premierleague.com/api/bootstrap-static/").json()
	teams=general_information["teams"]
	for team in teams:
		if team["id"]==id:
			return team["name"]
					
def get_player_position(element_type):
			general_information=requests.get("https://fantasy.premierleague.com/api/bootstrap-static/").json()
			positions=general_information["element_types"]
			for position in positions:
				if position["id"]==element_type:
					return position["singular_name_short"]

			
print(get_player_position(3))		
#for id in range(len(player_infos)):
#	player_info=general_information["elements"][id]
#	name=player_info["first_name"]+" "+player_info["second_name"]
#	team_id=player_info["team"]
#	cost=player_info["now_cost"]
#    element_type=player_info["element_type"]
#	print(name,team_id,cost)



#id: id
#seasn=2022/23
#name: first_name, second_name
#team: team
#team_code: team_code
