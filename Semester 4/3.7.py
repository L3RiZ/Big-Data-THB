import math

a = []
b = []

a += [float(input('Bitte X für Punkt A eingeben: '))]
a += [float(input('Bitte Y für Punkt A eingeben: '))]
b += [float(input('Bitte X für Punkt B eingeben: '))]
b += [float(input('Bitte Y für Punkt B eingeben: '))]

def distanz():
    return math.sqrt((b[0] - a[0])**2+(b[1] - a[1])**2)
    
print(distanz())