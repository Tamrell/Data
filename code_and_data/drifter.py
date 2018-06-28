import pandas as pd
import numpy as np
from time import sleep

from bokeh.plotting import figure, show, output_file, save
from bokeh.layouts import row, gridplot

from datetime import datetime

names = {'Ap': 'Appluimonia', 'Ch': 'Chlorodinine', 'Me': 'Methylosmolene', 'AG':'AGOC-3A'}

def behaviour(df):
    chemicals = ['Ap', 'Ch', 'Me', 'AG']
    color_map = {'Ap': 'green', 'Ch': 'red', 'Me': 'blue', 'AG':'orange'}
    sensors = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    for chem in chemicals:
        output_file('EDA/' + chem + ' behaviour over time.html')
        plots = []
        for sen in sensors:
            means_y = []
            means_x = []
            p = figure(x_axis_type='datetime',
                       title=chem + ' abundancy at sensor ' + sen, plot_width=300, plot_height=300)
            for month in ['2016-04', '2016-08', '2016-12']:

                means_y.append(df[month][chem + sen].mean())
                means_x.append(pd.Timestamp(month + '-15'))
                p.yaxis.axis_label = 'Reading'
                p.xaxis.axis_label = 'Date Time'
                p.scatter(x=df[month].index, y=df[month][chem + sen])

            p.line(x=means_x,
                   y=means_y,
                   legend='mean' ,color='black')
            plots.append(p)
        save(gridplot(plots[:3], plots[3:6], plots[6:]))



def corrected_behaviour(df):
    chemicals = ['Ap', 'Ch', 'Me', 'AG']
    color_map = {'Ap': 'green', 'Ch': 'red', 'Me': 'blue', 'AG':'orange'}
    sensors = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    for chem in chemicals:
        output_file('EDA/Chem behaviour' + chem + ' corrected behaviour over time.html')
        plots = []
        for sen in sensors:
            means_y = []
            means_x = []
            p = figure(x_axis_type='datetime',
                       title=chem + ' abundancy at sensor ' + sen, plot_width=300, plot_height=300)
            for month in ['2016-04', '2016-08', '2016-12']:

                means_y.append(df[month][chem + sen].mean())
                means_x.append(pd.Timestamp(month + '-15'))

                diff = 0
                if sen == '4':
                    input(df[month][chem + sen].min())
                    df
                    diff = df[month][chem + sen].mean() - means_y[0]


                p.yaxis.axis_label = 'Reading'
                p.xaxis.axis_label = 'Date Time'
                p.scatter(x=df[month].index,
                          y=df[month][chem + sen] - diff)

            p.line(x=means_x,
                   y=means_y,
                   legend='mean' ,color='black')
            plots.append(p)
        save(gridplot(plots[:3], plots[3:6], plots[6:]))

if __name__ == '__main__':

    df = pd.read_excel("Complete Data.xlsx", index_col='Timestamp')

    chemicals = ['Ap', 'Ch', 'Me', 'AG']
    sensors = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    speed_mod = 0.15

    corrected_behaviour(df)
