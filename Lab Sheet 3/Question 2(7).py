def isPrime(inputNumber, possibleFactor):
    '''input of two integers with second integer being less than first.
    Will return a string sentence, or will call function again.'''

    #if there has not been a number which it can be divided by without a remainder
    #by before one.
    if possibleFactor == 1:
        #then it is a prime.
        return "Number is a prime number"
    elif inputNumber%possibleFactor != 0:
        #if current number cannot be divided by possibleFactor without a remainder
        #then call function again with the value of possibleFactor being one less.
        return isPrime(inputNumber, possibleFactor-1)
    else:
        #if the number can be divided without a remainder
        #then it is not a prime number.
        return "Number is not a prime number"

#get number and convert input into an integer.
number = int(input("please enter a number"))

#makes other number first possible factor.
possibleFactor = number-1

#ensures number could possible be a prime number.
if possibleFactor <1:
    print("please run program again with a number larger than one")
else:
    print(isPrime(number, possibleFactor))
