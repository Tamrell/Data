import numpy,math
factories = {
    "RFE": [89,27],
    "KOF": [90,21],
    "RCT": [109,26],
    "ISB": [120,22]
}

sensors = {
    "Sensor1": [62,21],
    "Sensor2": [66,35],
    "Sensor3": [76,41],
    "Sensor4": [88,45],
    "Sensor5": [103,43],
    "Sensor6": [102,22],
    "Sensor7": [89,3],
    "Sensor8": [74,7],
    "Sensor9": [119,42]
}

def buildRanges(factories,sensors,range):
    ranges = {}
    for factorie in factories:
        ranges[factorie] = {}
        factorie_x = factories[factorie][0]
        factorie_y = factories[factorie][1]
        for sensor in sensors:
            sensor_x = sensors[sensor][0]
            sensor_y = sensors[sensor][1]
            dx = abs(factorie_x - sensor_x)
            dy = abs(factorie_y - sensor_y)
            print(dy,dx,math.degrees(math.tanh(dy/dx)))

            '''
            print(factorie,sensor,factorie_x,sensor_x,'dx: ',dx,factorie_y,sensor_y,'dy: ',dy)
            if dx != 0:
                print(factorie,sensor,math.degrees(numpy.arctan(dy/dx)))
            '''

def buildRange(factorie,sensor,range):
    dx = sensor[0] - factorie[0]
    dy = sensor[1] - factorie[1]
    print(factorie,sensor,dx,dy,math.degrees(math.tanh(float(dy)/float(dx))))

buildRange([89,27],[66,35],1)

