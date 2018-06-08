import pandas as pd
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile
from bokeh.plotting import figure, output_file, show

from pre_processing import integrated_data

def sensor_reading(sensor):
    reading_sensor = pd.Series(integrated_data.loc[integrated_data['Monitor'] == sensor]['Reading']).values
    date_time_sensor = pd.Series(integrated_data.loc[integrated_data['Monitor'] == sensor]['Date Time']).values
    reading_date_time = {'Date Time':date_time_sensor,'Reading':reading_sensor}
    data_sensor = pd.DataFrame(reading_date_time)
    return(data_sensor)

def sensor_reading_chemical(sensor, chemical):
    reading_sensor_chem = pd.Series(integrated_data.loc[(integrated_data['Monitor'] == sensor) & (integrated_data['Chemical'] == chemical)]['Reading']).values
    date_time_sensor_chem = pd.Series(integrated_data.loc[(integrated_data['Monitor'] == sensor) & (integrated_data['Chemical'] == chemical)]['Date Time']).values
    reading_date_time = {'Date Time':date_time_sensor_chem,'Reading':reading_sensor_chem}
    data_sensor_chem = pd.DataFrame(reading_date_time)
    return(data_sensor_chem)

def plot_sensor_reading(sensor):
    plot = figure(x_axis_type = 'datetime')
    plot.scatter(x=sensor_reading(sensor)['Date Time'], y=sensor_reading(sensor)['Reading'])
    output_file('Reading sensor' + str(sensor) + 'over Time')
    show(plot)

def plot_sensor_reading_chemical(sensor, chemical):
    plot = figure(x_axis_type = 'datetime')
    plot.scatter(x=sensor_reading_chemical(sensor, chemical)['Date Time'], y=sensor_reading_chemical(sensor, chemical)['Reading'])
    output_file('Reading sensor' + str(sensor) + 'over Time for chemical' + str(chemical))
    show(plot)
