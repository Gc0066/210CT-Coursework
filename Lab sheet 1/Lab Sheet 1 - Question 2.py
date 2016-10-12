def division(fiveCount, number):
    '''This function calculates the amount of trailing 0s in the factorial
    of the number that is inputted.
    The first argument should be an integer and the second should be a float.
    '''
    #checks for base case
    if number > 0 and number < 1:
        return fiveCount
    else:
        #calculates the float number of trailing 0s
        hold = fiveCount + number/5
        #turns it into an integer to round down
        fiveCount = int(hold)
        #calls the function again to keep it going till the base case hits.
        return division(fiveCount, number/5) 


inputNumber = input("Please enter a number")
#turns it into a float so that when it is divided it can then be rounded down.
floatHolder = float(inputNumber)
#initalises the number of trailing 0s.
count = 0


print(division(count, floatHolder))
    
