import pandas as pd
import numpy as np
from datetime import datetime
import csv

from bokeh.plotting import figure, show, output_file
from bokeh.layouts import row

def interpolate(x, y):
    '''When given a list with x elements is given, calculates  '''
    pass

def hours(date):
    date = date.split(' ')
    hours = int(date[1][:2])
    y, m, d = date[0].split('-')
    hours += int(d) * 24 + int(m) * 200
    return hours


if __name__ == '__main__':


    df = pd.read_csv("Meteorological Data.csv", delimiter=';')

    df['Timestamp'] = pd.to_datetime(df['Timestamp'], yearfirst=True)

    df.groupby(pd.Grouper(freq='M'))

    input(df)

    df.interpolate(inplace=True)


    p = figure(x_axis_type='datetime', title='Wind Direction over time')
    p.yaxis.axis_label = 'Sinus value of the incoming angle'
    p.xaxis.axis_label = 'Date Time'

    p.line(x=df['2016-04'], y=df['Wind Direction'])
    p.line(x=df['2016-04'], y=df['Wind Speed'], color='red')
    show(p)
    p2 = figure(x_axis_type='datetime', title='Wind Direction over time')
    p2.yaxis.axis_label = 'Sinus value of the incoming angle'
    p2.xaxis.axis_label = 'Date Time'
    p2.line(x=[pd.Timestamp(t) for t in df['Timestamp'] if t[5:7] == '08'], y= df.loc[df['Timestamp'][5:7] == '08']['Wind Direction'])

    p3 = figure(x_axis_type='datetime', title='Wind Direction over time')
    p3.yaxis.axis_label = 'Sinus value of the incoming angle'
    p3.xaxis.axis_label = 'Date Time'
    p3.line(x=[pd.Timestamp(t) for t in df['Timestamp'] if t[5:7] == '12'], y=df.loc[df['Timestamp'][5:7] == '12']['Wind Direction'])




    output_file('Wind Direction over time')
    show(row(p, p2, p3))

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
