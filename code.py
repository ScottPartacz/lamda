# %%
import csv
from functools import reduce
import json

data = []
neighborhoods = []

with open ("911_Calls_for_Service_(Last_30_Days).csv") as file:

    data = [{x: y for x,y in row.items()} for row in csv.DictReader(file)]
        

data = list(filter(lambda x: x["zip_code"] != "0" and x["neighborhood"] != "" and x["dispatchtime"] != "" and x["totaltime"] != "" and x["totalresponsetime"] != "", data))


print("avg totalresponsetime: ",reduce(lambda x,y: x + y, list(map(lambda x: float(x["totalresponsetime"]),data)))/len(data))

print("avg dispatchtime: ",reduce(lambda x,y: x + y, list(map(lambda x: float(x["dispatchtime"]),data)))/len(data))

print("avg totaltime: ",reduce(lambda x,y: x + y, list(map(lambda x: float(x["totaltime"]),data)))/len(data))


for x in data:
   if x["neighborhood"] not in neighborhoods:
       neighborhoods.append(x["neighborhood"])

for z in neighborhoods:
    print("\n" + z + "\n")
    print("avg totalresponsetime: ",reduce(lambda x,y: x + y, list(map(lambda x: float(x["totalresponsetime"]),list(filter(lambda x: x["neighborhood"] == z,data)))))/len(list(filter(lambda x: x["neighborhood"] == z,data))))

    print("avg dispatchtime: ",reduce(lambda x,y: x + y, list(map(lambda x: float(x["dispatchtime"]),list(filter(lambda x: x["neighborhood"] == z,data)))))/len(list(filter(lambda x: x["neighborhood"] == z,data))))

    print("avg totaltime: ",reduce(lambda x,y: x + y, list(map(lambda x: float(x["totaltime"]),list(filter(lambda x: x["neighborhood"] == z,data)))))/len(list(filter(lambda x: x["neighborhood"] == z,data))))

file = open("data.json","w")
file = json.dump(data,file)







