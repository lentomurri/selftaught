def milesToKm(miles):
    kilometers = miles * 1.609344
    print(str(miles) + " miles is equal to " + str(kilometers))

def fahrenheitToCelsius(fahrenheit):
    celsius = fahrenheit*9/5+32
    print(str(fahrenheit) + " fahrenheit is equal to " + str(celsius) + " celsius di Duru")

def decimalToBinary(decimal):
    binary = []
    #until decimal is different from 0
    while decimal > 0:
    # keep dividing by 2
        digit = decimal % 2
        binary.append(str(digit))
        decimal = decimal //2
    binary.reverse()
    binary = "".join(binary)
    print(binary)
    #store the remaainder in the list 
    #reverse the list when done 