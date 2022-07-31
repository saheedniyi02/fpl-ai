import pandas as pd
import warnings

warnings.filterwarnings("ignore")
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.preprocessing import StandardScaler, RobustScaler, MinMaxScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    confusion_matrix,
    accuracy_score,
    f1_score,
)


# GOALKEEPERS
print("gkps")
train_gkp = pd.read_csv("cleaned_dataset/train_GK.csv", index_col=0)
test_gkp = pd.read_csv("cleaned_dataset/test_GKP.csv", index_col=0)
train_copy = train_gkp.copy()
test_copy = test_gkp.copy()

train_gkp["index"] = train_gkp["name"] + train_gkp["kickoff_time"].astype("str")
train_gkp = train_gkp.set_index("index")
train_gkp.drop(["kickoff_time"], axis=1, inplace=True)

test_gkp["index"] = test_gkp["name"] + test_gkp["kickoff_time"].astype("str")
test_gkp = test_gkp.set_index("index")
test_gkp.drop(["kickoff_time"], axis=1, inplace=True)

target = train_gkp[["minutes", "name"]]
train_gkp.drop(["total_points", "minutes"], axis=1, inplace=True)
test_gkp.drop(["total_points", "minutes"], axis=1, inplace=True)


for col in train_gkp.columns:
    if train_gkp[col].dtype == "object":
        if col not in ["team_x", "name"]:
            train_gkp[col] = pd.factorize(train_gkp[col])[0]
            test_gkp[col] = pd.factorize(test_gkp[col])[0]

train_gkp["was_home"] = train_gkp["was_home"].replace({True: 0, False: 1})
test_gkp["was_home"] = test_gkp["was_home"].replace({True: 0, False: 1})

test_gkp = test_gkp[train_gkp.columns]


model=Pipeline([("imp",SimpleImputer()),("scaler",StandardScaler()),("model",RandomForestClassifier(n_estimators=1000,max_depth=10,random_state=1))])

x, val, y, y_val = train_test_split(
    train_gkp.drop(["name", "team_x"], axis=1),
    target["name"],
    test_size=0.1,
    random_state=0,
)


y = target["minutes"].loc[y.index]
y_val = target["minutes"].loc[y_val.index]

model.fit(x, y)

print(confusion_matrix(model.predict(val), y_val))
print(accuracy_score(model.predict(val), y_val))

print(f1_score(model.predict(val), y_val))

test_copy["minutes"] = model.predict(test_gkp.drop(["name", "team_x"], axis=1))
test_copy[["name", "minutes", "team_x"]].to_csv(
    "predicted_dataset/goalkeepers_minutes.csv"
)
print(test_copy[["name", "minutes"]])

# only starting players
train_gkp = train_copy[train_copy["minutes"] > 0]
test_gkp = test_copy[test_copy["minutes"] > 0]


# predict points
train_gkp["index"] = train_gkp["name"] + train_gkp["kickoff_time"].astype("str")
train_gkp = train_gkp.set_index("index")
train_gkp.drop(["kickoff_time"], axis=1, inplace=True)

test_gkp["index"] = test_gkp["name"] + test_gkp["kickoff_time"].astype("str")
test_gkp = test_gkp.set_index("index")
test_gkp.drop(["kickoff_time"], axis=1, inplace=True)

target = train_gkp[["total_points", "name"]]
train_gkp.drop(["total_points", "minutes"], axis=1, inplace=True)
test_gkp.drop(["total_points", "minutes"], axis=1, inplace=True)

for col in train_gkp.columns:
    if train_gkp[col].dtype == "object":
        if col not in ["team_x", "name"]:
            train_gkp[col] = pd.factorize(train_gkp[col])[0]
            test_gkp[col] = pd.factorize(test_gkp[col])[0]

train_gkp["was_home"] = train_gkp["was_home"].replace({True: 0, False: 1})

test_gkp["was_home"] = test_gkp["was_home"].replace({True: 0, False: 1})

test_gkp = test_gkp[train_gkp.columns]

x, val, y, y_val = train_test_split(
    train_gkp.drop(["name", "team_x"], axis=1),
    target["name"],
    test_size=0.1,
    random_state=0,
)

y = target["total_points"].loc[y.index]

y_val = target["total_points"].loc[y_val.index]

model=Pipeline([("imp",SimpleImputer()),("scaler",StandardScaler()),("model", RandomForestRegressor(random_state=0,max_depth=8,n_estimators=1000))])

