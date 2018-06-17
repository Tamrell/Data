import pandas,numpy,math
from bokeh.io import output_file, show
from bokeh.layouts import column, widgetbox
from bokeh.plotting import figure

SD = pandas.read_excel('../Final Data/Sensor Data.xlsx')
MD = pandas.read_excel('../Final Data/Meteorological Interpolated.xlsx')\

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

def getAngles(factories,sensors):
	angles = {}
	for factorie in factories:
		for sensor in sensors:
			dx = sensors[sensor][0] - factories[factorie][0]
			dy = sensors[sensor][1] - factories[factorie][1]
			angles['%s_%s'%(factorie,sensor)] = math.degrees(numpy.arctan2(dy,dx))
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

agreements = compareWDvsAngles(SD,MD,angles,10)

for agreement in agreements:
	if agreement[-7:] == 'Sensor2' and agreement[-11:-8] == 'RFE':
		print(agreement)



output = {}
reading = pandas.Series(SD.loc[(SD['Chemical'] == 'Methylosmolene') & (SD['Monitor'] == 2)]['Reading']).values
datetime = pandas.Series(SD.loc[(SD['Chemical'] == 'Methylosmolene') & (SD['Monitor'] == 2)]['Timestamp']).values
output[1] = figure(plot_width=1000, plot_height=250, title='Methylosmolene',y_range=(0,5))
output[1].line(datetime,reading)
#show(column([output[1]]))