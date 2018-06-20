import pandas as pd
import numpy as np
from time import sleep

from bokeh.plotting import figure, show, output_file, save
from bokeh.layouts import row, gridplot

from datetime import datetime

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
    '''Scatter-plots all chemicals in one bokeh plot.'''
    # Define data set/initialize variables
    chemicals = ['Ap', 'Ch', 'Me', 'AG']
    color_map = {'Ap': 'green', 'Ch': 'red', 'Me': 'blue', 'AG':'orange'}
    sensors = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    output_file('EDA/Chemicals Over Wind.html')
    p = figure(title='Chemical abundancy over wind speed')
    p.yaxis.axis_label = 'Reading (ppm)'
    p.xaxis.axis_label = 'Wind Speed'

    # Make a scatterplot for each chemical
    for chem in chemicals:

        # Sum all readings of the chemical at a given date time
        df['All' + chem] = sum([df[chem + sen] for sen in sensors])
        p.scatter(x=df['Wind Speed Spline'], y=df['All' + chem],
                  color=color_map[chem], legend=chem, alpha=0.4)
    p.legend.click_policy="hide"
    save(p)

def all_chems2(df):
    '''Scatter-plots all chemicals in 4 bokeh plots aligned in a row.'''
    # Define data set/initialize variables
    chemicals = ['Ap', 'Ch', 'Me', 'AG']
    color_map = {'Ap': 'green', 'Ch': 'red', 'Me': 'blue', 'AG':'orange'}
    sensors = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    plots = []

    # Make a plot for each chemical
    for chem in chemicals:

        # Sum all readings of the chemical at a given date time
        df['All' + chem] = sum([df[chem + sen] for sen in sensors])

        output_file('EDA/Chemicals Over Wind (row).html')
        p = figure(title='Chemical abundancy over wind speed', plot_width=400, plot_height=400)
        p.yaxis.axis_label = 'Reading (ppm)'
        p.xaxis.axis_label = 'Wind Speed'
        p.scatter(x=df['Wind Speed Spline'], y=df['All' + chem],
                  color=color_map[chem], legend=chem, alpha=0.8)
        plots.append(p)
    plots.append(all_chems(df))
    save(row(*plots))


def all_chems3(df):
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
                       title=chem + ' abundancy at ' + sen, plot_width=300, plot_height=300)
            for month in ['2016-04', '2016-08', '2016-12']:

                means_y.append(df[month][chem + sen].mean())
                means_x.append(pd.Timestamp(month + '-15'))
                p.yaxis.axis_label = 'Reading'
                p.xaxis.axis_label = 'Date Time'
                p.scatter(x=df[month].index, y=df[month][chem + sen], legend=chem + sen)

            p.line(x=means_x,
                   y=means_y,
                   legend='mean' ,color='black')
            plots.append(p)
        save(gridplot(plots[:3], plots[3:6], plots[6:]))

def cumulative_Chems(df):

    # Line plots for year.
    chemicals = ['Ap', 'Ch', 'Me', 'AG']
    color_map = {'Ap': 'green', 'Ch': 'red', 'Me': 'blue', 'AG':'orange'}
    sensors = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    df = df.cumsum()
    for chem in chemicals:
        plots = []
        output_file('EDA/cumulative sums/Cumulative ' + chem + ' over time.html')
        for sen in sensors:
            p = figure(x_axis_type='datetime',
                       title=chem + ' abundancy at ' + sen, plot_width=300, plot_height=300)
            for month in ['2016-04', '2016-08', '2016-12']:


                p.yaxis.axis_label = 'Reading'
                p.xaxis.axis_label = 'Date Time'
                p.line(x=df[month].index, y=df[month][chem + sen], legend=chem + sen)
            plots.append(p)
        save(gridplot(plots[:3], plots[3:6], plots[6:]))


def cumulative_Chems2(df):
    chemicals = ['Ap', 'Ch', 'Me', 'AG']
    color_map = {'Ap': 'green', 'Ch': 'red', 'Me': 'blue', 'AG':'orange'}
    sensors = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    df = df.cumsum()

    for sen in sensors:
        plots = []
        output_file('EDA/cumulative sums/Per Sensor/Cumulative chems' + sen +
                    '.html')

        for month in ['2016-04', '2016-08', '2016-12']:
            p = figure(x_axis_type='datetime',
                       title='Cumulative abundancy at ' +
                       sen)#, plot_width=300, plot_height=300)
            for chem in chemicals:
                p.yaxis.axis_label = 'Cumulative Reading'
                p.xaxis.axis_label = 'Date Time'
                p.line(x=df[month].index,
                       y=df[month][chem + sen], legend=chem + sen,
                       color=color_map[chem])
                p.legend.click_policy="hide"
            plots.append(p)
        save(row(*plots))


if __name__ == '__main__':

    df = pd.read_excel("Complete Data.xlsx", index_col='Timestamp')

    chemicals = ['Ap', 'Ch', 'Me', 'AG']
    sensors = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    speed_mod = 0.15

    cumulative_Chems2(df)
