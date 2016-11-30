inputTest = False                                               #(1)
while inputTest == False:                                       #(n)
    try:                                                        #(n)
        sizeOfInput = int(input("Please enter the size of the list"))       #(n)
        if sizeOfInput < 1:                                     #(n)
            raise ValueError                                    #(n)
        inputTest = True                                        #(n)
    except ValueError:                                          #(n)
        print("please enter a postive integer")                 #(n)
count = 0                                                       #(1)
inputSeq = []                                                   #(1)
while count <= sizeOfInput - 1:                                 #(n)
    try:                                                        #(n)
        x = int(input("enter number"))                          #(n)
        inputSeq.append(x)                                      #(n)
        count = count + 1                                       #(n)
    except ValueError:                                          #(n)
        print("Please input a number")                          #(n)

biggestSequence = 0                                             #(1)
subSequence = []                                                #(1)
sameSize = False                                                #(1)
listOfStartingIndex = []                                        #(1)
number = 0                                                      #(1)
i = 0                                                           #(1)
startingIndex = 0                                               #(1)

while i <= len(inputSeq)-1:                                     #(n)
    
    #always increases the number, for each number in list
    number = number + 1                                         #(n)
    #due to short ciruciting in python, it wont go out of range of list,
    #when the loop is one over the size of the list, the first part of
    #the if will be checked first and that will return true.
    #thus the second condition will never be run due to it being an or.

    #then if it is in fact not in ascending
    if i == len(inputSeq) - 1 or inputSeq[i+1] < inputSeq[i]:   #(n)
        #checks if it was the largest subsequence so far
        if number > biggestSequence:                            #(n)
            #incase two or more subsequences of same size
            #then a bigger one, it makes it so it only prints
            #the bigger one.
            sameSize = False                                    #(n)
            #As a larger seqeunce found, it removes any starting
            #indexes which were added. As otherwise it would print
            #the previous same sized subsequences if there is another
            #one which is the same size as the newest biggest size.
            listOfStartingIndex=[]                              #(n)

            #gets the starting index of that subsequence does this
            #through taking away the amount of numbers in the
            #sequence from the total we have covered so far.
            #as done immediately after the ascending order has been broken,
            #taking away the number and then adding one will give you
            #the starting index.
            startingIndex = i-number+1                          #(n)
            
            #adds it to the list that will be used if there is multiple subsequences
            #of the same size so that we still print the first subsequence.
            listOfStartingIndex.append(startingIndex)           #(n)
            biggestSequence = number                            #(n)
            #makes it 0 so that the number of consecutive numbers in ascending order
            #can be counted a fresh without the previous's subsequence streak included.
            number = 0                                          #(n)
        elif number == biggestSequence:                         #(n)
            #indicates whether their is multiple subsequences
            #that are the same size and are the largest so far.
            sameSize = True                                     #(n)
            listOfStartingIndex.append(i-number+1)              #(n)
            number = 0                                          #(n)
            
        else:                                                   #(n)
                number = 0                                      #(n)
    
    i = i +1                                                    #(n)
    
#if their was more than one sequence that was the largest
if sameSize == True:                                            #(1)
    #adds every subsequence to a new list
    for n in listOfStartingIndex:                               #(n)
        subSequence.append(inputSeq[n:n+biggestSequence])       #(n)

else:                                                           #(1)
    #adds the highest subsequence to a new list
    subSequence.append(inputSeq[startingIndex:startingIndex+biggestSequence])
    #(1)


print(subSequence)                                              #(1)

#Runtime = 34n+13
#Big O: O(n)
