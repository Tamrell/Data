import matplotlib.pyplot as plt

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

fig, ax = plt.subplots()
ax.scatter(xfactories,yfactories,marker='s')
ax.scatter(xsensors,ysensors)
plt.xlabel('x-coordinaat')
plt.ylabel('y-coordinaat')
plt.axis('equal')

for i,txt in enumerate(namesfactories):
	ax.annotate(txt, (xfactories[i],yfactories[i]))
for i, txt in enumerate(namessensors):
	ax.annotate(txt, (xsensors[i],ysensors[i]))

plt.show(fig)