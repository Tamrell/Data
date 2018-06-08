import os, pandas, numpy
import matplotlib.pyplot as plt

SD = pandas.read_excel('Sensor Data.xlsx')
MD = pandas.read_excel('Meteorological Data.xlsx')

#return a set of the chemicals
def getChemicals(SD):
    return list(set(pandas.Series(SD['Chemical']).values))

#return a set of the sensors
def getSensors(SD):
    return list(set(pandas.Series(SD['Monitor']).values))

#error where Reading = 31
selected = pandas.Series(SD.loc[(SD['Monitor'] == 1) & (SD['Chemical'] == 'Methylosmolene') & (SD['Reading'] < 25)]['Reading']).values
selectedAfter = [i - numpy.mean(selected) for i in selected]

#https://matplotlib.org/examples/pylab_examples/subplots_demo.html -> goeie uitleg subplots

chemicals = getChemicals(SD)
sensors = getSensors(SD)

for chemical in chemicals:
	for i in range(1,len(sensors)+1):
	    data = pandas.Series(SD.loc[(SD['Monitor'] == i) & (SD['Chemical'] == chemical) & (SD['Reading'] < 100)]['Reading']).values
	    plt.subplot(int('91%i'%i))
	    plt.ylabel('%i'%i)
	    plt.plot(range(len(data)),data)
	plt.savefig('%s.jpg'%chemical)
	plt.clf()