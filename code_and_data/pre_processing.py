import pandas as pd
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile
from bokeh.plotting import figure, output_file, show

# Read into Meteorological_Data.xlsx.
m_data = pd.read_excel('Meteorological_Data.xlsx', sheet='Sheet1')
m_datetime = m_data['Date Time']
m_wind_direction = m_data['Wind Direction']
m_wind_speed = m_data['Wind Speed']

# Read into Sensor_Data.xlsx.
s_data = pd.read_excel('Sensor_Data.xlsx', sheet='Sheet1')
s_chemical = s_data['Chemical']
s_monitor = s_data['Monitor']
s_datetime = s_data['Date Time']
s_reading = s_data['Reading']

# All different chemicals, monitors and datetimes.
#all_chemicals = set(s_chemical)
#all_monitors = set(s_monitor)
#all_dates_times = set(s_datetime)

s_data['Wind Speed'] = np.nan
s_data['Wind Direction'] = np.nan
for datetime in m_datetime:
    m_index = m_data.index[m_datetime == datetime]
    direction_datetime = m_wind_direction.loc[m_index]
    speed_datetime = m_wind_speed.loc[m_index]

    s_indexes = s_data.index[s_datetime == datetime]
    for s_index in s_indexes:
        s_data.at[s_index, 'Wind Speed'] = speed_datetime
        s_data.at[s_index, 'Wind Direction'] = direction_datetime

integrated_data = s_data

#sorted_by_chemicals = integrated_data.sort_values(['Chemical'])
#sorted_by_datetime = integrated_data.sort_values(['Date Time'])
#sorted_by_monitor = integrated_data.sort_values(['Monitor'])
#sorted_by_chem_dat_mon = integrated_data.sort_values(['Chemical', 'Date Time', 'Monitor'])
#sorted_by_mon_chem_dat = integrated_data.sort_values(['Monitor', 'Chemical', 'Date Time'])

#plot = figure(x_axis_type = 'datetime')
#plot.scatter(x=integrated_data['Date Time'], y=integrated_data['Wind Speed'])
#output_file('Wind speed over Time')
#show(plot)

#plot = figure(x_axis_type = 'datetime')
#plot.scatter(x=integrated_data['Date Time'], y=integrated_data['Reading'])
#output_file('Reading over Time')
#show(plot)

#integrated_data.to_csv('Integrated_Data.csv')
