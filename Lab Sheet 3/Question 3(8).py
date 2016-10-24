#changed if statement to == instead of !=
#as even when it was one of the vowels. It would not equal all of the other vowels
#thus, all of the other or statements would equal True.
#thus by making it ==, only one would be true or none of them. Making it able to detect
#a vowel.
def removeVowels(inputString, count, newString):
    '''’’Function passed are a string, an integer and another string.
    Returns a string. Function places every character that is not a vowel into a new string
    Until the end of the input string. It is then returned to the user.'''

    #if we have gone through the entire input string, then return the new string
    if count == len(inputString):
        return newString
    else:
        #otherwise, if the current character is a vowel, then move onto the next character
        if inputString[count] == "a" or inputString[count] == "e" or inputString[count] == "i" or inputString[count] == "o" or inputString[count] == "u":
            #print(inputString[count]+ "hi")
            return removeVowels(inputString, count+1, newString)
        else:
            #if it is not a vowel, add that character to the new string and then move onto
            #the next character
            newString = newString + inputString[count]
            #print(newString)
            return removeVowels(inputString, count+1, newString)


#gets input and makes sure input is lowercase so comparison can work
inputString = input("Please enter a word").lower()
#initialises count integer which will work as index
count = 0
#initialises new string that will hold the removed vowel version of the string
newString = ""
#calls function to print
print(removeVowels(inputString, count, newString))
