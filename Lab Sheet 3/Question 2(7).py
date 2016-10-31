def isPrime(inputNumber, possibleFactor):                       #(n-1)
    '''input of two integers with second integer being less than first.
    Will return a string sentence, or will call function again.'''

    #if there has not been a number which it can be divided by without a remainder
    #by before one.
    if possibleFactor == 1:                                     #(n-1)
        #then it is a prime.
        return "Number is a prime number"                       #(1)
    elif inputNumber%possibleFactor != 0:                       #(n-2)
        #if current number cannot be divided by possibleFactor without a remainder
        #then call function again with the value of possibleFactor being one less.
        return isPrime(inputNumber, possibleFactor-1)           #(n-2)
    else:                                                       #(1)
        #if the number can be divided without a remainder
        #then it is not a prime number.
        return "Number is not a prime number"                   #(1)


number = int(input("please enter a number"))                    #(1)

#assigns the first number that the input number could possibly be divisible by.
possibleFactor = number-1                                       #(1)

#ensures number could possible be a prime number.
if possibleFactor <1:                                           #(1)
    print("please run program again with a number larger than one")      #(1)
else:                                                           #(1)
    print(isPrime(number, possibleFactor))                      #(1)

#run time: (4n-6)+9
#big O: O(n)
