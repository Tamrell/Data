import pandas,numpy,math
from bokeh.io import output_file, show
from bokeh.layouts import column, widgetbox
from bokeh.plotting import figure

SD = pandas.read_excel('../Final Data/Sensor Data.xlsx')
MD = pandas.read_excel('../Final Data/Meteorological Interpolated.xlsx')

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

chemicals = ['Methylosmolene','Chlorodinine','AGOC-3A','Appluimonia']

def getAngles(factories,sensors):
	angles = {}
	for factorie in factories:
		for sensor in sensors:
			dx = sensors[sensor][0] - factories[factorie][0]
			dy = sensors[sensor][1] - factories[factorie][1]
			angles['%s_%s'%(factorie,sensor)] = math.degrees(numpy.arctan2(dy,dx)+(0.5*numpy.pi))
	return angles

#angles = getAngles(factories,sensors)

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

#agreements = compareWDvsAngles(SD,MD,angles,10)

'''
readingDots = []
datetimeDots = []

for agreement in agreements:
	if agreement[-7:] == 'Sensor2' and agreement[-11:-8] == 'RFE':
		try:
			readingDot = pandas.Series(SD.loc[(SD['Timestamp'] == agreement[0:19]) & (SD['Chemical'] == 'Methylosmolene') & (SD['Monitor'] == 2)]['Reading']).values
			datetimeDot = pandas.Series(SD.loc[(SD['Timestamp'] == agreement[0:19]) & (SD['Chemical'] == 'Methylosmolene') & (SD['Monitor'] == 2)]['Timestamp']).values
			readingDots.append(readingDot[0])
			datetimeDots.append(datetimeDot[0])
		except:
			pass

print(readingDots)
output = {}
reading = pandas.Series(SD.loc[(SD['Chemical'] == 'Methylosmolene') & (SD['Monitor'] == 2)]['Reading']).values
readingMean = numpy.mean(reading)
datetime = pandas.Series(SD.loc[(SD['Chemical'] == 'Methylosmolene') & (SD['Monitor'] == 2)]['Timestamp']).values
output[1] = figure(plot_width=1000, plot_height=250, title='Methylosmolene',y_range=(0,5))
output[1].line(datetime,reading)
output[1].line(datetime,readingMean,color='orange')
output[1].circle(datetimeDots,readingDots,fill_color='red')
show(column([output[1]]))'''


def plotEverything(factoies,sensors,chemicals,MD,SD,ranger):
	everything = []
	angles = getAngles(factories,sensors)
	agreements = compareWDvsAngles(SD,MD,angles,ranger)
	Methylosmolene = []
	Chlorodinine = []
	AGOC3A = []
	Appluimonia = []
	for sensor in sensors:
		for factorie in factories:
			for chemical in chemicals:
				for agreement in agreements:
					readingDot = pandas.Series(SD.loc[(SD['Timestamp'] == agreement[0:19]) & (SD['Chemical'] == chemical) & (SD['Monitor'] == sensor)]['Reading']).values
					datetimeDot = pandas.Series(SD.loc[(SD['Timestamp'] == agreement[0:19]) & (SD['Chemical'] == chemical) & (SD['Monitor'] == sensor)]['Date Time']).values
					if agreement[24:31] == sensor and agreement[20:23] == factorie:
						print(agreement)
		everything.append([agreement[0:19],agreement[20:23],agreement[24:31]])
	#print(everything)

plotEverything(factories,sensors,chemicals,MD,SD,10)


'''
def getReadingsAndDatetime(factorie,sensor,agreements):
	readingDots = []
	datetimeDots = []

	for agreement in agreements:
		if agreement[-7:] == sensor and agreement[-11:-8] == factorie:
			print(agreement[0:19])
			readingDot = pandas.Series(SD.loc[(SD['Timestamp'] == agreement[0:19]) & (SD['Chemical'] == 'Methylosmolene') & (SD['Monitor'] == sensor)]['Reading']).values
			datetimeDot = pandas.Series(SD.loc[(SD['Timestamp'] == agreement[0:19]) & (SD['Chemical'] == 'Methylosmolene') & (SD['Monitor'] == sensor)]['Timestamp']).values
			readingDots.append(readingDot[0])
			datetimeDots.append(datetimeDot[0])
		
	return readingDots,datetimeDots

for factorie in factories:
	for sensor in sensors:
		print(factorie,sensor)
		print(getReadingsAndDatetime(factorie,sensor,agreements))



def plotter(factorie,sensor,chemicals,SD,MD,agreements):
	readingDots = []
	datetimeDots = []

	for agreement in agreements:
		
			for chemical in chemicals:

			try:
				readingDot = pandas.Series(SD.loc[(SD['Timestamp'] == agreement[0:19]) & (SD['Chemical'] == chemical) & (SD['Monitor'] == sensor)]['Reading']).values
				datetimeDot = pandas.Series(SD.loc[(SD['Timestamp'] == agreement[0:19]) & (SD['Chemical'] == chemical) & (SD['Monitor'] == sensor)]['Timestamp']).values
				readingDots.append(readingDot[0])
				datetimeDots.append(datetimeDot[0])
			except:
				pass
	output = figure(plot_width=1000, plot_height=250, title='%s'%sensor,y_range=(0,5))
'''