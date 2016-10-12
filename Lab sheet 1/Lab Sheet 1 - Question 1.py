from random import randint
#inputs list
inputList = input("Please enter a series of numbers")
#splits up entered characters on the , to form a list
usuableList = inputList.split(",")

#initalises what will be our random number
number = 0
#initalises the new list
newList = []
#initalises random numbers generated list
numberList = []
#initalises boolean value used ot exit while loop
boolValue = False

#
for i in usuableList:
    #sets boolean value to false for every new number
    boolValue = False
    #generates random number
    number = randint(0, len(usuableList)-1)
    while boolValue == False:
        #if the number generated has not been geenrated before
        if number not in numberList:
            #adds part of list in the indice specified by the random generation
            newList.append(usuableList[number])
            #to exit loop
            boolValue = True
            #adds number to the randomly generated list
            numberList.append(number)
        else:
            #trys a new random number
            number = randint(0, len(usuableList)-1)

print(newList)

#attempt with recrusion
