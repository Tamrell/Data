import pandas as pd
import csv

def tuples():

    df2 = pd.read_excel("data/Meteorological Data.xlsx", index_col=None)
    
    # Temporary solution!!!!
    df2.dropna()

    geo = {}
    for _, row in df2.iterrows():
        time = row['Date']
        dir = row['Wind Direction']
        speed = row['Wind Speed (m/s)']
        geo[time] = [dir, speed]

    df = pd.read_excel("data/Sensor Data.xlsx", index_col=None)
    chemicals = sorted(list({chemical for chemical in df['Chemical']}))
    monitors = {monitor for monitor in df['Monitor']}
    timestamps = {time for time in df['Date Time ']}
    header = ['Timestamp'] + chemicals + ['Wind Direction', 'Wind Speed']
    readings = {time: {chem: {m: None
                              for m in monitors}
                       for chem in chemicals}
                for time in timestamps}

    for _, row in df.iterrows():
        time = row['Date Time ']
        chem = row['Chemical']
        mon = row['Monitor']
        reading = row['Reading']
        readings[time][chem][mon] = reading

    with open('reduced.csv', 'w') as nf:
        writer = csv.writer(nf, delimiter=';')

        # Set header for the new file.
        writer.writerow(header)
        for time in sorted(list(readings)):
            if not time in geo:
                geinfo = []
            else:
                geinfo = geo[time]
            writer.writerow([time] + [tuple(readings[time][chem].values())
                            for chem in readings[time]] + geinfo)

        #    writer.writerow([)

        #for time in df['Date Time ']:

def columns(df):
    # header = [chem + '@' + str(mon) for chem in chemicals for mon in monitors]
    # header.insert(0, 'Date Time')
    pass



if __name__ == '__main__':

    tuples()
    exit(1)
    x = []
    y = []
    with open('reduced.csv', 'r') as cf:
        next(cf)
        for line in cf:
            i = line.split(';')
            input(eval(i[1])[0])
