import pandas as pd
from pulp import *


predicted_fwds = pd.read_csv("predicted_dataset/forwards_points.csv",index_col=0)
predicted_fwds["name"] = predicted_fwds["name"].replace({
        "Diogo Teixeira da Silva": "Diogo jota",
        "Cristiano Ronaldo dos Santos Aveiro": "Cristaino Ronaldo",
        "Gabriel Fernando de Jesus": "Gabriel Jesus",
        "Darwin Núñez Ribeiro": "Darwin Núñez",})
injured=["Richarlison de Andrade","Diogo jota"]
predicted_fwds=predicted_fwds[~predicted_fwds["name"].isin(injured)]
predicted_fwds["position"]="FWD"
predicted_defs = pd.read_csv("predicted_dataset/defenders_points.csv",index_col=0)
predicted_defs["position"]="DEF"
predicted_mids = pd.read_csv("predicted_dataset/midfielders_points.csv",index_col=0)
predicted_mids["position"]="MID"
predicted_gks = pd.read_csv("predicted_dataset/goalkeepers_points.csv",index_col=0)
predicted_gks["position"]="GK"
predictions=pd.concat([predicted_fwds,predicted_defs,predicted_mids,predicted_gks])


POS = predictions["position"].unique()
CLUBS = predictions["team_x"].unique()
BUDGET = 1000
pos_available = {
    'DEF': 5,
    'FWD': 3,
    'MID': 5,
    'GK': 2,
}

# Initialize Variables
print(predictions.index)
names = [predictions["name"].loc[i] for i in predictions.index]
print(1)
teams = [predictions["team_x"].loc[i] for i in predictions.index]
positions = [predictions["position"].loc[i] for i in predictions.index]
prices = [predictions["value"].loc[i] for i in predictions.index]
points = [predictions["points"].loc[i] for i in predictions.index]
players = [LpVariable("player_" + str(i), cat="Binary") for i in predictions["name"]]
print(predictions)

# Initialize the problem
prob = LpProblem("FPL Player Choices", LpMaximize)

# Define the objective
prob += lpSum(players[i] * points[i] for i in range(len(predictions))) 
# Objective

# Build the constraints
prob += lpSum(players[i] * predictions.value[predictions.index[i]] for i in range(len(predictions))) <= BUDGET # Budget Limit

for pos in POS:
	prob += lpSum(players[i] for i in range(len(predictions)) if positions[i] == pos) <= pos_available[pos] # Position Limit

for club in CLUBS:
	prob += lpSum(players[i] for i in range(len(predictions)) if teams[i] == club) <= 3 # Club Limit
	
prob.solve()


for v in prob.variables():
    if v.varValue != 0:
    	name = predictions.name[int(v.name.split("_")[1])]
    	club = predictions.team_x[int(v.name.split("_")[1])]
    	position = predictions.position[int(v.name.split("_")[1])]
    	point = predictions.points[int(v.name.split("_")[1])]
    	price = predictions.value[int(v.name.split("_")[1])]
    	print(name, position, club, point, price, sep=" | ")
    	

score = str(prob.objective)
constraint = [str(const) for const in prob.constraints.values()][0]
for v in prob.variables():
	score = score.replace(v.name, str(v.varValue))
	constraint = constraint.replace(v.name, str(v.varValue))

score_pretty = " + ".join( re.findall('[0-9\.]*\*1.0', score) )
constraint_pretty = " + ".join( re.findall('[0-9\.]*\*1.0', constraint) )

print("Constraint: ")
print(constraint_pretty + " = " + str(eval(constraint_pretty)))
print()
print("Score: ")
print(score_pretty + " = " + str(eval(score_pretty)))