#intepreted question so that it took five days to hatch alien rather than on fifth day alien hatches.
#Decided to use a list to save memory.
#initalised lists for eggs laid and amount of Aliens.
numberOfEggs = []
numberOfAliens = []

#gets input of starting amount of aliens and makes that first day value of aliens.
numberOfAliens.append(int(input("Please enter amont of aliens that have landed")))
#gets number of eggs laid per alien per day.
numberOfEggsLaid = int(input("Please enter the amount laid by an alien each day"))
#gets number of days for each egg to hatch.
numberOfDaysPerHatch = int(input("Please enter amount of days for an egg to hatch"))

#adds the number of eggs laid as input and assigns that to the first day as that will be
#the amount that will be laid on the first day.
numberOfEggs.append(numberOfEggsLaid)
#gets number of days the invasion is happening for and assigns it to variable for later use.
days = int(input("Number Of days the aliens are invading"))
#initalises number of aliens that have hatched.
numberHatched = 0

#loops through from first day to last day inputted
for i in range(1,days):
    ##ignores first value as has already been done before loop, could start from 1 in the loop instead of 0
    ##to get rid of statement.
   # if i != 0:
        #if it has been five days, hatch the aliens and add them to number of aliens.
    if i-numberOfDaysPerHatch >=0:
        numberHatched = numberOfEggs[i-numberOfDaysPerHatch]
            
        numberOfAliens.append(numberOfAliens[i-1] + numberHatched)

    else:
        #if it hasnt been five days then add a new item that is the amount of aliens to signify the
        #amount of aliens that are there everyday.
        numberOfAliens.append(numberOfAliens[i-1])
        #calculates amount of eggs laid that day.
    numberOfEggs.append(numberOfAliens[i] * numberOfEggsLaid)
print(numberOfAliens)
#print the last day of aliens.
print(numberOfAliens[len(numberOfAliens)-1], "Aliens")
