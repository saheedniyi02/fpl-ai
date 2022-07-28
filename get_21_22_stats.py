import requests

general_info = requests.get(
    "https://fantasy.premierleague.com/api/bootstrap-static/"
).json()
player_infos = general_info["elements"]
gameweek = 1
all_stats = []
for player_info in player_infos:
    id = player_info["id"]
    name = player_info["first_name"] + " " + player_info["second_name"]
    link = f"https://fantasy.premierleague.com/api/element-summary/{id}/"
    try:
        print(id)
        stats_summary = requests.get(link).json()
        stats_2022 = stats_summary["history_past"][-1]
        stats_2022["name"] = name
        all_stats.append(stats_2022)
    except:
        pass

import pandas as pd

print(all_stats)
df = pd.DataFrame(all_stats)
print(df)
df.to_csv("cleaned_players_21_22_2.csv")
