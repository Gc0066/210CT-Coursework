#as still have to use start and end variables, using recursion only saves the need for
#two variables.

def binarySearch(sortedList, lowerNumber, upperNumber, midpoint):           #(1)
    '''takes a sorted list of integers. Two integers that specify the
    interval we are searching for. And an integer calculated by the starting
    index of the list + (the size of the list – the starting index of the list)/2.
    The function will return a Boolean value.'''
    print("in function")
    #initalises variables used for loop.
    valueFound = False                                                      #(1)
    endOfList = False                                                       #(1)
    start = 0                                                               #(1)
    end = len(sortedList)                                                   #(1)

    #while a number in the interval is not found and the list
    #has not completely been checked
    while valueFound == False and endOfList == False:                    #(log(n)
        print("in while loop")
        #if the midpoint number is inbetween the interval return true
        if sortedList[midpoint] < upperNumber and sortedList[midpoint] > lowerNumber: #(log(n))
                                                                          
            valueFound = True                                                #1)
        #if the midpoint number is one of the interval numbers then return true.
        elif sortedList[midpoint] == upperNumber or sortedList[midpoint]== lowerNumber: #(log(n))
            valueFound = True                                                #(1)
        #if the midpoint number is greater than the upper interval number
        #then interval we're searching for is not in list AFTER the midpoint,
        #so get rid of that part.
        elif sortedList[midpoint] > upperNumber:                            #(log(n))
            #checks if list is only one item
            #if it is then end the loop as we would have already checked whether
            #it is a value in the interval.
            if start == end or start>end or end<start:                                               #(log(n))
                endOfList = True                                           #(1)
            #calculates new end of searchable list and new midpoint.
            end = midpoint-1                                               #(log(n))
            midpoint = int(start + (end-start)/2)                          #(log(n))
            print(midpoint)
            print(start, end)
           
        else:                                                              #(log(n))
            #checks if list is only one item
            #if it is then end the loop as we would have already checked whether
            #it is a value in the interval.
            if start ==end or start>end or end<start:                                                #(log(n))
                endOfList = True                                           #(1)
            #calculates new beginning of searchable list and new midpoint. 
            start = midpoint + 1                                           #(log(n))
            midpoint = int(start + (end-start)/2)                          #(log(n))
            print(midpoint, "hi")
            print(start, end)
    #returns whether a value in the interval was found or not.
    return valueFound                                                      #(1)



#list of sorted numbers.
sortedList = [6,14,22,36,42,47,55,59,69]                                   #(1)
#sortedList = [1,2,5,6,7,8,9,.10,11]
#gets interval numbers.
inputNum = input("Please enter an interval")                               #(1)
hold = inputNum.split(",")                                                 #(1)
#assigns the numbers to a variable so can be used later.
lowerNumber = int(hold[0])                                                 #(1)
upperNumber = int(hold[1])                                                 #(1)
print(lowerNumber, upperNumber)
#works out initial midpoint
midpoint = int(0 + (len(sortedList)+0)/2)                                  #(1)

print(binarySearch(sortedList, lowerNumber, upperNumber, midpoint))        #(1)

