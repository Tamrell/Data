import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import Meteorological_Data.xlsx
import Sensor_Data.xlsx

df = pd.read_excel('Meteorological_Data.xlsx', sheet='Sheet1')
