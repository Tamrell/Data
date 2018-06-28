import pandas as pd
import numpy as np
from datetime import datetime
from pandas import ExcelWriter
from pandas import ExcelFile
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import row
from bokeh.layouts import gridplot
df = pd.read_excel("Complete Data.xlsx",index_col="Timestamp")

# drop invalid months

df=df.dropna(how="all")

# define chemicals
chemicals = list(df.columns.values)[:36]
print(chemicals)

#count missing values
nans=[]

# for i in df:
#   s= df[i]
#   a=s.isnull().sum()


#   nans.append(a)

# print(nans)

# # define hour intervals

hours=[]
for i in range(24):
  if i < 10:
    hour= "0" + str(i)
  else:
    hour = str(i)
  hours.append(hour)

# print(hours)

# # define daily intervals

# days=[]
# for i in range(1,32):
#   if i < 10:
#     day= "-0" + str(i)
#   else:
#     day = "-" + str(i)
#   days.append(day)

# print(days)



# for month in ['2016-08', '2016-12']:     
#   for hour in hours:
#     uurpermaand=[]
#     urenpermaand=[]
#     for day in days:
#       meting = df[month+day+hour]['AG1'] 
#       uurpermaand.append(meting)
#     meanhour= sum(uurpermaand)/len(uurpermaand)
#     urenpermaand.append(meanhour)
#     uurpermaand=[]

# print(urenpermaand)



#augustus = (df[datetime(2016,8,1,0):datetime(2016,8,30,23)][stof])
#december = (df[datetime(2016,12,1,0):datetime(2016,12,31,23)][stof])

#hours_au = augustus.index.hour
#hours_dec = december.index.hour





# urenpermaand=[]
# for i in range(24):
#   uurpermaand=[]
#   for j in range(len(april)):
#     if hours_ap[j] == 0:
#       print(april[j])
#     if hours_ap[j] == i :
#       uurpermaand.append(april[j])
  
#   meanhour=sum(uurpermaand)/len(uurpermaand)
#   urenpermaand.append(meanhour)


# print(urenpermaand)
    
plots = []
for stof in chemicals:
  december = december = (df[datetime(2016,12,1,0):datetime(2016,12,31,23)][stof])

  december=december.fillna(december.mean())
  hours_dec = december.index.hour
  date=december.index.day
  urenpermaand=[]
  for i in range(24):
    uurpermaand = []
    for j in range(len(december)):
      if (date[j] % 4) == 0:
        if hours_dec[j] == i :
          uurpermaand.append(december[j])
    meanhour=sum(uurpermaand)/len(uurpermaand)
    urenpermaand.append(meanhour)
    
  p = figure(title= stof +'/Mondays in December', plot_width=200, plot_height=200)
  p.yaxis.axis_label = stof +' concentration'
  p.xaxis.axis_label = 'Daily hours'

  p.line(x=hours, y=urenpermaand)


  plots.append(p)

show(gridplot([plots[:9],plots[9:18],plots[18:27],plots[27:36]]))
