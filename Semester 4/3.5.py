a = 123456789
b = 0

while a != 0:
    b = (10*b) + (a % 10)
    a //= 10
    print(a,b)
    
print (a,b)
