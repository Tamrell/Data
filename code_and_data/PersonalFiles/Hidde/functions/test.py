import pandas, numpy
from bokeh.layouts import gridplot, row, column
from bokeh.io import output_file, show
from bokeh.plotting import figure

SData = pandas.read_excel('../../Final Data/Sensor Data.xlsx')
MData = pandas.read_excel('../../Final Data/Meteorological Interpolated.xlsx')

output_file('all.html')
plots = []

for chemical in ['Methylosmolene','Chlorodinine','AGOC-3A','Appluimonia']:
	means = []

	for sensor in range(1,10):
		mean = numpy.mean(SData[(SData['Monitor'] == sensor) & (SData['Chemical'] == chemical)]['Reading'])
		means.append(mean)
	print(chemical, numpy.mean(means))
	