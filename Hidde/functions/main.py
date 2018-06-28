
# coding: utf-8

# In[ ]:


import pandas, math, numpy, time, os
from bokeh.layouts import gridplot, row, column
from bokeh.io import output_file, show
from bokeh.plotting import figure
from scipy import stats


# In[ ]:

# load Data

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

chemicals = ['Methylosmolene','Chlorodinine','AGOC-3A','Appluimonia']


# In[6]:

# make figure with plots for every sensor against every chemical
output_file('output/all.html')
plots = []

for sensor in range(1,10):
    p1 = figure(plot_width=250,plot_height=250,title='%s %s'%(sensor,'Methylosmolene'))#, y_range = (0,5))
    p2 = figure(plot_width=250,plot_height=250,title='%s %s'%(sensor,'Chlorodinine'))#, y_range = (0,5))
    p3 = figure(plot_width=250,plot_height=250,title='%s %s'%(sensor,'AGOC_3A'))#, y_range = (0,5))
    p4 = figure(plot_width=250,plot_height=250,title='%s %s'%(sensor,'Appluimonia'))#, y_range = (0,5))

    for chemical in chemicals:
        readings = pandas.Series(SData.loc[(SData['Monitor'] == sensor) & (SData['Chemical'] == chemical)]['Reading']).values
        timestamps = pandas.Series(SData.loc[(SData['Monitor'] == sensor) & (SData['Chemical'] == chemical)]['Timestamp']).values
        timestamps = [i for i in range(len(readings))]
        if chemical == 'Methylosmolene':
            p1.circle(timestamps,readings)
        elif chemical == 'Chlorodinine':
            p2.circle(timestamps,readings)
        elif chemical == 'AGOC-3A':
            p3.circle(timestamps,readings)
        elif chemical == 'Appluimonia':
            p4.circle(timestamps,readings)
    plots.append([p1,p2,p3,p4])


grid = gridplot([[plots[i][0] for i in range(9)],[plots[i][1] for i in range(9)],[plots[i][2] for i in range(9)],[plots[i][3] for i in range(9)]],title='Everything')
show(grid)


# In[7]:


WindLinear = [float(i) for i in MData['Wind Direction Linear'].values]
WindSpline = [float(i) for i in MData['Wind Direction Spline'].values]

# returns dictionary with the angles between every factory with every sensor
def getAngles(factories,sensors):
    angles = {}
    for factorie in factories:
        for sensor in sensors:
            dx = sensors[sensor][0] - factories[factorie][0]
            dy = sensors[sensor][1] - factories[factorie][1]
            angle = math.degrees(numpy.arctan2(dy,dx))
            if angle < 0:
                angle = 360 + angle
            angles['%s_%s'%(factorie,sensor)] = angle
    return angles

angles = getAngles(factories,sensors)

# return dictionary with a range of X degrees around the angle for every angle from getAngles
def makeRanges(angles,X):
    ranges = {}
    for angle in angles:
        if angles[angle] < X:
            Xmin = angles[angle] - X + 360
        else:
            Xmin = angles[angle] - X
        Xmax = angles[angle] + X
        ranges[angle] = [Xmin,Xmax]
    return ranges

ranges = makeRanges(angles,5)

# convert given wind direction to unit circle axis
def convertWindDirection(MData):
    directionsNew = {}
    for index, row in MData.iterrows():
        windDirection = 270 - row['Wind Direction Linear']
        if windDirection < 0:
            windDirection += 180
        directionsNew[row['Timestamp']] = windDirection
    return directionsNew

windDirections = convertWindDirection(MData)


# returns a dictionary with all the moments the wind blows
# from a factorie to within the range of a sensor
def findOverlap(windDirections,ranges):
    overlap = []
    for direction in windDirections:
        d = windDirections[direction]
        for r in ranges:
            Xmin = ranges[r][0]
            Xmax = ranges[r][1]
            if Xmin > Xmax:
                if (d >= Xmin) | (d <= Xmax):
                    overlap.append('%s_%s'%(r,direction))
            else:
                if (d >= Xmin) & (d <= Xmax):
                    overlap.append('%s_%s'%(r,direction))
    return overlap

