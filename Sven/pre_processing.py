import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

m_data = pd.read_excel('Meteorological_Data.xlsx', sheet='Sheet1')
datetime = m_data['Date']
wind_direction = m_data['Wind Direction']
wind_speed = m_data['Wind Speed (m/s)']

s_data = pd.read_excel('Sensor_Data.xlsx', sheet='Sheet1')
chemical = s_data['Chemical']
monitor = s_data['Monitor']
datetime = s_data['Date Time ']
reading = s_data['Reading']

all_chemicals = set(chemical)
all_monitors = set(monitor)
all_dates_times = set(datetime)

sorted_by_chemicals =s_data.sort_values(['Chemical'])
sorted_by_datetime = s_data.sort_values(['Date Time '])
sorted_by_monitor = s_data.sort_values(['Monitor'])
sorted_by_chem_dat_mon = s_data.sort_values(['Chemical', 'Date Time ', 'Monitor'])
sorted_by_mon_chem_dat = s_data.sort_values(['Monitor', 'Chemical', 'Date Time '])

#for row in m_data.rows:
#    if 
