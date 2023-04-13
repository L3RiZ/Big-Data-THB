a = int(input('Gebe die erste Zahl ein:'))
b = int(input('Gebe die zweite Zahl ein:'))

def Teiler(num1, num2):
    if num1 % num2 == 0:
        print("True")
    else:
        print("False")

Teiler(a, b)