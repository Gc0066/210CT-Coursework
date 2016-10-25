#changed if statement to == instead of !=
#as even when it was one of the vowels. It would not equal all of the other vowels
#thus, all of the other or statements would equal True.
#thus by making it ==, only one would be true or none of them. Making it able to detect
#a vowel.

<<<<<<< HEAD
def removeVowels(inputString, count, newString):                        #(n)
=======
def removeVowels(inputString, count, newString):        #(n)
>>>>>>> origin/master
    '''’’Function passed are a string, an integer and another string.
    Returns a string. Function places every character that is not a vowel into a new string
    Until the end of the input string. It is then returned to the user.'''

    #if we have gone through the entire input string, then return the new string
<<<<<<< HEAD
    if count == len(inputString):                                       #(n)
        return newString                                                #(1)
    
    else:                                                               #(n)
=======
    if count == len(inputString):      #(n)
        return newString       #(1)
    
    else:      #(n)
>>>>>>> origin/master
        
        #otherwise, if the current character is a vowel, then move onto the next character
        if inputString[count] == "a" or inputString[count] == "e" or inputString[count] == "i" or inputString[count] == "o" or inputString[count] == "u":      #(n)
            #print(inputString[count]+ "hi")
<<<<<<< HEAD
            return removeVowels(inputString, count+1, newString)        #(m)
        
        else:                                                           #(n-m)
            #if it is not a vowel, add that character to the new string and then move onto
            #the next character
            newString = newString + inputString[count]                  #(n-m)
=======
            return removeVowels(inputString, count+1, newString)     #(m)
        
        else:     #(n-m)
            #if it is not a vowel, add that character to the new string and then move onto
            #the next character
            newString = newString + inputString[count]     #(n-m)
>>>>>>> origin/master
            #print(newString)
            return removeVowels(inputString, count+1, newString)         #(n-m)


#gets input and makes sure input is lowercase so comparison can work
<<<<<<< HEAD
inputString = input("Please enter a word").lower()                      #(1)
#initialises count integer which will work as index
count = 0                                                               #(1)
#initialises new string that will hold the removed vowel version of the string
newString = ""                                                          #(1)
#calls function to print
print(removeVowels(inputString, count, newString))                      #(1)
=======
inputString = input("Please enter a word").lower()  #(1)
#initialises count integer which will work as index
count = 0    #(1)
#initialises new string that will hold the removed vowel version of the string
newString = ""    #(1)
#calls function to print
print(removeVowels(inputString, count, newString))     #(1)
>>>>>>> origin/master

#runtime: 4n + m + 3(n-m)+ 5

#big O: O(n)
