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


inputTest = False                                                           #(1)
while inputTest == False:                                                 #(n)
    try:                                                                    #(n)
        count = int(input("How many numbers are in your sorted list?"))     #(n)
        if count < 1:                                                       #(n)
            raise ValueError                                                #(n)
        inputTest = True                                                    #(n)
    except:                                                                 #(n)
        print("please enter a postive integer")                             #(n)
i = 0                                                                       #(1)
sortedList = []                                                             #(1)
while i <= count-1:                                                         #(n)
    try:                                                                    #(n)
        number = int(input("enter number"))                                 #(n)
        if i == 0:                                                          #(n)
            sortedList.append(number)                                       #(n)
            i = i + 1                                                       #(n)
        elif number < sortedList[len(sortedList)-1]:                        #(n)
            raise ValueError                                                #(n)
        else:                                                               #(n)
            sortedList.append(number)                                       #(n)
            i = i+1                                                         #(n)
            
    except ValueError:                                                      #(n)
        print("Please make sure your list is sorted")                       #(n)
    

inputTest = False                                                           #(1)
while inputTest == False:                                                   #(n)
    try:                                                                    #(n)
            
        lowerNumber = int(input("please enter lower number in interval"))   #(n)
        upperNumber = int(input("please enter upper number in interval"))   #(n)
        if lowerNumber > sortedList[len(sortedList)-1] or upperNumber < sortedList[0]:  #(n)
            print(False)                                                    #(1)
            inputTest = True                                                #(1)
        else:                                                               #(n)
            if lowerNumber <= upperNumber:                                  #(n)
                inputTest = True                                            #(1)
                midpoint = int(0 + (len(sortedList)+0)/2)                                  #(1)
                print(binarySearch(sortedList, lowerNumber, upperNumber, midpoint))        #(1)

    except ValueError:                                                      #(n)
        print("Please make sure you're entering only integers")             #(n)
        





#Runtime of algorithm excluding input validation: 10log(n)+11

#As the length of the list getting searched is shortened by moving to the midpoint,
#and then eliminating the list that is either above it or below it. 
#The while loop thus is not run n times as it is not searched sequentially.
#Thus it is instead log(n) due to it being a divide and conquer algorithm


#Big O excluding input validation: O(log(n))
