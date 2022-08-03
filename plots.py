# import matplotlib.pyplot as plt
# import pandas as pd
# from config import no_plotted_players  # , x_ticks
# import plotly.express as px

# predicted_fwds = pd.read_csv("predicted_dataset/forwards_points.csv")
# predicted_fwds["name"] = predicted_fwds["name"].replace({"Diogo Teixeira da Silva": "Diogo jota","Cristiano Ronaldo dos Santos Aveiro": "Cristaino Ronaldo","Gabriel Fernando de Jesus": "Gabriel Jesus","Darwin Núñez Ribeiro": "Darwin Núñez",})
# predicted_defs = pd.read_csv("predicted_dataset/defenders_points.csv")
# predicted_gks = pd.read_csv("predicted_dataset/goalkeepers_points.csv")
# predicted_mids = pd.read_csv("predicted_dataset/midfielders_points.csv")
# plot predicted_fwds
# long_df = px.data.medals_long()
# fig = px.bar(long_df, x="nation", y="count", color="medal", title="Long-Form Input")
# fig.show()
# fig.write_image("plots/fig1.png")
"""
fig = plt.figure(figsize=(15, 10), facecolor="white")
plt.xlabel("Strikers", size=30)
ax = plt.axes()
ax.set_facecolor("white")
plt.xticks(rotation=x_ticks, fontsize=14)
plt.ylabel("Predicted points", size=30)
plt.bar(
    "name",
    "points",
    width=0.3,
    align="edge",
    bottom=5,
    data=predicted_fwds.head(no_plotted_players).sort_values("points", ascending=True),
)

plt.savefig("plots/predicted_forwards.jpg", bbox_inches="tight")

# plot predicted_mids

fig = plt.figure(figsize=(10, 15))
fig.patch.set_facecolor(color=None)
plt.bar(
    "name",
    "points",
    data=predicted_mids.head(no_plotted_players).sort_values("points", ascending=True),
)

plt.xticks(rotation=x_ticks)
plt.xlabel("Midfielders")
plt.ylabel("Predicted points")
plt.savefig("plots/predicted_midfielders.jpg")


# plot predicted_defs

fig = plt.figure(figsize=(10, 15))
fig.patch.set_facecolor(color=None)
plt.bar(
    "name",
    "points",
    data=predicted_defs.head(no_plotted_players).sort_values("points", ascending=True),
)

plt.xticks(rotation=x_ticks)
plt.xlabel("Defenders")
plt.ylabel("Predicted points")
plt.savefig("plots/predicted_defenders.jpg")


# plot predicted_gks
fig = plt.figure(figsize=(10, 15))
fig.patch.set_facecolor(color=None)
plt.bar(
    "name",
    "points",
    data=predicted_gks.head(no_plotted_players).sort_values("points", ascending=True),
)
plt.xticks(rotation=x_ticks)
plt.xlabel("Goalkeepers")
plt.ylabel("Predicted points")
plt.savefig("plots/predicted_goalkeepers.jpg")"""
