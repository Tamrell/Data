import pandas
from bokeh.layouts import gridplot, row, column
from bokeh.io import output_file, show
from bokeh.plotting import figure

SData = pandas.read_excel('../../Final Data/Sensor Data.xlsx')
MData = pandas.read_excel('../../Final Data/Meteorological Interpolated.xlsx')

output_file('all.html')
plots = []

for sensor in range(1,10):
    p1 = figure(plot_width=250,plot_height=250,title='%s_%s'%(sensor,'Methylosmolene'))#, y_range = (0,5))
    p2 = figure(plot_width=250,plot_height=250,title='%s_%s'%(sensor,'Chlorodinine'))#, y_range = (0,5))
    p3 = figure(plot_width=250,plot_height=250,title='%s_%s'%(sensor,'AGOC_3A'))#, y_range = (0,5))
    p4 = figure(plot_width=250,plot_height=250,title='%s_%s'%(sensor,'Appluimonia'))#, y_range = (0,5))

    for chemical in ['Methylosmolene','Chlorodinine','AGOC-3A','Appluimonia']:
        readings = pandas.Series(SData.loc[(SData['Monitor'] == sensor) & (SData['Chemical'] == chemical)]['Reading']).values
        timestamps = pandas.Series(SData.loc[(SData['Monitor'] == sensor) & (SData['Chemical'] == chemical)]['Timestamp']).values
        print(len(readings),len(timestamps))
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