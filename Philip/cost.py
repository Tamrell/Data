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

for i in range(36):
    remove_outlier(df, chemicals[0])


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
    exponent= (downwind**2 * azimuth**2)/(2*std_az**2)
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
        try:
            cost1 = payup(meting,downwind1,azimuth1,std_az)
        except:
            cost1 = "x"
        try:
            cost2 = payup(meting,downwind2,azimuth2,std_az)
        except:
            cost2 = "x"
        try:
            cost3 = payup(meting,downwind3,azimuth3,std_az)
        except:
            cost3 = "x"
        try:
            cost4 = payup(meting,downwind4,azimuth4,std_az)
        except:
            cost4 = "x"
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
        czech = [roady[j],kasi[j],radi[j],indi[j]]
        check = [x for x in czech if not isinstance(x, str)]

        if roady[j] == "x":
            ro = 0
        else :
            ro = 1/roady[j]
        if kasi[j] == "x":
            k = 0
        else :
            k = 1/kasi[j]
        if radi[j] == "x":
            ra = 0
        else :
            ra = 1/radi[j]
        if indi[j] == "x":
            ii = 0
        else :
            ii = 1/indi[j]
        likeli = ro + k + ra + ii
        if check == [] :
            prob = 0
            cuzza = "dunno"
        else :
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



Road_AG = []
Road_Ap = []
Road_Ch = []
Road_Me = []
Kas_AG = []
Kas_Ap = []
Kas_Ch = []
Kas_Me = []
Radi_AG = []
Radi_Ap = []
Radi_Ch = []
Radi_Me = []
Indi_AG = []
Indi_Ap = []
Indi_Ch = []
Indi_Me = []

count = -1
for stof in chemicals:
    count +=1
    guys = Causa[stof]
    meting = df[stof]
    probabilities = Probs[stof]
    for i in range(len(Causa[stof])):
        if count < 9 :
            if guys[i] == "Road" :
                if probs[i] > 0.5 :
                    prob = math.sqrt(probs[i])
                    weight = meting[i] * math.sqrt(probs[i])
                    Road_AG.append(weight)
                    Road_AG.append(prob)
            if guys[i] == "Kas" :
                if probs[i] > 0.5 :
                    weight = meting[i] * math.sqrt(probs[i])
                    Kas_AG.append(weight)
                    Kas_AG.append(math.sqrt(probs[i]))
            if guys[i] == "Radi" :
                if probs[i] > 0.5 :
                    weight = meting[i] * math.sqrt(probs[i])
                    Radi_AG.append(weight)
                    Radi_AG.append(math.sqrt(probs[i]))
            if guys[i] == "Indi" :
                if probs[i] > 0.5 :
                    weight = meting[i] * math.sqrt(probs[i])
                    Indi_AG.append(weight)
                    Indi_AG.append(math.sqrt(probs[i]))
        if count >= 9 & count < 18:
            if guys[i] == "Road" :
                if probs[i] > 0.5 :
                    weight = meting[i] * math.sqrt(probs[i])
                    Road_Ap.append(weight)
                    Road_Ap.append(math.sqrt(probs[i]))
            if guys[i] == "Kas" :
                if probs[i] > 0.5 :
                    weight = meting[i] * math.sqrt(probs[i])
                    Kas_Ap.append(weight)
                    Kas_Ap.append(math.sqrt(probs[i]))
            if guys[i] == "Radi" :
                if probs[i] > 0.5 :
                    weight = meting[i] * math.sqrt(probs[i])
                    Radi_Ap.append(weight)
                    Radi_Ap.append(math.sqrt(probs[i]))
            if guys[i] == "Indi" :
                if probs[i] > 0.5 :
                    weight = meting[i] * math.sqrt(probs[i])
                    Indi_Ap.append(weight)
                    Indi_Ap.append(math.sqrt(probs[i]))
        if count >= 18 & count < 27:
            if guys[i] == "Road" :
                if probs[i] > 0.5 :
                    weight = meting[i] * math.sqrt(probs[i])
                    Road_Ch.append(weight)
                    Road_Ch.append(math.sqrt(probs[i]))
            if guys[i] == "Kas" :
                if probs[i] > 0.5 :
                    weight = meting[i] * math.sqrt(probs[i])
                    Kas_Ch.append(weight)
                    Kas_Ch.append(math.sqrt(probs[i]))
            if guys[i] == "Radi" :
                if probs[i] > 0.5 :
                    weight = meting[i] * math.sqrt(probs[i])
                    Radi_Ch.append(weight)
                    Radi_Ch.append(math.sqrt(probs[i]))
            if guys[i] == "Indi" :
                if probs[i] > 0.5 :
                    weight = meting[i] * math.sqrt(probs[i])
                    Indi_Ch.append(weight)
                    Indi_Ch.append(math.sqrt(probs[i]))
        if count >= 27:
            if guys[i] == "Road" :
                if probs[i] > 0.5 :
                    weight = meting[i] * math.sqrt(probs[i])
                    Road_Me.append(weight)
                    Road_Me.append(math.sqrt(probs[i]))
            if guys[i] == "Kas" :
                if probs[i] > 0.5 :
                    weight = meting[i] * math.sqrt(probs[i])
                    Kas_Me.append(weight)
                    Kas_Me.append(math.sqrt(probs[i]))
            if guys[i] == "Radi" :
                if probs[i] > 0.5 :
                    weight = meting[i] * math.sqrt(probs[i])
                    Radi_Me.append(weight)
                    Radi_Me.append(math.sqrt(probs[i]))
            if guys[i] == "Indi" :
                if probs[i] > 0.5 :
                    weight = meting[i] * math.sqrt(probs[i])
                    Indi_Me.append(weight)
                    Indi_Me.append(math.sqrt(probs[i]))

