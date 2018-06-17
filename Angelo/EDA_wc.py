import pandas as pd
import numpy as np

from bokeh.plotting import figure, show, output_file, save
from bokeh.layouts import row

df = pd.read_excel("Complete Data.xlsx", index_col='Timestamp')

chemicals = ['Ap', 'Ch', 'Me', 'AG']
sensors = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

speed_mod = 0.15
# chem = chemicals[3]
# sen = sensors[0]

for chem in chemicals:
    for sen in sensors:
        # Plot seperate months for comparison reasons
        output_file('EDA/Spline/' + chem + sen + '.html')
        plots = []
        for month in ['2016-04', '2016-08', '2016-12']:

            p = figure(x_axis_type='datetime',
                       title='Wind Speed vs ' + chem + ' abundancy at ' + sen + ' in ' + month)
            p.yaxis.axis_label = 'Reading'
            p.xaxis.axis_label = 'Date Time'

            p.line(x=df[month].index, y=df[month][chem + sen], legend=chem + sen)
            p.line(x=df[month].index,
                   y=df[month]['Wind Speed Spline']*speed_mod,
                   legend='Wind Speed (Spline)x'+str(speed_mod),color='red')

            plots.append(p)
            save(row(*plots))
