import pandas as pd
import numpy as np
from utils import clean_minutes
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    mean_squared_error,
    mean_absolute_error,
    f1_score,
)

# load result
results = pd.read_csv("datasets/week2_results.csv")
results["minutes_actual"] = results["minutes"].apply(clean_minutes)

# load minutes
goalkeeper_minutes = pd.read_csv("predicted_dataset/goalkeepers_minutes.csv")
defender_minutes = pd.read_csv("predicted_dataset/defenders_minutes.csv")
midfielder_minutes = pd.read_csv("predicted_dataset/midfielders_minutes.csv")
foward_minutes = pd.read_csv("predicted_dataset/forwards_minutes.csv")
foward_minutes["name"] = foward_minutes["name"].replace(
    {"Erling Håland": "Erling Haaland"}
)

# load points
goalkeeper_points = pd.read_csv("predicted_dataset/goalkeepers_points.csv")
defender_points = pd.read_csv("predicted_dataset/defenders_points.csv")
midfielder_points = pd.read_csv("predicted_dataset/midfielders_points.csv")
foward_points = pd.read_csv("predicted_dataset/forwards_points.csv")
foward_points["name"] = foward_minutes["name"].replace(
    {"Erling Håland": "Erling Haaland"}
)


# calculate goalkeepers
print("\nGOALKEEPERS")
goalkeeper_minutes = pd.merge(
    goalkeeper_minutes,
    results[["name", "minutes_actual"]],
    left_on="name",
    right_on="name",
    how="left",
)

print(goalkeeper_minutes[pd.isna(goalkeeper_minutes["minutes_actual"])]["name"])
goalkeeper_minutes=goalkeeper_minutes.dropna()

print(
    confusion_matrix(
        goalkeeper_minutes["minutes"], goalkeeper_minutes["minutes_actual"]
    )
)
acc_score = accuracy_score(
    goalkeeper_minutes["minutes"], goalkeeper_minutes["minutes_actual"]
)
print(f"accuracy score {acc_score}")
f1_score_ = f1_score(
    goalkeeper_minutes["minutes"], goalkeeper_minutes["minutes_actual"]
)
print(f"F1 SCORE {f1_score_}")

goalkeeper_points = pd.merge(
    goalkeeper_points,
    results[["name", "minutes_actual", "total_points"]],
    left_on="name",
    right_on="name",
    how="left",
)

goalkeeper_points=goalkeeper_points.dropna()
rmse = np.sqrt(
    mean_squared_error(goalkeeper_points["points"], goalkeeper_points["total_points"])
)
print(f"Root Mean Square Error:{rmse}")


# calculate defenders
print("\nDEFENDERS")
defender_minutes = pd.merge(
    defender_minutes,
    results[["name", "minutes_actual"]],
    left_on="name",
    right_on="name",
    how="left",
)

print(defender_minutes[pd.isna(defender_minutes["minutes_actual"])]["name"])

defender_minutes=defender_minutes.dropna()
print(confusion_matrix(defender_minutes["minutes"], defender_minutes["minutes_actual"]))

acc_score = accuracy_score(
    defender_minutes["minutes"], defender_minutes["minutes_actual"]
)
print(f"Accuracy score {acc_score}")

f1_score_ = f1_score(defender_minutes["minutes"], defender_minutes["minutes_actual"])
print(f"F1 SCORE {f1_score_}")

defender_points = pd.merge(
    defender_points,
    results[["name", "minutes_actual", "total_points"]],
    left_on="name",
    right_on="name",
    how="left",
)
defender_points=defender_points.dropna()
rmse = np.sqrt(
    mean_squared_error(defender_points["points"], defender_points["total_points"])
)
print(f"Root Mean Square Error:{rmse}")


# calculate midfielders
print("\nMIDFIELDERS")
midfielder_minutes = pd.merge(
    midfielder_minutes,
    results[["name", "minutes_actual"]],
    left_on="name",
    right_on="name",
    how="left",
)

print(midfielder_minutes[pd.isna(midfielder_minutes["minutes_actual"])]["name"])

midfielder_minutes=midfielder_minutes.dropna()
print(
    confusion_matrix(
        midfielder_minutes["minutes"], midfielder_minutes["minutes_actual"]
    )
)


acc_score = accuracy_score(
    midfielder_minutes["minutes"], midfielder_minutes["minutes_actual"]
)
print(f"Accuracy score {acc_score}")

f1_score_ = f1_score(
    midfielder_minutes["minutes"], midfielder_minutes["minutes_actual"]
)
print(f"F1 SCORE {f1_score_}")

midfielder_points = pd.merge(
    midfielder_points,
    results[["name", "minutes_actual", "total_points"]],
    left_on="name",
    right_on="name",
    how="left",
)

midfielder_points=midfielder_points.dropna()

rmse = np.sqrt(
    mean_squared_error(midfielder_points["points"], midfielder_points["total_points"])
)

print(f"Root Mean Square Error:{rmse}")

# calculate fowards
print("\nFOWARDS")
foward_minutes = pd.merge(
    foward_minutes,
    results[["name", "minutes_actual"]],
    left_on="name",
    right_on="name",
    how="left",
)

print(foward_minutes[pd.isna(foward_minutes["minutes_actual"])]["name"])

foward_minutes=foward_minutes.dropna()

print(confusion_matrix(foward_minutes["minutes"], foward_minutes["minutes_actual"]))
acc_score = accuracy_score(foward_minutes["minutes"], foward_minutes["minutes_actual"])
print(f"Accuracy score {acc_score}")


f1_score_ = f1_score(foward_minutes["minutes"], foward_minutes["minutes_actual"])
print(f"F1 SCORE {f1_score_}")
foward_points = pd.merge(
    foward_points,
    results[["name", "minutes_actual", "total_points"]],
    left_on="name",
    right_on="name",
    how="left",
)

foward_points=foward_points.dropna()
rmse = np.sqrt(
    mean_squared_error(foward_points["points"], foward_points["total_points"])
)

print(f"Root Mean Square Error:{rmse}")
