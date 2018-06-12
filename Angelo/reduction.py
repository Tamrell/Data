import pandas as pd
import numpy as np
import csv

def tuples():

    df2 = pd.read_excel("data/Meteorological Data.xlsx", index_col=None)


    # Temporary solution!!!!
    df2.dropna(thresh=5, axis=1)
    df2.interpolate()
    geo = {}
    for _, row in df2.iterrows():
        time = row['Date']
        dir = row['Wind Direction']
        speed = row['Wind Speed (m/s)']
        try:
            geo[time] = [np.sin(np.deg2rad(dir)) / np.cos(np.deg2rad(dir)), speed]
        except:
            print(dir)

    df = pd.read_excel("data/Sensor Data.xlsx", index_col=None)
    chemicals = sorted(list({chemical for chemical in df['Chemical']}))
    monitors = {monitor for monitor in df['Monitor']}
    timestamps = {time for time in df['Date Time ']}
    header = ['Timestamp'] + ['Wind Direction', 'Wind Speed']

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
            writer.writerow([time] + #[tuple(readings[time][chem].values())
                            #for chem in readings[time]] +
                            geinfo)

def columns():

        df = pd.read_excel("data/Meteorological Data.xlsx", index_col=None)
        # Temporary solution!!!
        df2.interpolate()


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
                writer.writerow([time] #+ [tuple(readings[time][chem].values())
                                #or chem in readings[time]]
                                + geinfo)
        header = [chem + '@' + str(mon) for chem in chemicals for mon in monitors]
        header.insert(0, 'Date Time')
        pass

if __name__ == '__main__':

    tuples()
    exit(1)
    x = []
    y = []
    df = pd.read_csv('reduced.csv', delimiter=';')
    df.interpolate(inplace=True)
