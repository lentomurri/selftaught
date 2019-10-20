musicians = ["BTS", "Placebo", "Muse"]

musicians_songs = {"BTS": ["Run", "Idol", "Spring Day"], "Placebo" : ["Sleeping with ghosts", "Blind", "Meds"], "Muse": ["Plug in Baby", "Showbiz", "Bliss"]}

places = (["42°50'36.3N", "13°55'46.8E"], ["37°51'11.1N", "12°28'31.8E"])

myself = {"Height": 1.78, "Eyes": "Blue", "Weight": "A lot", "Color": "Purple"}

# SUM EACH NUMBER FUNCTION

nums = [1,2,3,4]

def sumNum(list):
    sumNumbers = 0
    for num in nums:
        sumNumbers += num
    print(sumNumbers)

sumNum(nums)

# variance with sum built-in function

def sumNumFast(list):
    result = sum(list)
    print(result)

sumNumFast(nums)

#----------------------------------

# Largest element of the list

def findLargest(list):
    largest = list[0]
# iterate through elements 
    for num in nums:
# compare first one to next one until we find the bigger one 
        if largest <= num:
            largest = num
    print(largest)

findLargest(nums)

# built in function max
def findLargestFast(list):
    result = max(list)
    print(result)

findLargestFast(nums)

#---------------------------------

# ask for a range of number and a power, and then sum the different powers 

# ask the user for the maximum number for the list, from 1 to maxNum
max_num = input("Enter the maximum number in the range you want to power and sum: ")
#ask which power should be used
power = input("Enter the power: ")

def sumPower(num):
# set final_sum result
    final_sum = 0
    # Create a list from number in range max_num and iterate through it
    for num in range (1, int(num) + 1):
        # multiply every number for the power4
        num_power = num ** int(power)
        # sum every result and store it into the final_sum variable
        final_sum += num_power
    print(final_sum)

sumPower(max_num)

# find the second Largest

# function to find largest 
#iterate through the list
def findTheLargest(list):
    largest = list[0]
    for num in list:
#compare one var to the rest and find the first largest one
        if largest <= num:
            largest = num
    return largest

def secondLargest(list):
# remove the value from the list 
    list.remove(findTheLargest(list))
# run function again and find actual largest
    findTheLargest(list)
    print(findTheLargest(list))

# secondLargest(nums)

# or

def secondLargest2(list):
#iterate through the list
    largest1 = list[0]
    largest2 = largest1
    for num in list:
# assume first var is the largest, 2nd one is the second largest
        if largest1 <= num:
#compare other variables to these first two and substitute them meanwhile 
# largest1 becomes the new num, largest2 become the old largest1 (which means the second largest we are searching for)
            largest2 = largest1
            largest1 = num
    print(largest2)
                

#or

def secondLargestMax(list):
#remove max from list
    list.remove(max(list))
#print second max
    print(max(list))



# find the second smallest in a list

def secondSmallest(list):
    # set variable to store smallest number in 
    smallest = list[0]
    # iterate through list
    for num in list:
        if smallest > num:
            smallest = num
    list.remove(smallest)
    #remove the smallest and find the second smallest
    for num in list:
        if smallest > num:
            smallest = num
    print(smallest)    

# quick way using in built function

def secondSmallestFast(list):
    list.remove(min(list))
    print(min(list))

# function to convert miles to kilometers
miles = int(input("How many miles you want to convert?"))

def milesToKm(miles):
    kilometers = miles * 1.609344
    print(str(miles) + " miles is equal to " + str(kilometers))

# function to convert fahrenheit to celsius

#take input from user
fahrenheit = float(input("Insert Fahrenheit: "))

def fahrenheitToCelsius(fahrenheit):
    celsius = fahrenheit*9/5+32
    print(str(fahrenheit) + " fahrenheit is equal to " + str(celsius) + " celsius di Duru") 

fahrenheitToCelsius(fahrenheit)

milesToKm(miles)
secondLargest2(nums)
secondLargestMax(nums)
secondSmallest(nums)
secondSmallestFast(nums)

decimal = int(input("Enter your number: "))

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

decimalToBinary(decimal)