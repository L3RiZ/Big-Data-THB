wind = float(input('Geben Sie die Windgeschwindigkeit ein:'))
temp = float(input('Geben Sie die Temperatur ein:'))

def gefühlteTemperatur(temp, wind):
    if wind > 5 and temp < 10:
        felttemp = 13.12 + 0.6215 * temp - 11.37 * wind ** 0.16 + 0.3965 * temp * wind **0.1616
        print(felttemp)
    else:
        print("Temperatur zu hoch und/oder Windgeschwindigkeit zu gering!")
        
gefühlteTemperatur(temp, wind)