import pandas,math,numpy
from bokeh.layouts import gridplot

SData = pandas.read_excel('../../Final Data/Sensor Data.xlsx')
MData = pandas.read_excel('../../Final Data/Meteorological Interpolated.xlsx')

FactoriesInput = pandas.read_csv('../../Final Data/Factories.csv')
SensorsInput = pandas.read_csv('../../Final Data/Sensors.csv')

factories = {}
sensors = {}

for index,row in FactoriesInput.iterrows():
	factories[row['Factory']] = [row['X'],row['Y']]
for index,row in SensorsInput.iterrows():
	sensors[row['Sensor']] = [row['X'],row['Y']]

def getAngles(factories,sensors):
	angles = {}
	for factorie in factories:
		for sensor in sensors:
			dx = sensors[sensor][0] - factories[factorie][0]
			dy = sensors[sensor][1] - factories[factorie][1]
			angles['%s_%s'%(factorie,sensor)] = math.degrees(numpy.arctan2(dy,dx)+(0.5*numpy.pi))
	return angles

angles = getAngles(factories,sensors)

def compareWDvsAngles(SD,MD,angles,dr):
	agreements = {}
	for index, row in MD.iterrows():
		for angle in angles:
			rw = row['Wind Direction Linear']
			ang = angles[angle]
			ts = row['Timestamp']
			if rw >= ang-dr and rw <= ang+dr:
				agreements['%s_%s_%s'%(ts,angle[0:3],angle[4:])] = ang-rw
				#print(row['Timestamp'],angle,angles[angle],row['Wind Direction Linear'])
	return agreements		

agreements = compareWDvsAngles(SData,MData,angles,10)

from bokeh.io import output_file, show
from bokeh.layouts import gridplot
from bokeh.palettes import Viridis3
from bokeh.plotting import figure

output_file("layout_grid.html")

x = list(range(11))
y0 = x
y1 = [10 - i for i in x]
y2 = [abs(i - 5) for i in x]
y3 = [i**2 for i in x]

# create three plots
p1 = figure(plot_width=250, plot_height=250, title=None)
p1.circle(x, y0, size=10, color=Viridis3[0])
p2 = figure(plot_width=250, plot_height=250, title=None)
p2.triangle(x, y1, size=10, color=Viridis3[1])
p3 = figure(plot_width=250, plot_height=250, title=None)
p3.square(x, y2, size=10, color=Viridis3[2])
p4 = figure(plot_width=250, plot_height=250, title=None)
p4.circle(x,y3,size=10,color=Viridis3[1])

# make a grid
grid = gridplot([[p1, p2, p4], [None, p3, p4]])

# show the results
show(grid)