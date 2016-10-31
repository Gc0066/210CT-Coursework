from random import randint
#decided to reprogram this question to make it more efficient. More efficient as
#has one less list and does no longer have to continually randomly generate a number
#until it has one that it had not generated before.
def shuffle(usuableList, number, newList):
    '''Function will shuffle a list, creating a new version of it and
    removing items from the old as they are randomly placed into the new list.
    Inputs are the list version of the input, an integer that will be a random
    number after first call and ta list that is the return list.'''

    #checks for base case
    if len(usuableList) == 1:
        #if there is only one item left in the list, then put that last
        #item in the new list and then return it so it can be output.
        newList.append(usuableList[0])
        return newList
    else:
        #generates random integer, 
        number = randint(0, len(usuableList)-1)
        #adds it to new list
        newList.append(usuableList[number])
        #removes the item that has been added to new list from the old list.
        # So that it can no longer be pointed to during the random generation.
        usuableList.remove(usuableList[number])
        #calls the function again so the process can repeat till only one item is in the
        #list.
        return shuffle(usuableList, number, newList)




inputList = input("Please enter a series of numbers")
#splits up entered characters on the , to form a list
usuableList = inputList.split(",")

inputBool = False
i = 0
#until the list entered is all integers
while inputBool == False or i <= len(usuableList)-1:
    #makes sure entered list is only integers
    try:
        #goes through items in the list to check they are all integers
        int(usuableList[i])
        i = i + 1
        #sets boolean value to true to exit loop
        inputBool = True
    #if list entered is not full of integers/if item is not an integer, then outputs error
    except ValueError:
        print("Please only input a series of integers")

        inputList = input("Please enter a series of numbers")
        #splits up entered characters on the , to form a list
        usuableList = inputList.split(",")
        i = 0


 
#initalises what will be our random number
number = 0
newList = []
#calls the shuffle, returning a shuffled version of the list.
print(shuffle(usuableList, number, newList))
