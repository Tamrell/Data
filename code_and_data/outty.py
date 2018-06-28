import pandas as pd
import numpy as np
from datetime import datetime
from pandas import ExcelWriter
from pandas import ExcelFile
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import row
from bokeh.layouts import gridplot
import math
import calendar


df = pd.read_excel("Complete Data.xlsx",index_col="Timestamp")


# drop invalid months

df=df.dropna(how="all")


# define chemicals
chemicals = list(df.columns.values)[:36]


def remove_outlier(df_in, col_name):
    q1 = df_in[col_name].quantile(0.25)
    q3 = df_in[col_name].quantile(0.75)
    iqr = q3-q1 #Interquartile range
    fence_low  = q1-1.5*iqr
    fence_high = q3+1.5*iqr
    lijst=df_in[col_name]
    lissabon=[]
    for i in range(len(lijst)):
        if (lijst[i] > fence_low) & (lijst[i] < fence_high):
            lissabon.append(lijst[i])
        else:
            x = np.nan 
            lissabon.append(x)
    df2 = pd.DataFrame(lissabon, columns = ['NewValues'])
    df_in[col_name] = df2['NewValues'].values
    return df_in

a=remove_outlier(df, chemicals[0])
b=remove_outlier(a, chemicals[1])
c=remove_outlier(b, chemicals[2])
d=remove_outlier(c, chemicals[3])
e=remove_outlier(d, chemicals[4])
f=remove_outlier(e, chemicals[5])
g=remove_outlier(f, chemicals[6])
h=remove_outlier(g, chemicals[7])
i=remove_outlier(h, chemicals[8])
j=remove_outlier(i, chemicals[9])
k=remove_outlier(j, chemicals[10])
l=remove_outlier(k, chemicals[11])
m=remove_outlier(l, chemicals[12])
n=remove_outlier(m, chemicals[13])
o=remove_outlier(n, chemicals[14])
p=remove_outlier(o, chemicals[15])
q=remove_outlier(p, chemicals[16])
r=remove_outlier(q, chemicals[17])
s=remove_outlier(r, chemicals[18])
t=remove_outlier(s, chemicals[19])
u=remove_outlier(t, chemicals[20])
v=remove_outlier(u, chemicals[21])
w=remove_outlier(v, chemicals[22])
x=remove_outlier(w, chemicals[23])
y=remove_outlier(x, chemicals[24])
z=remove_outlier(y, chemicals[25])
aa=remove_outlier(z, chemicals[26])
ab=remove_outlier(aa, chemicals[27])
ac=remove_outlier(ab, chemicals[28])
ad=remove_outlier(ac, chemicals[29])
ae=remove_outlier(ad, chemicals[30])
af=remove_outlier(ae, chemicals[31])
ag=remove_outlier(af, chemicals[32])
ah=remove_outlier(ag, chemicals[33])
ai=remove_outlier(ah, chemicals[34])
aj=remove_outlier(ai, chemicals[35])


