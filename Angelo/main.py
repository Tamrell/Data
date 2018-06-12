import pandas as pd
import numpy as np
from datetime import datetime
import csv

from bokeh.plotting import figure, show, output_file
from bokeh.layouts import row


def interpolate(df):
    '''interpolates the wind direction of given dataframe'''
    ndf = df.copy()
    ndf.interpolate(inplace=True, limit=5)
    df['Wind Direction Linear'] = np.rad2deg(np.arctan2(ndf['Sin'], ndf['Cos']))
    print(df.corr())

if __name__ == '__main__':

    df = pd.read_csv("reduced.csv", delimiter=',')

    # Classify timestamps as datetimes
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df.set_index(df['Timestamp'], inplace=True)

    # Multiply wind speed by 50 for a better scale
    #df['Wind Speed'] = df['Wind Speed'] * 50

    # Interpolate missing values
    interpolate(df)

    # Plot seperate months for comparison reasons
    plots = []
    for month in ['2016-04', '2016-08', '2016-12']:
        p = figure(x_axis_type='datetime', title='Wind Direction over time in ' + month)
        p.yaxis.axis_label = 'angle in degrees'
        p.xaxis.axis_label = 'Date Time'

        p.line(x=df[month]['Timestamp'], y=df[month]['Wind Direction Linear'])
        p.line(x=df[month]['Timestamp'], y=df[month]['Wind Speed'], color='red')

        plots.append(p)
    show(row(plots[0], plots[1], plots[2]))


    #plot in sinus(degrees) for better interpretable data

    # y = [np.sin(np.deg2rad(float(c))) for c in df['Wind Direction']]
    # x = []
    # print(x[4:8], y[4:8])
    # z = np.polyfit(x[:4], y[:4], 3)
    # f = np.poly1d(z)
    # xn = np.linspace(x[:4][0], x[:4][-1], 7) # 7 to get all relevant points
    # yn = f(xn)
    #
    #
    # p = figure(title='Chemical abundancy of Chlorodinine', x_axis_type='datetime')
    # p.line(x[:20], y[:20], color='red')
    # p.line(xn, yn)
    # for c in [1, 2, 3, 4, 5]:
    #     for i in [0, -1]:
    #         nb = (c * 3) + i
    #         ne = nb + 4
    #         nz = np.polyfit(x[nb:ne], y[nb:ne], 3)
    #         f = np.poly1d(nz)
    #         nx = np.linspace(x[nb:ne][0], x[nb:ne][-1], 7)
    #         ny = f(nx)
    #         p.line(nx, ny)
    # input(str(len(x)) + ' ' +  str(len(y)))
    # p = figure(x_axis_type='datetime')
    # p.scatter(x=df['Timestamp'], y=y)
    # show(p)
    #
    # colormap = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
    # colors = [colormap[x] for x in flowers[   'species']]
    #
    # p = figure(title = "Iris Morphology")
