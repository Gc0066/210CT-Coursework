#as still have to use start and end variables, using recursion only saves the need for
#two variables.

def binarySearch(sortedList, lowerNumber, upperNumber, midpoint):           #(1)
    '''takes a sorted list of integers. Two integers that specify the
    interval we are searching for. And an integer calculated by the starting
    index of the list + (the size of the list – the starting index of the list)/2.
    The function will return a Boolean value.'''
    
    #initalises variables used for loop.
    valueFound = False                                                      #(1)
    endOfList = False                                                       #(1)
    start = 0                                                               #(1)
    end = len(sortedList)                                                   #(1)

    #while a number in the interval is not found and the list
    #has not completely been checked
    while valueFound == False and endOfList == False:                    #(log(n)
        
        #if the midpoint number is in the interval return true
        if sortedList[midpoint] <= upperNumber and sortedList[midpoint] >= lowerNumber: #(log(n))                                                  
            valueFound = True                                                #(1)

        #if the midpoint number is greater than the upper interval number
        #then interval we're searching for is not in list AFTER the midpoint,
        #so get rid of that part.
        elif sortedList[midpoint] > upperNumber:                            #(log(n))
            
            #checks if the start and end have met or gone past eachother.
            #if it has then end the loop as we would have already checked whether
            #it is a value in the interval.
            
            if start == end or start>end or end<start:                     #(log(n))
                endOfList = True                                           #(1)

            #calculates new end of searchable list and new midpoint.
            end = midpoint-1                                               #(log(n))
            midpoint = int(start + (end-start)/2)                          #(log(n))

           
        else:                                                              #(log(n))

            if start ==end or start>end or end<start:                      #(log(n))
                endOfList = True                                           #(1)
                
            #calculates new beginning of searchable list and new midpoint. 
            start = midpoint + 1                                           #(log(n))
            midpoint = int(start + (end-start)/2)                          #(log(n))

    #returns whether a value in the interval was found or not.
    return valueFound                                                      #(1)




sortedList = [6,14,22,36]                                                   #(1)
#assigns the numbers to a variable so can be used later.
lowerNumber = int(input("please enter lower number in interval"))                 #(1)                               #(1)
upperNumber = int(input("please enter upper number in interval"))           #(1)                                 #(1)                                          

midpoint = int(0 + (len(sortedList)+0)/2)                                  #(1)

print(binarySearch(sortedList, lowerNumber, upperNumber, midpoint))        #(1)

#Runtime: 10log(n)+14

#As the length of the list getting searched is shortened by moving to the midpoint,
#and then eliminating the list that is either above it or below it. 
#The while loop thus is not run n times as it is not searched sequentially.
#Thus it is instead log(n) due to it being a divide and conquer algorithm


#Big O: O(log(n))
