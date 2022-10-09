import json

infile = open("US_fires_9_14-1.json",'r')

#creating another file to write the contents of json file 
jsonfile = open('readable_data.json','w')

us_fire_data = json.load(infile)
json.dump(us_fire_data,jsonfile,indent = 4)

#assigning empty list to store value to in future
lons,lats,brightness=[],[],[]

for fire in us_fire_data:
    #print(i)
    if fire['brightness'] > 450:
        lon = fire['longitude']
        lat = fire['latitude']
        bright = fire['brightness']

        #append the values to the corresponding list
        lons.append(lon)
        lats.append(lat)
        brightness.append(bright)

#print the 1st 3 values 
print(lons[1:3])
print(lats[1:3])
print(brightness[1:3])

from plotly.graph_objs import Scattergeo ,Layout
from plotly import offline

#pinpoints
data = {'type':'scattergeo',
        'lon':lons,
        'lat':lats,
        'marker':{
                #list in comprehension
                'size': [0.02*m for m in brightness],
                #'size': 15,
                'color':brightness,
                'colorscale':'Viridis',
                'reversescale':True,
                'colorbar':{'title':'Fire Intensity'}

        }}


mylayout = Layout(title='US Fires-California 9/14/2020 through 9/20/2020')

fig = {'data':data, 'layout':mylayout}
offline.plot(fig,filename='us_fires_california_09_14_through_09_20.html')















