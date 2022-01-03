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

neighborhoods_list_dict = []

for z in neighborhoods:
    length = len(list(filter(lambda x: x["neighborhood"] == z,data)))
    mini_list = list(filter(lambda x: x["neighborhood"] == z,data))

    print("\n" + z + "\n")

    totalrestime_avg = reduce(lambda x,y: x + y, list(map(lambda x: float(x["totalresponsetime"]),mini_list)))/length
    print("avg totalresponsetime: ",totalrestime_avg)

    distime_avg = reduce(lambda x,y: x + y, list(map(lambda x: float(x["dispatchtime"]),mini_list)))/length
    print("avg dispatchtime: ",distime_avg)

    totaltime_avg = reduce(lambda x,y: x + y, list(map(lambda x: float(x["totaltime"]),mini_list)))/length
    print("avg totaltime: ",totaltime_avg)

    temp_dict = {"neighborhood": z,"avg_totalresponsetime":totalrestime_avg,"avg_dispatchtime":distime_avg,"totaltime_avg":totaltime_avg}
    neighborhoods_list_dict.append(temp_dict)

#print(neighborhoods_list_dict)
file = open("data.json","w")
file = json.dump(neighborhoods_list_dict,file)







