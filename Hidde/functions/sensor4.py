import pandas, math, numpy, time, os
from bokeh.layouts import gridplot, row, column
from bokeh.io import output_file, show
from bokeh.plotting import figure

SData = pandas.read_excel('../../Final Data/Sensor Data.xlsx')

chemicals = ['Methylosmolene','Chlorodinine','AGOC-3A','Appluimonia']


p1 = figure(plot_width=250,plot_height=250,title='%i %s'%(4,'Methylosmolene'))#, y_range = (0,5))
p2 = figure(plot_width=250,plot_height=250,title='%i %s'%(4,'Chlorodinine'))#, y_range = (0,5))
p3 = figure(plot_width=250,plot_height=250,title='%i %s'%(4,'AGOC_3A'))#, y_range = (0,5))
p4 = figure(plot_width=250,plot_height=250,title='%i %s'%(4,'Appluimonia'))#, y_range = (0,5))

readings1 = pandas.Series(SData.loc[(SData['Monitor'] == 4) & (SData['Chemical'] == 'Methylosmolene')]['Reading']).values
readings2 = pandas.Series(SData.loc[(SData['Monitor'] == 4) & (SData['Chemical'] == 'Chlorodinine')]['Reading']).values
readings3 = pandas.Series(SData.loc[(SData['Monitor'] == 4) & (SData['Chemical'] == 'AGOC-3A')]['Reading']).values
readings4 = pandas.Series(SData.loc[(SData['Monitor'] == 4) & (SData['Chemical'] == 'Appluimonia')]['Reading']).values

p1.line([i for i in range(len(readings1))],readings1)
p2.line([i for i in range(len(readings2))],readings2)
p3.line([i for i in range(len(readings3))],readings3)
p4.line([i for i in range(len(readings4))],readings4)


#show(column([p1,p2,p3,p4]))	

def filter4(SData,chemical):
	low8 = 100
	low12 = 100

	readings = []
	timestamps = []
	readingsOverlapping = []

	for index, row in SData[(SData['Chemical'] == chemical) & (SData['Monitor'] == 4)].iterrows():
		timestamp = row['Timestamp'].to_pydatetime()
		if (timestamp.month == 8) & (row['Reading'] < float(low8)):
			low8 = row['Reading']
		if (timestamp.month == 12) & (row['Reading'] < (low12)):
			low12 = row['Reading']

	print('low8: %f en low12: %f'%(low8,low12))

	for index, row in SData[(SData['Chemical'] == chemical) & (SData['Monitor'] == 4)].iterrows():
		timestamp = row['Timestamp'].to_pydatetime()
		if timestamp.month == 8:
			SData[index,'Reading'] = row['Reading']-low8
		if timestamp.month == 12:
			SData[index,'Reading'] = row['Reading']-low12
	return SData

readings = SData[(SData['Chemical'] == 'Methylosmolene') & (SData['Monitor'] == 4)]['Reading'].values
timestamps = SData[(SData['Chemical'] == 'Methylosmolene') & (SData['Monitor'] == 4)]['Timestamp'].values

p10 = figure(plot_width=250, plot_height=250)
p10.line(timestamps,readings)

SData2 = filter4(SData,'Methylosmolene')

readings = SData2[(SData2['Chemical'] == 'Methylosmolene') & (SData2['Monitor'] == 4)]['Reading'].values
timestamps = SData2[(SData2['Chemical'] == 'Methylosmolene') & (SData2['Monitor'] == 4)]['Timestamp'].values

p11 = figure(plot_width=250, plot_height=250)
p11.line(timestamps,readings,color='red')

	
show(row([p10,p11]))
'''
timestamps1, readings11 = filter4(SData,'Methylosmolene')
timestamps2, readings22 = filter4(SData,'Chlorodinine')
timestamps3, readings33 = filter4(SData,'AGOC-3A')
timestamps4, readings44 = filter4(SData,'Appluimonia')

p11 = figure(plot_width=250,plot_height=250,title='%i %s'%(4,'Methylosmolene'))#, y_range = (0,5))
p22 = figure(plot_width=250,plot_height=250,title='%i %s'%(4,'Chlorodinine'))#, y_range = (0,5))
p33 = figure(plot_width=250,plot_height=250,title='%i %s'%(4,'AGOC_3A'))#, y_range = (0,5))
p44 = figure(plot_width=250,plot_height=250,title='%i %s'%(4,'Appluimonia'))#, y_range = (0,5))

p11.line([i for i in range(len(readings11))],readings11)
p22.line([i for i in range(len(readings22))],readings22)
p33.line([i for i in range(len(readings33))],readings33)
p44.line([i for i in range(len(readings44))],readings44)

#show(row([column([p1,p2,p3,p4]),column([p11,p22,p33,p44])]))'''