import pandas, math, numpy, time
from bokeh.layouts import gridplot, row, column
from bokeh.io import output_file, show
from bokeh.plotting import figure

start = time.time()

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
			angles['%s_%s'%(factorie,sensor)] = math.degrees(numpy.arctan2(dy,dx)) #HOEK INVOEREN
	return angles

angles = getAngles(factories,sensors)

for angle in angles:
	if angles[angle] < 0:
		angles[angle] = angles[angle]+360
	print(angle,angles[angle])


def compareWDvsAngles(SD,MD,angles,dr):
	agreements = {}
	for index, row in MD.iterrows():
		for angle in angles:
			rw = row['Wind Direction Linear']
			ang = angles[angle]
			ts = row['Timestamp']
			if rw >= ang-dr and rw <= ang+dr:
				agreements['%s_%s_%s'%(ts,angle[0:3],angle[4:])] = math.degrees(ang-rw)
				#print(row['Timestamp'],angle,angles[angle],row['Wind Direction Linear'])
	return agreements	

agreements = compareWDvsAngles(SData,MData,angles,10)



'''
for factorie in factories:
	output_file('%s'%factorie)
	plots = []

	for sensor in sensors:

		p1 = figure(plot_width=250,plot_height=250,title='%s_%s'%(sensor,'Methylosmolene'), y_range = (0,5))
		p2 = figure(plot_width=250,plot_height=250,title='%s_%s'%(sensor,'Chlorodinine'), y_range = (0,5))
		p3 = figure(plot_width=250,plot_height=250,title='%s_%s'%(sensor,'AGOC_3A'), y_range = (0,5))
		p4 = figure(plot_width=250,plot_height=250,title='%s_%s'%(sensor,'Appluimonia'), y_range = (0,5))

		overlap = []

		Methylosmolene = []
		MethylosmoleneTS = []

		Chlorodinine = []
		ChlorodinineTS = []

		AGOC_3A = []
		AGOC_3ATS = []

		Appluimonia = []
		AppluimoniaTS = []

		for agreement in agreements:
			if factorie == agreement[20:23] and sensor == agreement[24:]:
				for chemical in chemicals:
					reading = pandas.Series(SData.loc[(SData['Timestamp'] == numpy.datetime64(agreement[0:19])) & (SData['Chemical'] == chemical) & (SData['Monitor'] == numpy.int64(sensor[-1]))]['Reading']).values
					if len(reading) == 1:
						reading = reading[0]
					#print(reading)
					if chemical == 'Methylosmolene':
						#print(reading)
						Methylosmolene.append(reading)
						MethylosmoleneTS.append(agreement[0:19])

					elif chemical == 'Chlorodinine':
						#print(reading)
						Chlorodinine.append(reading)
						ChlorodinineTS.append(agreement[0:19])
					elif chemical == 'AGOC-3A':
						#print(reading)
						AGOC_3A.append(reading)
						AGOC_3ATS.append(agreement[0:19])
					elif chemical == 'Appluimonia':
						#print(reading)
						Appluimonia.append(reading)
						AppluimoniaTS.append(agreement[0:19])

		MethylosmoleneTS = [i for i in range(len(Methylosmolene))]
		ChlorodinineTS = [i for i in range(len(Chlorodinine))]
		AGOC_3ATS = [i for i in range(len(AGOC_3A))]
		AppluimoniaTS = [i for i in range(len(Appluimonia))]

		Methylosmolene_Mean = [numpy.mean(pandas.Series(SData.loc[(SData['Chemical'] == 'Methylosmolene') & (SData['Monitor'] == numpy.int64(sensor[-1]))]['Reading']).values) for i in range(len(Methylosmolene))]
		Chlorodinine_Mean = [numpy.mean(pandas.Series(SData.loc[(SData['Chemical'] == 'Chlorodinine') & (SData['Monitor'] == numpy.int64(sensor[-1]))]['Reading']).values) for i in range(len(Chlorodinine))]
		AGOC_3A_Mean = [numpy.mean(pandas.Series(SData.loc[(SData['Chemical'] == 'AGOC-3A') & (SData['Monitor'] == numpy.int64(sensor[-1]))]['Reading']).values) for i in range(len(AGOC_3A))]
		Appluimonia_Mean = [numpy.mean(pandas.Series(SData.loc[(SData['Chemical'] == 'Appluimonia') & (SData['Monitor'] == numpy.int64(sensor[-1]))]['Reading']).values) for i in range(len(Appluimonia))]


		#print('Methylosmolene',len(Methylosmolene),len(MethylosmoleneTS),MethylosmoleneTS)
		#print('Chlorodinine', len(Chlorodinine), len(ChlorodinineTS))
		#print('AGOC-3A', len(AGOC_3A),len(AGOC_3ATS))
		#print('Appluimonia', len(Appluimonia),len(AppluimoniaTS))

		p1.circle(MethylosmoleneTS,Methylosmolene)
		p1.line(MethylosmoleneTS,Appluimonia_Mean, color='orange')

		p2.circle(ChlorodinineTS,Chlorodinine)
		p2.line(ChlorodinineTS,Chlorodinine_Mean, color='orange')

		p3.circle(AGOC_3ATS,AGOC_3A)
		p3.line(AGOC_3ATS,AGOC_3A_Mean, color='orange')

		p4.circle(AppluimoniaTS,Appluimonia)
		p4.line(AppluimoniaTS,Appluimonia_Mean, color='orange')

		plots.append([p1,p2,p3,p4])

	grid = gridplot([[plots[i][0] for i in range(9)],[plots[i][1] for i in range(9)],[plots[i][2] for i in range(9)],[plots[i][3] for i in range(9)]],title=factorie)
	#grid = gridplot([[plots[0][0],plots[1][0]],[plots[0][1],plots[1][1]]])	
	show(grid)


					
					#print(agreement[0:19],factorie,sensor,chemical,reading)


end = time.time()

print(end-start)
'''