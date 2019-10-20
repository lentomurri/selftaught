import math

# function to calculate the cube
def cube(num):
    print(math.pow(num, 3))

# function to calculate the sum of all numbers in the lists 
def sumNumFast(list):
    result = sum(list)
    print(result)

#largest number in the list
def findLargestFast(list):
    result = max(list)
    print(result)

# ask for a range of number and a power, and then sum the different powers 

#second largest in the list

def secondLargest(list):
# remove the value from the list 
    list.remove(findLargestFast(list))
# run function again and find actual largest
    findLargestFast(list)
    print(findLargestFast(list))

# fast version with in-built module

def secondLargestMax(list):
#remove max from list
    list.remove(max(list))
#print second max
    print(max(list))

# quick way using in built function

def secondSmallestFast(list):
    list.remove(min(list))
    print(min(list))    

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

