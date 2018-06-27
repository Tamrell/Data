import pandas as pd
import numpy as np
from datetime import datetime
import math
import statistics


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
    df_in=df_in.fillna(df_in.mean())
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

df=aj
### Data

Roadrunner, Kasios, Radiance, Indigo = [89,27], [90,21], [109,26], [120,22]

Sen_1, Sen_2, Sen_3, Sen_4, Sen_5 = [62,21], [66,35], [76,41], [88,45], [103,43]
Sen_6, Sen_7, Sen_8, Sen_9 = [102,22], [89,3], [74,7], [119,42]

Sensors=Sen_1+Sen_2+Sen_3+Sen_4+Sen_5+Sen_6+Sen_7+Sen_8+Sen_9

Sen_X=[]
Sen_Y=[]
for i in range(18):
    if i % 2 == 0:
        Sen_X.append(Sensors[i])
    else:
        Sen_Y.append(Sensors[i])

fabrieken= ["Roadrunner","Kasios","Radiance","Indigo"]

fabriek_sen=[]
fab_sen_X=[]
fab_sen_Y=[]
for i in range(4):
    if i == 0:
        source = Roadrunner
    if i == 1:
        source = Kasios
    if i == 2:
        source = Radiance
    if i == 3:
        source = Indigo
    for j in range(9):
        fab_sen = fabrieken[i] + "_" + str(j)
        fabriek_sen.append(fab_sen)
        x = source[0]-Sen_X[j]
        y = source[1]-Sen_Y[j]
        fab_sen_X.append(x)
        fab_sen_Y.append(y)


Pathvectors = pd.DataFrame(fabriek_sen, columns = ['FabSenPath'])
Pathvectors["X"]=fab_sen_X
Pathvectors["Y"]=fab_sen_Y

Pathvectors_Roadrunner = Pathvectors.ix[0:8]
Pathvectors_Kasios = Pathvectors.ix[9:17]
Pathvectors_Radiance = Pathvectors.ix[18:26]
Pathvectors_Indigo = Pathvectors.ix[27:35]

def deg_vec(deg):
    rad=deg*math.pi/180
    x=math.cos(rad)
    y=math.sin(rad)
    return [x,y]

def giveVars(windvector,path):
    p = windvector[0]*path[0]+windvector[1]*path[1]
    ro = windvector[0]*windvector[0]+windvector[1]*windvector[1]
    pro = p / ro
    proj= [windvector[0]*pro,windvector[1]*pro]
    downwind = math.sqrt(proj[0]**2+proj[1]**2)
    a = windvector[0]*path[0]+windvector[1]*path[1]
    b = math.sqrt(windvector[0]**2+windvector[1]**2) + math.sqrt(path[0]**2+path[1]**2)
    azimuth =  a / b
    return [downwind,azimuth]

def payup(meting,downwind,azimuth,std_az):
    exponent= (downwind * azimuth)/(2*std_az)
    return (meting*math.pi*std_az*math.e**(exponent))

    april = (df[datetime(2016,4,1,0):datetime(2016,4,30,23)])

def giveAzi(windvector, path):
    a = (windvector[0]*path[0]+windvector[1]*path[1])
    b = math.sqrt(windvector[0]**2+windvector[1]**2) + math.sqrt(path[0]**2+path[1]**2)
    return  a / b



count =- 1
std_azilist=[]
for stof in chemicals:
    count += 1
    list=[]
    pathrow = Pathvectors_Roadrunner.ix[count%9]
    path = [int(pathrow['X']),int(pathrow['Y'])]
    for index, row in df.iterrows():
        windvector = deg_vec(row["Wind Direction Spline"])
        azi = giveAzi(windvector,path)
        list.append(azi)
    cleanedList = [x for x in list if str(x) != 'nan']
    std_azi = statistics.stdev(cleanedList)
    std_azilist.append(std_azi)


count =- 1
ueberlist_road=[]
ueberlist_kas=[]
ueberlist_radi=[]
ueberlist_indi=[]
for stof in chemicals:
    count += 1
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    pathrow1 = Pathvectors_Roadrunner.ix[count%9]
    path1 = [int(pathrow1['X']),int(pathrow1['Y'])]
    [id2, id3, id4] = [(9+(count%9)), (18+(count%9)),(27+(count%9))]
    pathrow2 = Pathvectors_Kasios.ix[id2]
    path2 = [int(pathrow2['X']),int(pathrow2['Y'])]
    pathrow3 = Pathvectors_Radiance.ix[id3]
    path3 = [int(pathrow3['X']),int(pathrow3['Y'])]
    pathrow4 = Pathvectors_Indigo.ix[id4]
    path4 = [int(pathrow4['X']),int(pathrow4['Y'])]
    std_az = std_azilist[count]
    for index, row in df.iterrows():
        meting = row[stof]
        windvector = deg_vec(row["Wind Direction Spline"])
        [downwind1,azimuth1] = giveVars(windvector,path1)
        [downwind2,azimuth2] = giveVars(windvector,path2)
        [downwind3,azimuth3] = giveVars(windvector,path3)
        [downwind4,azimuth4] = giveVars(windvector,path4)
        cost1 = payup(meting,downwind1,azimuth1,std_az)
        cost2 = payup(meting,downwind2,azimuth2,std_az)
        cost3 = payup(meting,downwind3,azimuth3,std_az)
        cost4 = payup(meting,downwind4,azimuth4,std_az)
        list1.append(cost1)
        list2.append(cost2)
        list3.append(cost3)
        list4.append(cost4)
    ueberlist_road.append(list1)
    ueberlist_kas.append(list2)
    ueberlist_radi.append(list3)
    ueberlist_indi.append(list4)

verantwoordelijke=[]
waarschijnlijkheden=[]

for i in range(len(ueberlist_road)):
    roady = ueberlist_road[i]
    kasi = ueberlist_kas[i]
    radi = ueberlist_radi[i]
    indi = ueberlist_indi[i]
    cuz=[]
    probs=[]
    for j in range(len(ueberlist_road[i])):
        check = [roady[j],kasi[j],radi[j],indi[j]]
        likeli = 1/roady[j] + 1/kasi[j] + 1/radi[j] + 1/indi[j]
        val, idx = min((val, idx) for (idx, val) in enumerate(check))
        prob = (1/val) / likeli
        guys = ["Road","Kas","Radi","Indi"]
        cuzza = guys[idx]
        cuz.append(cuzza)
        probs.append(prob)
    verantwoordelijke.append(cuz)
    waarschijnlijkheden.append(probs)

Causa = pd.DataFrame()
Probs = pd.DataFrame()

count = -1
for stof in chemicals:
    count += 1
    Causa[stof]= verantwoordelijke[count]
    Probs[stof]= waarschijnlijkheden[count]

Causa.to_csv('Who_Out.csv', index=False, header=False)
Probs.to_csv('Prob_Out.csv', index=False, header=False)
