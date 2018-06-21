import pandas,math,numpy
from bokeh.layouts import gridplot, row, column
from bokeh.io import output_file, show
from bokeh.plotting import figure

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

chemicals = list(set(pandas.Series(SData['Chemical']).values))

WindLinear = [float(i) for i in MData['Wind Direction Linear'].values]
WindSpline = [float(i) for i in MData['Wind Direction Spline'].values]

def getMeanSensorChemical(SD,sensor,chemical):
	readings = pandas.Series(SD.loc[(SD['Chemical'] == chemical) & (SD['Monitor'] == sensor)]['Reading']).values
	return numpy.mean(readings)

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

for factorie in factories:
	output_file('%s'%factorie)
	
	plot = figure(plot_width=1500,plot_height=500,title=factorie)
	plots = []
	for sensor in sensors:

		p1 = figure(plot_width=250,plot_height=250,title='%s_%s'%(sensor,'Methylosmolene'))
		p2 = figure(plot_width=250,plot_height=250,title='%s_%s'%(sensor,'Chlorodinine'))
		p3 = figure(plot_width=250,plot_height=250,title='%s_%s'%(sensor,'AGOC_3A'))
		p4 = figure(plot_width=250,plot_height=250,title='%s_%s'%(sensor,'Appluimonia'))

		overlap = []

		Methylosmolene = []
		MethylosmoleneTS = []

		Chlorodinine = []
		ChlorodinineTS = []

		AGOC_3A = []
		AGOC_3ATS = []

		Appluimonia = []
		AppluimoniaTS = []
		#find al the timestamps on which the wind blows from factorie to sensor
		for agreement in agreements:
			if factorie == agreement[20:23] and sensor == agreement[24:]:
				overlap.append(agreement[0:19])

		for index, row in SData.iterrows():
			if str(row['Timestamp']) in overlap:
				if row['Monitor'] == int(sensor[-1]):
					if row['Chemical'] == 'Methylosmolene':
						Methylosmolene.append(row['Reading'])
						MethylosmoleneTS.append(row['Timestamp'])
						MethylosmoleneTS = [i for i in range(len(Methylosmolene))]
						MethylosmoleneMean = getMeanSensorChemical(SData,sensor,'Methylosmolene')
						MethylosmoleneMean = [MethylosmoleneMean for i in range(len(Methylosmolene))]
						#print(factorie,sensor,row['Timestamp'],row['Chemical'],row['Reading'])
					elif row['Chemical'] == 'Chlorodinine':
						Chlorodinine.append(row['Reading'])
						ChlorodinineTS.append(row['Timestamp'])
						ChlorodinineTS = [i for i in range(len(Chlorodinine))]
						ChlorodinineMean = getMeanSensorChemical(SData,sensor,'Chlorodinine')
						ChlorodinineMean = [ChlorodinineMean for i in range(len(Chlorodinine))]
						#print(factorie,sensor,row['Timestamp'],row['Chemical'],row['Reading'])
					elif row['Chemical'] == 'AGOC-3A':
						AGOC_3A.append(row['Reading'])
						AGOC_3ATS.append(row['Timestamp'])
						AGOC_3ATS = [i for i in range(len(AGOC_3A))]
						AGOC_3AMean = getMeanSensorChemical(SData, sensor,'AGOC_3A')
						AGOC_3AMean = [AGOC_3AMean for i in range(len(AGOC_3A))]
						#print(factorie,sensor,row['Timestamp'],row['Chemical'],row['Reading'])
					elif row['Chemical'] == 'Appluimonia':
						Appluimonia.append(row['Reading'])
						AppluimoniaTS.append(row['Timestamp'])
						AppluimoniaTS = [i for i in range(len(Appluimonia))]
						AppluimoniaMean = getMeanSensorChemical(SData,sensor,'Appluimonia')
						AppluimoniaMean = [AppluimoniaMean for i in range(len(AppluimoniaTS))]
						#print(factorie,sensor,row['Timestamp'],row['Chemical'],row['Reading'])


		


		p1.circle(MethylosmoleneTS,Methylosmolene)
		p1.line(MethylosmoleneTS,)
		p1.line([i for i in range(len(Methylosmolene))],[MethylosmoleneMean for i in range(len(Methylosmolene))],color='orange')
		p2.circle(ChlorodinineTS,Chlorodinine)
		p2.line([i for i in range(len(Chlorodinine))],[ChlorodinineMean for i in range(len(Chlorodinine))],color='orange')
		p3.circle(AGOC_3ATS,AGOC_3A)
		p3.line([i for i in range(len(AGOC_3A))],[AGOC_3AMean for i in range(len(AGOC_3A))],color='orange')
		p4.circle(AppluimoniaTS,Appluimonia)
		p4.line([i for i in range(len(Appluimonia))],[AppluimoniaMean for i in range(len(Appluimonia))],color='orange')
		plots.append([p1,p2,p3,p4])

	grid = gridplot([[plots[i][0] for i in range(9)],[plots[i][1] for i in range(9)],[plots[i][2] for i in range(9)],[plots[i][3] for i in range(9)]],title=factorie)
	#grid = gridplot([[plots[0][0],plots[1][0]],[plots[0][1],plots[1][1]]])	
	show(grid)




























'''
for value in WindLinear:
	print(type(value))
	print(type(numpy.float(142)))

Base = range(len(WindLinear))

plot = figure(width=1500, plot_height=500, title=None)

plot.line(Base,WindLinear,color='blue',legend='Linear')
plot.line(Base,WindSpline,color='red',legend='Spline')
plot.legend.location = "top_left"
plot.legend.click_policy="hide"
show(plot)

for i in range(1,len(WindLinear)):
	if abs(WindLinear[i-1]-WindLinear[i]) > 100:
		WindLinearNew.append(WindLinear[i]+360)
	else:
		WindLinearNew.append(WindLinear[i])

for i in range(len(WindLinear)):
	print(WindLinear[i],WindLinearNew[i])

WindLinear = WindLinearNew


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
show(grid)'''