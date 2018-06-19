import pandas

SData = pandas.read_excel('../../Final Data/Sensor Data.xlsx')

dates = pandas.DatetimeIndex(SData['Timestamp'].values)
for date in dates:
	print(date.year,date.month,date.day)


#print([i[5:7] for i in SData['Timestamp'].values])


#readingDot = pandas.Series(SD.loc[(SD['Timestamp'] == agreement[0:19]) & (SD['Chemical'] == chemical) & (SD['Monitor'] == sensor)]['Reading']).values
#datetimeDot = pandas.Series(SD.loc[(SD['Timestamp'] == agreement[0:19]) & (SD['Chemical'] == chemical) & (SD['Monitor'] == sensor)]['Timestamp']).values