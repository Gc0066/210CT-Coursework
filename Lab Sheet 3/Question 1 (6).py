#decided against recursion as it would use more memory than the loop
#due too having to pass the variables to the function. Rather than just use
#them immediately.

inputSentence= input("Please input a sentence you would like reversed")  #(1)

#splits the inputted sentence into just the words
splitSentence = inputSentence.split()        #(1)

#print(splitSentence)
reversedString = ""          #(1)

#finds the amount of words in the list. Takes away one as the list
#is indexed from 0 so that loop therefore doesn't begin outside of list.
i = len(splitSentence) -1          #(1)

#from the end of the list to the beginning. Add the item at position i in the
#list to the new string.
while i >=0:            #(n)
    reversedString = reversedString + splitSentence[i] + " "        #(n)
    i = i -1           #(n)
print(reversedString)       #(1)

#run time: 3n+5
#big O: O(n)