overlap = findOverlap(windDirections,ranges)

# splits the overlaps from findOverlap() per factory per sensor
def overlapPerFactoriePerSensor(overlap):
    overlapNew = {}
    for factorie in factories:
        overlapNew[factorie] = {}
        for sensor in range(1,10):
            overlapNew[factorie][sensor] = []
            for o in overlap:
                if (o[0:3] == factorie) & (o[10] == str(sensor)):
                    overlapNew[factorie][sensor].append(o[12:])
    return overlapNew

overlap = overlapPerFactoriePerSensor(overlap)


# In[8]:

'''creates seperate graphs for every factory
makes plots per sensor per chemical with the timestamps on the horizontal axes
and the readings on the times off overlap on the vertical axes. A blue line
represents the overall mean value for that chemical for that sensor '''
def plotGraphs(SData,overlap,chemicals):
    for factorie in overlap:
        output_file('output/%s.html'%factorie)
        plots = []

        for sensor in range(1,10):
 
            #print('Ik begin nu aan sensor %i'%sensor)
            

            print('Ik begin nu aan sensor %i'%sensor)

 
            Methylosmolene = []
            MethylosmoleneTS = []
            MethylosmoleneMean = numpy.mean(pandas.Series(SData.loc[(SData['Monitor'] == sensor) & (SData['Chemical'] == 'Methylosmolene')]['Reading']).values)

            Chlorodinine = []
            ChlorodinineTS = []
            ChlorodinineMean = numpy.mean(pandas.Series(SData.loc[(SData['Monitor'] == sensor) & (SData['Chemical'] == 'Chlorodinine')]['Reading']).values)

            AGOC_3A = []
            AGOC_3ATS = []
            AGOC_3AMean = numpy.mean(pandas.Series(SData.loc[(SData['Monitor'] == sensor) & (SData['Chemical'] == 'AGOC-3A')]['Reading']).values)

            Appluimonia = []
            AppluimoniaTS = []
            AppluimoniaMean = numpy.mean(pandas.Series(SData.loc[(SData['Monitor'] == sensor) & (SData['Chemical'] == 'Appluimonia')]['Reading']).values)

            p1 = figure(plot_width=250,plot_height=250,title='%s %s'%(sensor,'Methylosmolene'))#, y_range = (0,5))
            p2 = figure(plot_width=250,plot_height=250,title='%s %s'%(sensor,'Chlorodinine'))#, y_range = (0,5))
            p3 = figure(plot_width=250,plot_height=250,title='%s %s'%(sensor,'AGOC_3A'))#, y_range = (0,5))
            p4 = figure(plot_width=250,plot_height=250,title='%s %s'%(sensor,'Appluimonia'))#, y_range = (0,5))

            timestamps = overlap[factorie][sensor]
 
            #print('%i x overlap tussen %s en sensor %i'%(len(timestamps),factorie,sensor))
            
            

            print('%i x overlap tussen %s en sensor %i'%(len(timestamps),factorie,sensor))


 
            for index, row in SData[(SData['Monitor'] == sensor) & (SData['Timestamp'].isin(timestamps))].iterrows():
                if str(row['Timestamp'] in timestamps):

                    if row['Chemical'] == 'Methylosmolene':
                            Methylosmolene.append(row['Reading'])
                            MethylosmoleneTS.append(row['Timestamp'])

                    if row['Chemical'] == 'Chlorodinine':
                        Chlorodinine.append(row['Reading'])
                        ChlorodinineTS.append(row['Timestamp'])

                    if row['Chemical'] == 'AGOC-3A':
                        AGOC_3A.append(row['Reading'])
                        AGOC_3ATS.append(row['Timestamp'])

                    if row['Chemical'] == 'Appluimonia':
                        Appluimonia.append(row['Reading'])
                        AppluimoniaTS.append(row['Timestamp'])
 
                        
            #print('Me: %i'%len(Methylosmolene))
            #print('Ch: %i'%len(Chlorodinine))
            #print('AG: %i'%len(AGOC_3A))
            #print('Ap: %i'%len(Appluimonia))


            #print('Me: %i'%len(Methylosmolene))
            #print('Ch: %i'%len(Chlorodinine))
            #print('AG: %i'%len(AGOC_3A))
            #print('Ap: %i'%len(Appluimonia))
 

            MethylosmoleneTS = [i for i in range(len(Methylosmolene))]
            p1.circle(MethylosmoleneTS, Methylosmolene, color='orange')
            p1.line(MethylosmoleneTS,[MethylosmoleneMean for i in range(len(MethylosmoleneTS))])

            ChlorodinineTS = [i for i in range(len(Chlorodinine))]
            p2.circle(ChlorodinineTS, Chlorodinine, color='orange')
            p2.line(ChlorodinineTS,[ChlorodinineMean for i in range(len(ChlorodinineTS))])

            AGOC_3ATS = [i for i in range(len(AGOC_3A))]
            p3.circle(AGOC_3ATS, AGOC_3A, color='orange')
            p3.line(AGOC_3ATS,[AGOC_3AMean for i in range(len(AGOC_3ATS))])

            AppluimoniaTS = [i for i in range(len(Appluimonia))]
            p4.circle(AppluimoniaTS, Appluimonia, color='orange')
            p4.line(AppluimoniaTS,[AppluimoniaMean for i in range(len(AppluimoniaTS))])

            plots.append([p1,p2,p3,p4])
 
        
        #print('En dan nu plotten')


        #print('En dan nu plotten')
 
        grid = gridplot([[plots[i][0] for i in range(9)],[plots[i][1] for i in range(9)],[plots[i][2] for i in range(9)],[plots[i][3] for i in range(9)]],title='Everything')
        show(grid)