model.fit(x, y)
print(mean_squared_error(model.predict(val), y_val))
print(mean_absolute_error(model.predict(val), y_val))
test_gkp["points"] = model.predict(test_gkp.drop(["name", "team_x"], axis=1))

print(test_gkp["points"].sort_values(ascending=False))

test_gkp[["name", "points", "team_x"]].sort_values("points", ascending=False).to_csv(
    "predicted_dataset/goalkeepers_points.csv"
)

# DEFENDERS
print("defs")
train_def = pd.read_csv("cleaned_dataset/train_DEF.csv", index_col=0)
test_def = pd.read_csv("cleaned_dataset/test_DEF.csv", index_col=0)
train_copy = train_def.copy()
test_copy = test_def.copy()

train_def["index"] = train_def["name"] + train_def["kickoff_time"].astype("str")
train_def = train_def.set_index("index")
train_def.drop(["kickoff_time"], axis=1, inplace=True)

test_def["index"] = test_def["name"] + test_def["kickoff_time"].astype("str")
test_def = test_def.set_index("index")
test_def.drop(["kickoff_time"], axis=1, inplace=True)

target = train_def["minutes"]
train_def.drop(["total_points", "minutes"], axis=1, inplace=True)
test_def.drop(["total_points", "minutes"], axis=1, inplace=True)


for col in train_def.columns:
    if train_def[col].dtype == "object":
        if col not in ["team_x", "name"]:
            train_def[col] = pd.factorize(train_def[col])[0]
            test_def[col] = pd.factorize(test_def[col])[0]

train_def["was_home"] = train_def["was_home"].replace({True: 0, False: 1})
test_def["was_home"] = test_def["was_home"].replace({True: 0, False: 1})

test_def = test_def[train_def.columns]


model=Pipeline([("imp",SimpleImputer()),("scaler",StandardScaler()),("model",RandomForestClassifier(n_estimators=1000,max_depth=10,random_state=1))])

x, val, y, y_val = train_test_split(
    train_def.drop(["name", "team_x"], axis=1), target, test_size=0.1, random_state=0
)


model.fit(x, y)

print(confusion_matrix(model.predict(val), y_val))
print(accuracy_score(model.predict(val), y_val))

print(f1_score(model.predict(val), y_val))

test_copy["minutes"] = model.predict(test_def.drop(["name", "team_x"], axis=1))
test_copy[["name", "minutes", "team_x"]].to_csv(
    "predicted_dataset/defenders_minutes.csv"
)
print(test_copy[["name", "minutes"]])

# only starting players
train_def = train_copy[train_copy["minutes"] > 0]
test_def = test_copy[test_copy["minutes"] > 0]


# predict points
train_def["index"] = train_def["name"] + train_def["kickoff_time"].astype("str")
train_def = train_def.set_index("index")
train_def.drop(["kickoff_time"], axis=1, inplace=True)

test_def["index"] = test_def["name"] + test_def["kickoff_time"].astype("str")
test_def = test_def.set_index("index")
test_def.drop(["kickoff_time"], axis=1, inplace=True)

target = train_def["total_points"]
train_def.drop(["total_points", "minutes"], axis=1, inplace=True)
test_def.drop(["total_points", "minutes"], axis=1, inplace=True)

for col in train_def.columns:
    if train_def[col].dtype == "object":
        if col not in ["team_x", "name"]:
            train_def[col] = pd.factorize(train_def[col])[0]
            test_def[col] = pd.factorize(test_def[col])[0]

train_def["was_home"] = train_def["was_home"].replace({True: 0, False: 1})

test_def["was_home"] = test_def["was_home"].replace({True: 0, False: 1})

test_def = test_def[train_def.columns]

x, val, y, y_val = train_test_split(
    train_def.drop(["name", "team_x"], axis=1), target, test_size=0.1, random_state=0
)

model=Pipeline([("imp",SimpleImputer()),("scaler",StandardScaler()),("model", RandomForestRegressor(random_state=0,max_depth=8,n_estimators=1000))])

model.fit(x, y)
print(mean_squared_error(model.predict(val), y_val))
print(mean_absolute_error(model.predict(val), y_val))
test_def["points"] = model.predict(test_def.drop(["name", "team_x"], axis=1))

print(test_def["points"].sort_values(ascending=False))

test_def[["name", "points", "team_x"]].sort_values("points", ascending=False).to_csv(
    "predicted_dataset/defenders_points.csv"
)


