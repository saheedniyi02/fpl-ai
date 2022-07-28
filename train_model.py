
import pandas as pd
#goal_keepers

#defenders
#midfielders

#fowards

train_fwd=pd.read_csv("train_FWD.csv",index_col=0)
test_fwd=pd.read_csv("test_FWD.csv",index_col=0)

data_fwd_copy["index"]=data_fwd_copy["name"]+data_fwd_copy["kickoff_time"].astype("str")
data_fwd_copy=data_fwd_copy.set_index("index")
data_fwd_copy.drop(["kickoff_time"],axis=1, inplace=True)

test_data_copy["index"]=test_data_copy["name"]+test_data_copy["kickoff_time"].astype("str")
test_data_copy=test_data_copy.set_index("index")
test_data_copy.drop(["kickoff_time"],axis=1, inplace=True)

target=data_fwd_copy[["minutes","name"]]
data_fwd_copy.drop(["total_points","minutes","name"],axis=1, inplace=True)
test_data_copy.drop(["total_points","minutes","name"],axis=1, inplace=True)

for col in data_fwd_copy.columns:
    if data_fwd_copy[col].dtype=="object":
        data_fwd_copy[col]=pd.factorize(data_fwd_copy[col])[0]
        test_data_copy[col]=pd.factorize(test_data_copy[col])[0]
        
 data_fwd_copy["was_home"]=data_fwd_copy["was_home"].replace({True:0,False:1})
test_data_copy["was_home"]=test_data_copy["was_home"].replace({True:0,False:1})
test_data_copy=test_data_copy[data_fwd_copy.columns]
model=Pipeline([("imp",SimpleImputer()),("scaler",RobustScaler()),("model",RandomForestClassifier(verbose=2,n_estimators=1000))])
x,val,y,y_val=train_test_split(data_fwd_copy,target["name"],test_size=0.1,random_state=0)
y=target["minutes"].loc[y.index]
y_val=target["minutes"].loc[y_val.index]
model=CatBoostClassifier(verbose=100,scale_pos_weight=2.5,random_state=0,use_best_model=True,early_stopping_rounds=200, learning_rate=0.01,n_estimators=10000)
model.fit(x,y,eval_set=(val,y_val))
confusion_matrix(model.predict(val),y_val)
accuracy_score(model.predict(val),y_val)
f1_score(model.predict(val),y_val)
test_data_copy.drop("minutes",axis=1,inplace=True)
test_data_2["minutes"]=model.predict(test_data_copy)
data_fwd_copy=data_fwd_2[data_fwd_2["minutes"]>0]
test_data_2=test_data_2[test_data_2["minutes"]>0]
data_fwd_copy["index"]=data_fwd_copy["name"]+data_fwd_copy["kickoff_time"].astype("str")
data_fwd_copy=data_fwd_copy.set_index("index")
data_fwd_copy.drop(["kickoff_time"],axis=1, inplace=True)
test_data_2["index"]=test_data_2["name"]+test_data_2["kickoff_time"].astype("str")
test_data_2=test_data_2.set_index("index")
test_data_2.drop(["kickoff_time"],axis=1, inplace=True)
target=data_fwd_copy[["total_points","name"]]
data_fwd_copy.drop(["total_points","minutes","name"],axis=1, inplace=True)
test_data_2.drop(["total_points","minutes","name"],axis=1, inplace=True)
for col in data_fwd_copy.columns:
    if data_fwd_copy[col].dtype=="object":
        data_fwd_copy[col]=pd.factorize(data_fwd_copy[col])[0]
        test_data_2[col]=pd.factorize(test_data_2[col])[0]
        
def clean_points(val):
  if val<=1:
    return 1
  elif val<=5:
    return 2
  elif val>=6:
    return 3

data_fwd_copy["was_home"]=data_fwd_copy["was_home"].replace({True:0,False:1})
test_data_2["was_home"]=test_data_2["was_home"].replace({True:0,False:1})

x,val,y,y_val=train_test_split(data_fwd_copy,target["name"],test_size=0.1,random_state=0)

y=target["total_points"].loc[y.index]
y_val=target["total_points"].loc[y_val.index]
model=Pipeline([("imp",SimpleImputer()),("scaler",StandardScaler()),("model",RandomForestClassifier(verbose=2,n_estimators=1000))])
model.fit(x,y,eval_set=(val,y_val))
accuracy_score(model.predict(val),y_val)
confusion_matrix(model.predict(val),y_val)
feature_importance=pd.DataFrame({"column":x.columns,"imp":model.feature_importances_}).sort_values("imp", ascending=False)#
test_data_2["points"]=model.predict(test_data_2)
test_data_2["points"].sort_values(ascending=False)