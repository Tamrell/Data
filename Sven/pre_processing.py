import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

m_data = pd.read_excel('Meteorological_Data.xlsx', sheet='Sheet1')
m_datetime = m_data['Date Time ']
m_wind_direction = m_data['Wind Direction']
m_wind_speed = m_data['Wind Speed (m/s)']

s_data = pd.read_excel('Sensor_Data.xlsx', sheet='Sheet1')
s_chemical = s_data['Chemical']
s_monitor = s_data['Monitor']
s_datetime = s_data['Date Time ']
s_reading = s_data['Reading']

all_chemicals = set(s_chemical)
all_monitors = set(s_monitor)
all_dates_times = set(s_datetime)

sorted_by_chemicals =s_data.sort_values(['Chemical'])
sorted_by_datetime = s_data.sort_values(['Date Time '])
sorted_by_monitor = s_data.sort_values(['Monitor'])
sorted_by_chem_dat_mon = s_data.sort_values(['Chemical', 'Date Time ', 'Monitor'])
sorted_by_mon_chem_dat = s_data.sort_values(['Monitor', 'Chemical', 'Date Time '])

for datetime in m_data['Date Time ']:
    m_index = m_data.index[m_data['Date Time '] == datetime]
    direction_datetime = m_wind_direction.loc[m_index]
    speed_datetime = m_wind_speed.loc[m_index]

    s_indexes = s_data.index[s_data['Date Time '] == datetime]
    for s_index in s_indexes:
        s_data['Wind Speed'] = speed_datetime
        s_data['Wind Direction'] = direction_datetime
