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

        for j in range(len(number)):
            if RomNumber.numbers[RomNumber.roman.index(number[j])] < RomNumber.numbers[RomNumber.roman.index(number[j+1])]:          
                final_int += RomNumber.numbers[RomNumber.roman.index(number[j] + number[j+1])]  
                j += 1            
                print(final_int) 
            else:
                final_int += RomNumber.numbers[RomNumber.roman.index(number[j])] 
                print(final_int) 

        return final_int
                

print(RomNumber.print_number("MCMXCIX"))