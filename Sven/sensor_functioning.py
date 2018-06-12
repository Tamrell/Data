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

def plot_serounding_sensor_readings(group):
    if group == 1:
        plot = figure(x_axis_type = 'datetime')
        plot.scatter(x=sensor_reading(9)['Date Time'], y=sensor_reading(9)['Reading'], color="blue")
        plot.scatter(x=sensor_reading(group)['Date Time'], y=sensor_reading(group)['Reading'], color="red")
        plot.scatter(x=sensor_reading(group + 1)['Date Time'], y=sensor_reading(group + 1)['Reading'], color="green")
        output_file('sensor_readings_groep' + str(group))
        show(plot)
        group = int(group)
    elif group == 9:
        plot = figure(x_axis_type = 'datetime')
        plot.scatter(x=sensor_reading(group - 1)['Date Time'], y=sensor_reading(group - 1)['Reading'], color="blue")
        plot.scatter(x=sensor_reading(group)['Date Time'], y=sensor_reading(group)['Reading'], color="red")
        plot.scatter(x=sensor_reading(1)['Date Time'], y=sensor_reading(1)['Reading'], color="green")
        output_file('sensor_readings_groep' + str(group))
        show(plot)
        group = int(group)
    else:
        plot = figure(x_axis_type = 'datetime')
        plot.scatter(x=sensor_reading(group - 1)['Date Time'], y=sensor_reading(group - 1)['Reading'], color="blue")
        plot.scatter(x=sensor_reading(group)['Date Time'], y=sensor_reading(group)['Reading'], color="red")
        plot.scatter(x=sensor_reading(group + 1)['Date Time'], y=sensor_reading(group + 1)['Reading'], color="green")
        output_file('sensor_readings_groep' + str(group))
        show(plot)

def plot_serounding_sensor_readings_chemical(group, chemical):
    if group == 1:
        plot = figure(x_axis_type = 'datetime')
        plot.scatter(x=sensor_reading_chemical(9, chemical)['Date Time'], y=sensor_reading_chemical(9, chemical)['Reading'], color="blue")
        plot.scatter(x=sensor_reading_chemical(group, chemical)['Date Time'], y=sensor_reading_chemical(group, chemical)['Reading'], color="red")
        plot.scatter(x=sensor_reading_chemical(group + 1, chemical)['Date Time'], y=sensor_reading_chemical(group + 1, chemical)['Reading'], color="green")
        output_file('Reading_group' + str(group) + 'for chemical' + str(chemical))
        show(plot)
        group = int(group)
    elif group == 9:
        plot = figure(x_axis_type = 'datetime')
        plot.scatter(x=sensor_reading_chemical(group - 1, chemical)['Date Time'], y=sensor_reading_chemical(group - 1, chemical)['Reading'], color="blue")
        plot.scatter(x=sensor_reading_chemical(group, chemical)['Date Time'], y=sensor_reading_chemical(group, chemical)['Reading'], color="red")
        plot.scatter(x=sensor_reading_chemical(1, chemical)['Date Time'], y=sensor_reading_chemical(1, chemical)['Reading'], color="green")
        output_file('Reading_group' + str(group) + 'for chemical' + str(chemical))
        show(plot)
        group = int(group)
    else:
        plot = figure(x_axis_type = 'datetime')
        plot.scatter(x=sensor_reading_chemical(group - 1, chemical)['Date Time'], y=sensor_reading_chemical(group - 1, chemical)['Reading'], color="blue")
        plot.scatter(x=sensor_reading_chemical(group, chemical)['Date Time'], y=sensor_reading_chemical(group, chemical)['Reading'], color="red")
        plot.scatter(x=sensor_reading_chemical(group + 1, chemical)['Date Time'], y=sensor_reading_chemical(group + 1, chemical)['Reading'], color="green")
        output_file('Reading_group' + str(group) + 'for chemical' + str(chemical))
        show(plot)

#plot_serounding_sensor_readings(1)
#plot_serounding_sensor_readings_chemical(9, 'AGOC-3A')

def plot_sen_red_chem_for_all():
    sensors = list(range(10))
    chemicals = ['Methylosmolene', 'Chlorodinine', 'Appluimonia', 'AGOC-3A']
    for sensor in sensors:
        for chemical in chemicals:
            plot_sensor_reading_chemical(sensor, chemical)

#plot_sen_red_chem_for_all()

#print(sensor_reading_chemical(1, 'Chlorodinine').std())

def outliers_sensor_chemical(sensor, chemical, outlier_def):
    dataframe = sensor_reading_chemical(sensor, chemical)
    outliers = dataframe[dataframe['Reading'] > outlier_def]
    outliers.to_excel('outliers_sensor' + str(sensor) + 'chemical' + chemical + '.xlsx')

def outliers_all_sensors_chemical(chemical, outlier_def):
    for sensor in list(range(10)):
        outliers_sensor_chemical(sensor, chemical, outlier_def)

outliers_all_sensors_chemical('Appluimonia', 2)
