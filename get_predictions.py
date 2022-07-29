import pandas as pd


def get_predictions(formation="442", clubs=None):

    """
    clubs is the list of clubs
    """
    predicted_fwds = pd.read_csv("predicted_dataset/forwards_points.csv")
    predicted_defs = pd.read_csv("predicted_dataset/defenders_points.csv")
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
    predicted_defs = pd.read_csv("predicted_dataset/defenders_points.csv")
    predicted_gks = pd.read_csv("predicted_dataset/goalkeepers_points.csv")
    predicted_mids = pd.read_csv("predicted_dataset/midfielders_points.csv")

    return {
        "goalkeepers": list(predicted_gks["name"])[:2],
        "defenders": list(predicted_defs["name"])[:5],
        "midfielders": list(predicted_mids["name"])[:5],
        "forwards": list(predicted_fwds["name"])[:3],
    }


print(get_predictions(formation="442", clubs=["Man City"]))
print(get_full_squad())
