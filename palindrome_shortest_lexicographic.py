'''
Question:
Given a string, find the palindrome that can be made by inserting the 
fewest number of characters as possible anywhere in the word. 
If there is more than one palindrome of minimum length that can be made, 
return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", 
since we can add three letters to it (which is the smallest amount to make a palindrome). 
There are seven other palindromes that can be made from "race" by adding three letters, 
but "ecarace" comes first alphabetically.
'''

def ispalindrome(word):
    '''
    This function is a helper function for identifying if a string is a palindrome.
    '''
    word = str(word)
    wordlen=len(word)
    count=0
    for (i,j) in zip(word,reversed(word)):
        if i == j:
            count+=1
    if count == wordlen:
        return True
    else:
        return False

def makepalindrome(word):
    '''
    This function generates palindromes from a given string 
    and returns the lexicographically earliest palindrome,
    or the palindrome that is shortest.
    '''
    list_of_palindromes = []
    word = str(word)
    if ispalindrome(word) == True:
        list_of_palindromes.append(word)
    # On to generating palindromes.
    # First we reverse the given string
    drow = ''
    # Next we add on the last i letters to the front of the 
    # word to generate new palindromes
    for i in reversed(word):
        drow += i
    for i in range(len(drow)):
        temp = drow[:i+1]+word
        if ispalindrome(temp) == True:
            list_of_palindromes.append(temp)
    # Next we sort the list by the string values and return the 
    # first string entry which should give us the lexicographically 
    # earliest palindrome, or the palindrome that is shortest.
    list_of_palindromes.sort()
    list_of_palindromes.sort(key=len)
    return list_of_palindromes[0]

print(makepalindrome('google'))