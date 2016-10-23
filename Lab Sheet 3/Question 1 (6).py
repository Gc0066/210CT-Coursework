#decided against recursion as it would use more memory than the loop
#due too having to pass the variables to the function. Rather than just use
#them immediately.

inputSentence= input("Please input a sentence you would like reversed")

#splits the inputted sentence into just the words
splitSentence = inputSentence.split()

#print(splitSentence)
reversedString = ""

#finds the amount of words in the list. Takes away one as the list
#is indexed from 0 so that loop therefore doesn't begin outside of list.
i = len(splitSentence) -1

#from the end of the list to the beginning. Add the item at position i in the
#list to the new string.
while i >=0:
    reversedString = reversedString + " " + splitSentence[i]
    i = i -1
print(reversedString)
