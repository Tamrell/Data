import pandas as pd
import numpy as np

from bokeh.plotting import figure, show, output_file, save
from bokeh.layouts import row

def seperate_chems(df, speed_mod):

    chemicals = ['Ap', 'Ch', 'Me', 'AG']
    sensors = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

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

def all_chems(df):
    chemicals = ['Ap', 'Ch', 'Me', 'AG']
    color_map = {'Ap': 'green', 'Ch': 'red', 'Me': 'blue', 'AG':'orange'}
    sensors = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    output_file('EDA/Chemicals Over Wind.html')
    p = figure(title='Chemical abundancy over wind speed')
    p.yaxis.axis_label = 'Reading (ppm)'
    p.xaxis.axis_label = 'Wind Speed'

    for chem in chemicals:
        df['All' + chem] = sum([df[chem + sen] for sen in sensors])

        # Plot seperate months for comparison reasons
        p.scatter(x=df['Wind Speed Spline'], y=df['All' + chem],
                  color=color_map[chem], legend=chem, alpha=0.4)
    p.legend.click_policy="hide"
    save(p)



if __name__ == '__main__':

    df = pd.read_excel("Complete Data.xlsx", index_col='Timestamp')

    chemicals = ['Ap', 'Ch', 'Me', 'AG']
    sensors = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    speed_mod = 0.15

    all_chems(df)