emssionweights_Road_Ag = []
probabilities_Road_Ag = []
for i in range(len(Road_AG)):
    if i % 2:
        emissionweights.append(Road_AG[i])
    else :
        probabilities.append(Road_AG[i])

emssionweights_Road_Ap = []
probabilities_Road_Ap = []
for i in range(len(Road_Ap)):
    if i % 2:
        emissionweights.append(Road_Ap[i])
    else :
        probabilities.append(Road_Ap[i])

emssionweights_Road_Ch = []
probabilities_Road_Ch = []
for i in range(len(Road_Ch)):
    if i % 2:
        emissionweights.append(Road_Ch[i])
    else :
        probabilities.append(Road_Ch[i])

emssionweights_Road_Me = []
probabilities_Road_Me = []
for i in range(len(Road_Me)):
    if i % 2:
        emissionweights.append(Road_Me)
    else :
        probabilities.append(Road_Me)


emssionweights_Kas_AG = []
probabilities_Kas_AG = []
for i in range(len(Kas_AG)):
    if i % 2:
        emissionweights.append(Kas_AG[i])
    else :
        probabilities.append(Kas_AG[i])

emssionweights_Kas_Ap = []
probabilities_Kas_Ap = []
for i in range(len(Kas_Ap)):
    if i % 2:
        emissionweights.append(Kas_Ap[i])
    else :
        probabilities.append(Kas_Ap[i])

emssionweights_Kas_Ch = []
probabilities_Kas_Ch = []
for i in range(len(Kas_Ch)):
    if i % 2:
        emissionweights.append(Kas_Ch[i])
    else :
        probabilities.append(Kas_Ch[i])

emssionweights_Kas_Me = []
probabilities_Kas_Me = []
for i in range(len(Kas_Me)):
    if i % 2:
        emissionweights.append(Kas_Me)
    else :
        probabilities.append(Kas_Me)

emssionweights_Radi_AG = []
probabilities_Radi_AG = []
for i in range(len(Radi_AG)):
    if i % 2:
        emissionweights.append(Radi_AG[i])
    else :
        probabilities.append(Radi_AG[i])

emssionweights_Radi_Ap = []
probabilities_Radi_Ap = []
for i in range(len(Radi_Ap)):
    if i % 2:
        emissionweights.append(Radi_Ap[i])
    else :
        probabilities.append(Radi_Ap[i])

