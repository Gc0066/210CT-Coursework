
#inputSeq = [1,2,3,4,5,6,7,10,3,20,30,50,60,55,10,11,12,13,14,15,16,17]
inputSeq = [-5, 0,1,100,55,102,103]
#inputSeq = [1,4,5,3,1,2]
#inputSeq = [1,4,3,1,2,3,4]
#inputSeq = [1,4]


biggestSequence = 0
subSequence = []
sameSize = False
listOfStartingIndex = []
number = 0
i = 0
startingIndex = 0
#print(len(inputSeq)-1)
while i <= len(inputSeq)-1:
#    if i == len(inputSeq)-1:
    #always increases the number of consecuitve ascending numbers.
    number = number + 1
    #due to short ciruciting in python, it wont go out of range of list,
    #when the loop is one over the size of the list, as it will check
    #the first part of the if statment and that will return true.
    #thus the second condition will never be run due to it being an or.

    #then if it is in fact not in ascending
    if i == len(inputSeq) - 1 or inputSeq[i+1] < inputSeq[i]:
        #checks if it was the largest subsequence so far
        if number > biggestSequence:
            #incase two subsequences of same size then a bigger one
            sameSize = False
                #print(i)
            #print("number is bigger than current sequence value")

            #if it was it it gets the starting index of that subsequence
            #Does this through taking away the amount of numbers in the
            #sequence from the total we have covered so far.
            #as done immediately after the ascending order has been broken,
            #taking away the number and then adding one will give you
            #the starting index.
            startingIndex = i-number+1
            #adds it to the list that will be used if there is multiple subsequences
            #of the same size so that we still print the first subsequence.
            listOfStartingIndex.append(startingIndex)
            #print(startingIndex)
            biggestSequence = number
            #makes it 0 so that the number of consecutive numbers in ascending order
            #can be counted a fresh without the previous's subsequence streak included.
            number = 0
                #print(biggestSequence, "big Seq")
        elif number == biggestSequence:
            #indicates
            sameSize = True
            listOfStartingIndex.append(i-number+1)
            number = 0
            #print("number is equal to current sequence value")
        else:
                number = 0

##    if i == 0:
##        number = 1
####    elif i == len(inputSeq)-1:# and inputSeq[i-1] <= inputSeq[i]:
####        number = number + 1
##        #havent assigned this to the bigest sequence
##    
##    elif i == len(inputSeq):
##        number = number +1
##        #print(number)
##        if number > biggestSequence:
##                #print(i)
##            #print("number is bigger than current sequence value")
##            startingIndex = i-number
##            #print(startingIndex)
##            biggestSequence = number
##                #number = 0
##                #print(biggestSequence, "big Seq")
##        elif number == biggestSequence:
##            sameSize = True
##            listOfStartingIndex.append(i-number)
##                #number = 0
##            #print("number is equal to current sequence value")
##        else:
##                number = 0
##                #print("number is smaller than current value")
##    else:
##        if inputSeq[i-1] <= inputSeq[i]:
##
##            number = number + 1
##            #print(number)
##
##        else:
##            #number = number + 1
##            if number > biggestSequence:
##                #print(i)
##                #print("number is bigger than current sequence value 2nd")
##                #print(number)
##                startingIndex = i-number
##                #print(startingIndex, "2nd")
##                biggestSequence = number
##                number = 0
##                #print(biggestSequence, "big Seq")
##            elif number == biggestSequence:
##                sameSize = True
##                listOfStartingIndex.append(i-number)
##                number = 0
##                #print("number is equal to current sequence value 2nd")
##            else:
##                number = 0
                #print("number is smaller than current value 2nd")
    #print(number, "this is the number")
    #print(biggestSequence)
    print(i, "this is input", number, "this is number")
    i = i +1
    

print(startingIndex, startingIndex+biggestSequence)
print(listOfStartingIndex)

if sameSize == True:
    for n in listOfStartingIndex:
        print(n)
        subSequence.append(inputSeq[n:n+biggestSequence])
        #print(inputSeq[n:n+biggestSequence])
else:
    
    subSequence.append(inputSeq[startingIndex:startingIndex+biggestSequence])

print(subSequence)
