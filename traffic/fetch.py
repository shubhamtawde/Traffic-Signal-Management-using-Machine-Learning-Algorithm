import requests 
import json
import pandas as pd
import numpy
import pickle
 
h='jhulelal chowk ghatkopar'
response = requests.get("https://geocode.search.hereapi.com/v1/geocode?q="+h+"&apiKey=0k30d8NNE3Pz6plpwT6YE6WJsiAwQ3ulsVjudVvZk_Q")
data= json.loads(response.text)
#data=json.dumps(d, indent=2)
#print(data)
for i in data["items"]:
      for m, n in i["position"].items():
            if m == 'lat':
                 lat = n
            if m == 'lng':
                 lon = n
print(lat,lon)
lat1=str(lat)
lon1=str(lon)  
#print(lat1,lon1)
response = requests.get("https://traffic.ls.hereapi.com//traffic/6.2/flow.json?bbox="+str(lat1)+","+str(lon1)+";"+str(lat1)+","+str(lon1)+"&apiKey=0k30d8NNE3Pz6plpwT6YE6WJsiAwQ3ulsVjudVvZk_Q")
#print(response.status_code) 
#print(json.dumps(json.loads(response.text), indent=2))
list1=h.split()
cap=list1[0].capitalize()
road_name=[]
road_direction=[]
road_length=[]
jam_factor=[]
speed=[]
data= json.loads(response.text)
for i in data["RWS"]:
      for j in i["RW"]:
        times = j['PBT']
        for k in j["FIS"]:
           #print(k)
           for l in k["FI"]:
                  for m,n in l["TMC"].items():
                    #print(type(n))
                    if (m == 'DE') :
                       rd=n
                       road_name.append(n)
                    if (m == 'QD') :
                       road_direction.append(n)
                    if (m == 'LE') :                     
                       road_length.append(n)
                  for g in l["CF"]:
                    for x,y in g.items():
                       if (x == 'JF'):
                          jam_factor.append(y)                   
                       if (x == 'SP'):
                          speed.append(y)
#print(road_name, road_direction,road_length,jam_factor,speed)
df = pd.DataFrame(list(zip(road_name, road_direction,road_length,jam_factor,speed)), columns =['Name', 'direction', 'length', 'JM','speed']) 
df.sort_values("direction", axis = 0, ascending = True, inplace = True, na_position ='last') 
row2 = df.iloc[0:4]
x=row2['Name'].tolist();
rslt_df = df[(df['direction'] == '-') & (df['Name'].isin(x))]
queue=(row2,rslt_df)
frames=pd.concat(queue)
frames.sort_values("Name", axis = 0, ascending = True,inplace = True, na_position ='last') 
print(frames)
jf=frames['JM'].tolist();
print(jf)
filename = 'trained_model.pkl'
loaded_model = pickle.load(open(filename, 'rb'))
person = pd.DataFrame()
person['road_1'] = [jf[0]]
person['road_2'] = [jf[2]]
person['road_3'] = [jf[4]]
person['road_4'] = [jf[6]]
person['road_5'] = [jf[1]]
person['road_6'] = [jf[3]]
person['road_7'] = [jf[5]]
person['road_8'] = [jf[7]]
print(person)
# the data is stored in Datadrame person
predicted_y = loaded_model.predict(person)
print(predicted_y[0])

#0k30d8NNE3Pz6plpwT6YE6WJsiAwQ3ulsVjudVvZk_Q
#and (n.find(cap)!=-1)
#elif(m == 'DE') and (n.find(cap)==-1):rd=n
#and (rd.find(cap)!=-1)
#and (rd.find(cap)!=-1)
# and (rd.find(cap)!=-1)
# and (rd.find(cap)!=-1)