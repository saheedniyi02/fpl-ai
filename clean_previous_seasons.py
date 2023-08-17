import pandas as pd
from config import *
from utils import get_all_players_last_stats,create_features
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv("datasets/previous_seasons.csv", index_col=0)
#data["Goal_difference"]=data["team_h_score"]-data["team_a_score"]
data.drop(unused_columns,axis=1,inplace=True)

data["kickoff_time"]=pd.to_datetime(data["kickoff_time"])
data.sort_values(by="kickoff_time",inplace=True)
#print(data.columns)
for stat in history_stats:
    print(stat)
    data=get_all_players_last_stats(data,stat)

data=create_features(data,mean_features,std_features)
data.drop([f"last {no_last_stats} {stat}" for stat in history_stats],axis=1,inplace=True)

data.to_csv("cleaned_dataset/cleaned_previous_seasons.csv")
