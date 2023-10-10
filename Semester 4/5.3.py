import math

class RomNumber: 
    #class variable
    roman = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    numbers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

    def print_roman(number):
        final_str = ""

        for j in range(len(RomNumber.roman)-1, -1, -1):
            output = number // RomNumber.numbers[j]
            number %=  RomNumber.numbers[j]
            while output: 
                final_str += RomNumber.roman[j]
                output -= 1
            
        return final_str
    
    def print_number(number):
        final_int = 0
        j = 0

        while j < len(number):
            if j != len(number)-1 and RomNumber.numbers[RomNumber.roman.index(number[j])] < RomNumber.numbers[RomNumber.roman.index(number[j+1])]:          
                final_int += RomNumber.numbers[RomNumber.roman.index(number[j] + number[j+1])]  
                j += 2            
            else:
                final_int += RomNumber.numbers[RomNumber.roman.index(number[j])] 
                j += 1

        return final_int
                
print(RomNumber.print_roman(321))
print(RomNumber.print_number("CCCXXI"))

class XN:
    def __init__(self, x , n):
        self.x = x
        self.n = n
    
    def calc(x, n):
        return x ** n

print(XN.calc(7,2))

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def umfang(radius):
        return 2 * math.pi * radius
    
    def fläche(radius):
        return math.pi * radius ** 2

print(Circle.umfang(14))
print(Circle.fläche(14))


