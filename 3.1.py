a = float(input("Geben Sie die erste Zahl ein:"))
b = float(input("Geben Sie die zweite Zahl ein:"))

def between(num1, num2):
    if num1 > 0 and num1 < 1 and num2 > 0 and num2 < 1 :
        print('True')
    else:
        print('False')
        
between(a, b)