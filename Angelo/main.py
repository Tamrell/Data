import pandas as pd
import numpy as np
from datetime import datetime

from bokeh.plotting import figure, show, output_file

def interpolate(x, y):
    '''When given a list with x elements is given, calculates  '''
    pass

def hours(date):
    date = date.split(' ')
    hours = int(date[1][:2])
    y, m, d = date[0].split('-')
    hours += int(d) * 24
    return hours

if __name__ == '__main__':

    df = pd.read_csv("reduced.csv", delimiter=';')
    df.fillna('', inplace=True)

    #df.fillna(method='ffill', inplace=True)
    print(df)
    #df.interpolate(method='values')


    # plot in sinus(degrees) for better interpretable data

    # y = [np.sin(np.deg2rad(float(c))) for c in df['Wind Direction'] if not c == '' and not c == 'NaT']
    # # print(x[4:8], y[4:8])
    # z = np.polyfit(x[:4], y[:4], 3)
    # f = np.poly1d(z)
    # xn = np.linspace(x[:4][0], x[:4][-1], 7) # 7 to get all relevant points
    # yn = f(xn)
    #
    #
    # p = figure(title='Chemical abundancy of Chlorodinine', x_axis_type='datetime')
    # p.yaxis.axis_label = 'Chemical abundancy in ppm'
    # p.xaxis.axis_label = 'Timestamp'
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
    p = figure(x_axis_type='datetime')
    p.scatter(x=integrated_data['Timestamp'], y=integrated_data['Wind Direction'])
    show(p)
    #
    # colormap = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
    # colors = [colormap[x] for x in flowers[   'species']]
    #
    # p = figure(title = "Iris Morphology")

    #
    # p.circle(flowers["petal_length"], flowers["petal_width"],
    #          color=colors, fill_alpha=0.2, size=10)
    #
    # show(p)
