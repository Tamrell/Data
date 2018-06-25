import pandas, math, numpy, time
from bokeh.layouts import gridplot, row, column
from bokeh.io import output_file, show
from bokeh.plotting import figure
from tabulate import tabulate
from scipy import stats

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

def filterReadings(SData,Mdata):
	table = []
	for sensor in range(1,10):
		for chemical in chemicals:
				outliers = []
				readings = pandas.Series(SData.loc[(SData['Chemical'] == chemical) & (SData['Monitor'] == sensor)]['Reading']).values
				mean = numpy.mean(readings)
				sem = abs(stats.sem(readings))
				Xmin = mean - 10*sem
				Xmax = mean + 10*sem
				for reading in readings:
					if ((reading > Xmax) | (reading < Xmin)):
						outliers.append(reading)





				table.append([sensor,chemical,len(readings),mean,sem,Xmin,Xmax,len(outliers)])
	return table
table = filterReadings(SData,MData)

print(tabulate(table,headers=['sensor','chemical','# readings','Mean','SEM','Xmin','Xmax','#outliers']))