# MIDFIELDERS
print("mids")
train_mid = pd.read_csv("cleaned_dataset/train_MID.csv", index_col=0)
test_mid = pd.read_csv("cleaned_dataset/test_MID.csv", index_col=0)
train_copy = train_mid.copy()
test_copy = test_mid.copy()

train_mid["index"] = train_mid["name"] + train_mid["kickoff_time"].astype("str")
train_mid = train_mid.set_index("index")
train_mid.drop(["kickoff_time"], axis=1, inplace=True)

test_mid["index"] = test_mid["name"] + test_mid["kickoff_time"].astype("str")
test_mid = test_mid.set_index("index")
test_mid.drop(["kickoff_time"], axis=1, inplace=True)

target = train_mid["minutes"]
train_mid.drop(["total_points", "minutes"], axis=1, inplace=True)
test_mid.drop(["total_points", "minutes"], axis=1, inplace=True)


for col in train_mid.columns:
    if train_mid[col].dtype == "object":
        if col not in ["team_x", "name"]:
            train_mid[col] = pd.factorize(train_mid[col])[0]
            test_mid[col] = pd.factorize(test_mid[col])[0]

train_mid["was_home"] = train_mid["was_home"].replace({True: 0, False: 1})
test_mid["was_home"] = test_mid["was_home"].replace({True: 0, False: 1})

test_mid = test_mid[train_mid.columns]


model=Pipeline([("imp",SimpleImputer()),("scaler",StandardScaler()),("model",RandomForestClassifier(n_estimators=1000,max_depth=10,random_state=1))])

x, val, y, y_val = train_test_split(
    train_mid.drop(["name", "team_x"], axis=1), target, test_size=0.1, random_state=0
)


model.fit(x, y)

print(confusion_matrix(model.predict(val), y_val))
print(accuracy_score(model.predict(val), y_val))

print(f1_score(model.predict(val), y_val))

test_copy["minutes"] = model.predict(test_mid.drop(["name", "team_x"], axis=1))
test_copy[["name", "minutes", "team_x"]].to_csv(
    "predicted_dataset/midfielders_minutes.csv"
)
print(test_copy[["name", "minutes"]])

# only starting players
train_mid = train_copy[train_copy["minutes"] > 0]
test_mid = test_copy[test_copy["minutes"] > 0]


# predict points
train_mid["index"] = train_mid["name"] + train_mid["kickoff_time"].astype("str")
train_mid = train_mid.set_index("index")
train_mid.drop(["kickoff_time"], axis=1, inplace=True)

test_mid["index"] = test_mid["name"] + test_mid["kickoff_time"].astype("str")
test_mid = test_mid.set_index("index")
test_mid.drop(["kickoff_time"], axis=1, inplace=True)

target = train_mid["total_points"]
train_mid.drop(["total_points", "minutes"], axis=1, inplace=True)
test_mid.drop(["total_points", "minutes"], axis=1, inplace=True)

for col in train_mid.columns:
    if train_mid[col].dtype == "object":
        if col not in ["team_x", "name"]:
            train_mid[col] = pd.factorize(train_mid[col])[0]
            test_mid[col] = pd.factorize(test_mid[col])[0]

train_mid["was_home"] = train_mid["was_home"].replace({True: 0, False: 1})

test_mid["was_home"] = test_mid["was_home"].replace({True: 0, False: 1})

test_mid = test_mid[train_mid.columns]

x, val, y, y_val = train_test_split(
    train_mid.drop(["name", "team_x"], axis=1), target, test_size=0.1, random_state=0
)


model=Pipeline([("imp",SimpleImputer()),("scaler",StandardScaler()),("model", RandomForestRegressor(random_state=0,max_depth=8,n_estimators=1000))])

model.fit(x, y)
print(mean_squared_error(model.predict(val), y_val))
print(mean_absolute_error(model.predict(val), y_val))
test_mid["points"] = model.predict(test_mid.drop(["name", "team_x"], axis=1))

print(test_mid["points"].sort_values(ascending=False))
test_mid[["name", "points", "team_x"]].sort_values("points", ascending=False).to_csv(
    "predicted_dataset/midfielders_points.csv"
)


# FORWARDS
print("fwds")
train_fwd = pd.read_csv("cleaned_dataset/train_FWD.csv", index_col=0)
test_fwd = pd.read_csv("cleaned_dataset/test_FWD.csv", index_col=0)
train_copy = train_fwd.copy()
test_copy = test_fwd.copy()

