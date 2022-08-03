import pandas as pd


def get_predictions(formation="433", clubs=None):

    """
    clubs is the list of clubs
    """

    predicted_fwds = pd.read_csv("predicted_dataset/forwards_points.csv")
    predicted_fwds["name"] = predicted_fwds["name"].replace(
        {
            "Diogo Teixeira da Silva": "Diogo jota",
            "Cristiano Ronaldo dos Santos Aveiro": "Cristaino Ronaldo",
            "Gabriel Fernando de Jesus": "Gabriel Jesus",
            "Darwin Núñez Ribeiro": "Darwin Núñez",
        }
    )
    injured = ["Richarlison de Andrade", "Diogo jota", "Ben Chilwell"]
    predicted_fwds = predicted_fwds[~predicted_fwds["name"].isin(injured)]
    predicted_defs = pd.read_csv("predicted_dataset/defenders_points.csv")
    predicted_defs = predicted_defs[~predicted_defs["name"].isin(injured)]
    predicted_gks = pd.read_csv("predicted_dataset/goalkeepers_points.csv")
    predicted_mids = pd.read_csv("predicted_dataset/midfielders_points.csv")
    if clubs:
        predicted_fwds = predicted_fwds[predicted_fwds["team_x"].isin(clubs)]
        predicted_defs = predicted_defs[predicted_defs["team_x"].isin(clubs)]
        predicted_mids = predicted_mids[predicted_mids["team_x"].isin(clubs)]
        predicted_gks = predicted_gks[predicted_gks["team_x"].isin(clubs)]
        print(predicted_gks["name"])
    return {
        "goalkeepers": list(predicted_gks["name"])[0],
        "defenders": list(predicted_defs["name"])[: int(formation[0])],
        "midfielders": list(predicted_mids["name"])[: int(formation[1])],
        "forwards": list(predicted_fwds["name"])[: int(formation[2])],
    }


def get_full_squad():

    """
    clubs is the list of clubs
    """

    predicted_fwds = pd.read_csv("predicted_dataset/forwards_points.csv")
    predicted_fwds["name"] = predicted_fwds["name"].replace(
        {
            "Diogo Teixeira da Silva": "Diogo jota",
            "Cristiano Ronaldo dos Santos Aveiro": "Cristaino Ronaldo",
            "Gabriel Fernando de Jesus": "Gabriel Jesus",
            "Darwin Núñez Ribeiro": "Darwin Núñez",
        }
    )
    injured = ["Richarlison de Andrade", "Diogo jota"]
    predicted_fwds = predicted_fwds[~predicted_fwds["name"].isin(injured)]
    predicted_defs = pd.read_csv("predicted_dataset/defenders_points.csv")
    predicted_gks = pd.read_csv("predicted_dataset/goalkeepers_points.csv")
    predicted_mids = pd.read_csv("predicted_dataset/midfielders_points.csv")

    return {
        "goalkeepers": list(predicted_gks["name"])[:2],
        "defenders": list(predicted_defs["name"])[:5],
        "midfielders": list(predicted_mids["name"])[:5],
        "forwards": list(predicted_fwds["name"])[:3],
    }


print(get_predictions(formation="343"))