emssionweights_Radi_Ch = []
probabilities_Radi_Ch = []
for i in range(len(Radi_Ch)):
    if i % 2:
        emissionweights.append(Radi_Ch[i])
    else :
        probabilities.append(Radi_Ch[i])

emssionweights_Radi_Me = []
probabilities_Radi_Me = []
for i in range(len(Radi_Me)):
    if i % 2:
        emissionweights.append(Radi_Me)
    else :
        probabilities.append(Radi_Me)

emssionweights_Indi_AG = []
probabilities_Indi_AG = []
for i in range(len(Indi_AG)):
    if i % 2:
        emissionweights.append(Indi_AG[i])
    else :
        probabilities.append(Indi_AG[i])

emssionweights_Indi_Ap = []
probabilities_Indi_Ap = []
for i in range(len(Indi_Ap)):
    if i % 2:
        emissionweights.append(Indi_Ap[i])
    else :
        probabilities.append(Indi_Ap[i])

emssionweights_Indi_Ch = []
probabilities_Indi_Ch = []
for i in range(len(Indi_Ch)):
    if i % 2:
        emissionweights.append(Indi_Ch[i])
    else :
        probabilities.append(Indi_Ch[i])

emssionweights_Indi_Me = []
probabilities_Indi_Me = []
for i in range(len(Indi_Me)):
    if i % 2:
        emissionweights.append(Indi_Me)
    else :
        probabilities.append(Indi_Me)

Road_AG = [sum(emssionweights_Road_AG),mean(probabilities_Road_AG)]
Road_Ap = [sum(emssionweights_Road_Ap),mean(probabilities_Road_Ap)]
Road_Ch = [sum(emssionweights_Road_Ch),mean(probabilities_Road_Ch)]
Road_Me = [sum(emssionweights_Road_Me),mean(probabilities_Road_Me)]
Kas_AG = [sum(emssionweights_Kas_AG),mean(probabilities_Kas_AG)]
Kas_Ap = [sum(emssionweights_Kas_Ap),mean(probabilities_Kas_Ap)]
Kas_Ch = [sum(emssionweights_Kas_Ch),mean(probabilities_Kas_Ch)]
Kas_Me = [sum(emssionweights_Kas_Me),mean(probabilities_Kas_Me)]
Radi_AG = [sum(emssionweights_Radi_AG),mean(probabilities_Radi_AG)]
Radi_Ap = [sum(emssionweights_Radi_Ap),mean(probabilities_Radi_Ap)]
Radi_Ch = [sum(emssionweights_Radi_Ch),mean(probabilities_Radi_Ch)]
Radi_Me = [sum(emssionweights_Radi_Me),mean(probabilities_Radi_Me)]
Indi_AG = [sum(emssionweights_Indi_AG),mean(probabilities_Indi_AG)]
Indi_Ap = [sum(emssionweights_Indi_Ap),mean(probabilities_Indi_Ap)]
Indi_Ch = [sum(emssionweights_Indi_Ch),mean(probabilities_Indi_Ch)]
Indi_Me = [sum(emssionweights_Indi_Me),mean(probabilities_Indi_Me)]



results = pd.DataFrame()

results["Road_AG"] = Road_AG
results["Road_Ap"] = Road_Ap
results["Road_Ch"] = Road_Ch
results["Road_Me"] = Road_Me

results["Kas_AG"] = Kas_AG
results["Kas_Ap"] = Kas_Ap
results["Kas_Ch"] = Kas_Ch
results["Kas_Me"] = Kas_Me

results["Radi_AG"] = Radi_AG
results["Radi_Ap"] = Radi_Ap
results["Radi_Ch"] = Radi_Ch
results["Radi_Me"] = Radi_Me

results["Indi_AG"] = Indi_AG
results["Indi_Ap"] = Indi_Ap
results["Indi_Ch"] = Indi_Ch
results["Indi_Me"] = Indi_Me


results.to_csv('ResultsUncensored.csv')