train_fwd["index"] = train_fwd["name"] + train_fwd["kickoff_time"].astype("str")
train_fwd = train_fwd.set_index("index")
train_fwd.drop(["kickoff_time"], axis=1, inplace=True)

test_fwd["index"] = test_fwd["name"] + test_fwd["kickoff_time"].astype("str")
test_fwd = test_fwd.set_index("index")
test_fwd.drop(["kickoff_time"], axis=1, inplace=True)

target = train_fwd[["minutes", "name"]]
train_fwd.drop(["total_points", "minutes"], axis=1, inplace=True)
test_fwd.drop(["total_points", "minutes"], axis=1, inplace=True)


for col in train_fwd.columns:
    if train_fwd[col].dtype == "object":
        if col not in ["team_x", "name"]:
            train_fwd[col] = pd.factorize(train_fwd[col])[0]
            test_fwd[col] = pd.factorize(test_fwd[col])[0]

train_fwd["was_home"] = train_fwd["was_home"].replace({True: 0, False: 1})
test_fwd["was_home"] = test_fwd["was_home"].replace({True: 0, False: 1})

test_fwd = test_fwd[train_fwd.columns]


model=Pipeline([("imp",SimpleImputer()),("scaler",StandardScaler()),("model",RandomForestClassifier(n_estimators=1000,max_depth=10,random_state=1))])

x, val, y, y_val = train_test_split(
    train_fwd.drop(["name", "team_x"], axis=1),
    target["name"],
    test_size=0.1,
    random_state=0,
)


y = target["minutes"].loc[y.index]
y_val = target["minutes"].loc[y_val.index]

model.fit(x, y)

print(confusion_matrix(model.predict(val), y_val))
print(accuracy_score(model.predict(val), y_val))

print(f1_score(model.predict(val), y_val))

test_copy["minutes"] = model.predict(test_fwd.drop(["name", "team_x"], axis=1))
test_copy[["name", "minutes", "team_x"]].to_csv(
    "predicted_dataset/forwards_minutes.csv"
)
print(test_copy[["name", "minutes"]])

# only starting players
train_fwd = train_copy[train_copy["minutes"] > 0]
test_fwd = test_copy[test_copy["minutes"] > 0]


# predict points
train_fwd["index"] = train_fwd["name"] + train_fwd["kickoff_time"].astype("str")
train_fwd = train_fwd.set_index("index")
train_fwd.drop(["kickoff_time"], axis=1, inplace=True)

test_fwd["index"] = test_fwd["name"] + test_fwd["kickoff_time"].astype("str")
test_fwd = test_fwd.set_index("index")
test_fwd.drop(["kickoff_time"], axis=1, inplace=True)

target = train_fwd[["total_points", "name"]]
train_fwd.drop(["total_points", "minutes"], axis=1, inplace=True)
test_fwd.drop(["total_points", "minutes"], axis=1, inplace=True)

for col in train_fwd.columns:
    if train_fwd[col].dtype == "object":
        if col not in ["team_x", "name"]:
            train_fwd[col] = pd.factorize(train_fwd[col])[0]
            test_fwd[col] = pd.factorize(test_fwd[col])[0]

train_fwd["was_home"] = train_fwd["was_home"].replace({True: 0, False: 1})

test_fwd["was_home"] = test_fwd["was_home"].replace({True: 0, False: 1})

test_fwd = test_fwd[train_fwd.columns]

x, val, y, y_val = train_test_split(
    train_fwd.drop(["name", "team_x"], axis=1),
    target["name"],
    test_size=0.1,
    random_state=0,
)

y = target["total_points"].loc[y.index]

y_val = target["total_points"].loc[y_val.index]

model=Pipeline([("imp",SimpleImputer()),("scaler",StandardScaler()),("model", RandomForestRegressor(random_state=0,max_depth=8,n_estimators=1000))])

model.fit(x, y)
print(mean_squared_error(model.predict(val), y_val))
print(mean_absolute_error(model.predict(val), y_val))
test_fwd["points"] = model.predict(test_fwd.drop(["name", "team_x"], axis=1))

print(test_fwd["points"].sort_values(ascending=False))

test_fwd[["name", "points", "team_x"]].sort_values("points", ascending=False).to_csv(
    "predicted_dataset/forwards_points.csv"
)
