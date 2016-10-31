
def IntegerCheck(x):
    """This function will take a number input and check whether it is
    an integer or a float. Returning a boolean value of true if it is an
    integer and false if it is not.
    """
    #Makes a rounded down version of x.
    y = int(x)
    #calculates difference between the rounded down
    #version and the non rounded version.
    diff = x-y
    #if their is not a difference then number is integer.
    if diff == 0:
        return True
    #if their is a difference number is float.
    else:
        return False
boolean = False
#until user has input a positive integer, make them input again
while boolean == False:
    try:
        #converts input to integer
        number = int(input("Please enter a number"))
        #checks to see if it is an integer then checks if it is a
        #positive one
        if number <= 0:
            #if it is not then raises exception so it can be caught by except
            raise ValueError
        boolean = True
    except ValueError:
        print("please enter a positive integer")
    
#works out square root of inputted number.
squareNumber = number **0.5

if IntegerCheck(squareNumber):
    print(number)
else:
    #converts it to a integer to round down.
    finalValue = int(squareNumber)
    #squares number.
    finalValue = finalValue **2
    #outputs the highest perfect square to user.
    print(finalValue)