plotGraphs(SData,overlap,chemicals)



# In[9]:

from tabulate import tabulate

table = []

for factorie in overlap:
    for chemical in chemicals:
        numOverlaps = 0
        numCorrect = 0
        means = []
 
        mean6 = numpy.mean(SData[(SData['Monitor'] == 6) & (SData['Chemical'] == chemical) & (SData['Reading'] < 5)]['Reading'].values)
        for sensor in [1,2,6,7,8]:
 
            timestamps = overlap[factorie][sensor]

            #  calculate mean reading for specific chemical en monitor
            mean = numpy.mean(SData[(SData['Monitor'] == sensor) & (SData['Chemical'] == chemical) & (SData['Reading'] < 5)]['Reading'].values)

            readingsOverlapping = SData[(SData['Monitor'] == sensor) & (SData['Chemical'] == chemical)& (SData['Timestamp'].isin(timestamps))]['Reading'].values
            if len(readingsOverlapping) > 0:
                means.append(numpy.mean(readingsOverlapping))
            for o in readingsOverlapping:
                if o > mean:
                    numCorrect += 1
                numOverlaps += 1

            # calculate confidence interval    
            Sem = stats.sem(SData[(SData['Monitor'] == sensor) & (SData['Chemical'] == chemical)]['Reading'].values)
            conf = [mean-1.99*Sem, mean+1.99*Sem]



                
        table.append([factorie,chemical,numOverlaps,int((numCorrect/numOverlaps)*100),mean,numpy.mean(means),int((numpy.mean(means)/mean)*100),conf,int((mean6/mean)*100)])

 
os.system('clear')            
with open('output/resultsWithout459.txt','w') as file:
    file.write(tabulate(table,headers=['factorie','chemicals','# overlaps','% correct','Mean','% toename','Mean Overlap','% toename','Confidence interval','mean6']))
#print(tabulate(table,ers=['factorie','chemicals','# overlaps','% correct','Mean','Mean Overlap','% toename']))


os.system('clear')
print(tabulate(table,headers=['factorie','chemicals','# overlaps','% correct','Mean','Mean Overlap',' Conf','% toename']))
 
