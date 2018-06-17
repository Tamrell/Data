import pandas as pd
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile
from bokeh.plotting import *
import matplotlib.dates as mdates

from pre_processing import integrated_data
from sensor_functioning import *

################## PLOT SENSOR 4 #################

def calculate_regression(sensor):
    sensor_4_df = sensor_reading(sensor)
    index = sensor_4_df.index.astype('l')
    index = index - index[0]
    x = index
    y = sensor_4_df['Reading']
    regression = pd.np.polyfit(x, y, 1)
    return regression

def plot_sensor_reading_regression(sensor, regression):
    plot = figure(x_axis_type = 'datetime')
    regression_x = [sensor_reading(sensor)['Date Time'][sensor_reading(sensor).index[0]], sensor_reading(sensor)['Date Time'][sensor_reading(sensor).index[-1]]]
    plot.line(x=regression_x, y=regression, color='red')
    plot.scatter(x=sensor_reading(sensor)['Date Time'], y=sensor_reading(sensor)['Reading'])
    output_file('Reading sensor' + str(sensor) + 'over Time')
    show(plot)

def plot_sensor_reading_chemical_regression(sensor, chemical):
    plot = figure(x_axis_type = 'datetime')
    plot.scatter(x=regression_x, y=sensor_reading_chemical(sensor, chemical)['Reading'])
    output_file('Reading sensor' + str(sensor) + 'over Time for chemical' + str(chemical))
    show(plot)

def plot_final_sensor_regression(sensor):
    regression = calculate_regression(sensor)
    plot_sensor_reading_regression(sensor, regression)

#print(calculate_regression(4))
plot_final_sensor_regression(4)
