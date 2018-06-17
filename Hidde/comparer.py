import os, pandas, numpy
import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file, show
from bokeh.models import GeoJSONDataSource
from bokeh.sampledata.sample_geojson import geojson

MD = pandas.read_excel('Meteorological Data.xlsx')

factories = {
    "RFE": [89,27],
    "KOF": [90,21],
    "RCT": [109,26],
    "ISB": [120,22]
}

sensors = {
    "Sensor1": [62,21],
    "Sensor2": [66,35],
    "Sensor3": [76,41],
    "Sensor4": [88,45],
    "Sensor5": [103,43],
    "Sensor6": [102,22],
    "Sensor7": [89,3],
    "Sensor8": [74,7],
    "Sensor9": [119,42]
}

#plot map of the city
def plotMap(factories,sensors):
    output_file('map.html')
    p = figure(background_fill_color='lightgrey',plot_width=750, plot_height=750)
    p.circle([factories[factorie][0] for factorie in factories],[factories[factorie][1] for factorie in factories],size=10, color='navy', alpha=0.5)
    p.square([sensors[sensor][0] for sensor in sensors],[sensors[sensor][1] for sensor in sensors], size=10, color='red',alpha=0.5)
    geo_source = GeoJSONDataSource(geojson=geojson)
    return p


#plot line between factorie and sensor
def drawLine(factorie,sensor):
    p = plotMap(factories,sensors)
    x = [sensors[sensor][0],factories[factorie][0]]
    y = [sensors[sensor][1],factories[factorie][1]]
    p.line(x,y,line_width=2)
    return p

#draw a range around a line between a factory and a sensor
def drawRange(factorie,sensor,angle):
    p = drawLine(factorie,sensor)
    xOld = sensors[sensor][0] - factories[factorie][0]
    yOld = sensors[sensor][1] - factories[factorie][1]
    x = xOld*numpy.cos(angle*numpy.pi/180) + yOld*numpy.sin(angle*numpy.pi/180)
    y = -xOld*numpy.sin(angle*numpy.pi/180) + yOld*numpy.cos(angle*numpy.pi/180)
    xNew = factories[factorie][0]+x
    yNew = factories[factorie][1]+y
    x = xOld*numpy.cos(angle*numpy.pi/180) + yOld*numpy.sin(angle*numpy.pi/180)
    y = -xOld*numpy.sin(angle*numpy.pi/180) + yOld*numpy.cos(angle*numpy.pi/180)
    xNew = factories[factorie][0]+x
    yNew = factories[factorie][1]+y
    p.line([factories[factorie][0],xNew],[factories[factorie][1],yNew],line_width=2,color='red')
    return p

# bokeh serv -> updaten    

show(drawRange('RFE','Sensor3',10))

def drawWindDirection(timestamp,factorie):
    p = plotMap(factories,sensors)
    selected = pandas.Series(MD.loc[(MD['Date'] == timestamp)]['Wind Direction']).values
    #selected = pandas.Series(SD.loc[(SD['Monitor'] == 1) & (SD['Chemical'] == 'Methylosmolene') & (SD['Reading'] < 25)]['Reading']).values

    return(selected)

print(drawWindDirection(pandas.Timestamp('2016-04-01 00'),'RFE'))

'''
print(MD['Date'])
def drawWind(p,timestamp,factorie):
    print(MD['Date'])
    direction = pandas.Series(MD.loc[MD['Date'] == timestamp]['Wind Direction']).values
    alpha = direction*numpy.pi/180
    y1 = 50-factories[factorie][0]
    x1 = y1*numpy.tan(alpha)
    y2 = 0-factories[factorie][1]
    x2 = y2*numpy.tan(alpha)
    xNew = [factories[factorie][0]+x1,factories[factorie][0]+x2]
    print(xNew)

drawWind('p','01-04-2016 00','RFE')


#D = pandas.read_excel('Sensor Data.xlsx')
#MD = pandas.read_excel('Meteorological Data.xlsx')

def getAnglesSF(sensors,factories):
    angles = {}
    for factorie in factories:
        for sensor in sensors:
            dx = factories[factorie][0] - sensors[sensor][0]
            dy = factories[factorie][1] - sensors[sensor][1]
            if dx != 0:
                angles['%s_%s'%(factorie,sensor)] = dy/dx
            else:
                angles['%s_%s'%(factorie,sensor)] = 0
    return angles

angles = getAnglesSF(sensors,factories)


def getCoordinates(locations):
    names = []
    x = []
    y = []
    for location in locations:
        names.append(location)
        x.append(locations[location][0])
        y.append(locations[location][1])
    return names,x,y

namesfactories,xfactories,yfactories = getCoordinates(factories)
namessensors,xsensors, ysensors = getCoordinates(sensors)

for angle in angles:
    x1 = factories[angle[0:3]][0]
    x2 = sensors[angle[4:]][0]
    if x1 >= x2:
        x = numpy.arange(x1,x2,-0.1)
    else:
        x = numpy.arange(x1,x2,0.1)
    y1 = factories[angle[0:3]][1] 
    y2 = sensors[angle[4:]][1]
    print(y1,y2)
    if y1 >= y2:
        y = numpy.arange(y1,y2,-0.1)
    else:
        y = numpy.arange(y1,y2,0.1)
    print(y)




fig, ax = plt.subplots()
plt.plot(x,y)
ax.scatter(xfactories,yfactories,marker='s')
ax.scatter(xsensors,ysensors)
plt.xlabel('x-coordinaat')
plt.ylabel('y-coordinaat')
plt.axis('equal')

for i,txt in enumerate(namesfactories):
    ax.annotate(txt, (xfactories[i],yfactories[i]))
for i, txt in enumerate(namessensors):
    ax.annotate(txt, (xsensors[i],ysensors[i]))

plt.savefig('map.jpg')
plt.show()

'''