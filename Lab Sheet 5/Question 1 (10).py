inputSeq = [1,4,3,2,5,6]

biggestSequence = 0
subSequence = []
sameSize = False
listOfStartingIndex = []
number = 0
i = 0

while i != len(inputSeq)-1:
    print(inputSeq[i], "this is input")
    if inputSeq[i+1] >= inputSeq[i]:
        number = number + 1
        print(number)

    else:
        if number > biggestSequence:
            listOfStartingIndex.append(i-number)
            biggestSequence = number
            number = 0
            print(biggestSequence, "big Seq")
        elif number == biggestSequence:
            sameSize = True
            listOfStartingIndex.append(i-number)
            number = 0
            print("Why are you running")
    i = i +1

#think loop could be working correctly but next bit not

if sameSize == True:
    print("whya u run")
    for n in listOfStartingIndex:
        subSequence.append(inputSeq[inputSeq[listOfStartingIndex[n]]:listOfStartingIndex[n]+number])
else:
    print("are")
    subSequence.append(inputSeq[inputSeq[listOfStartingIndex[0]]:listOfStartingIndex[0]+number])

print(subSequence)
