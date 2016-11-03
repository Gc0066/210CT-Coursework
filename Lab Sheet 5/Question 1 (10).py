inputSeq = [1,4,3,2,5,6]

biggestSequence = 0
subSequence = []
sameSize = False
listOfStartingIndex = []
number = 0
i = 0

while i != len(inputSeq)-1:
    if inputSeq[i+1] >= inputSeq[i]:
        number = number + 1
    else:
        if number > biggestSequence:
            listOfStartingIndex.append(i-number)
            biggestSequence = number
        elif number == biggestSequence:
            sameSize = True
            listOfStartingIndex.append(i-number)
    i = i +1

if sameSize == True:
    for n in listOfStartingIndex:
        subSequence.append(inputSeq[inputSequence[listOfStartingIndex[n]]:listOfStartingIndex[n]+number])
else:
    subSequence.append(inputSeq[inputSequence[listOfStartingIndex[0]]:listOfStartingIndex[0]+number])

print(subSequence)
