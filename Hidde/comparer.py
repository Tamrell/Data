import os, pandas, numpy
import matplotlib.pyplot as plt

#D = pandas.read_excel('Sensor Data.xlsx')
#MD = pandas.read_excel('Meteorological Data.xlsx')

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
	print(angle,angles[angle],len(x))
	if len(x) > 0 and angles[angle] != 0:
		y = numpy.arange(y1,y2,angles[angle]/len(x))
	print(len(x),len(y))


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

