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

def makepalindrome(word):
    '''
    This function generates palindromes from a given string 
    and returns the lexicographically earliest palindrome,
    or the palindrome that is shortest.
    '''
    list_of_palindromes = []
    word = str(word)
    if word == word[::-1]:
        list_of_palindromes.append(word)
    # On to generating palindromes.
    # Python slicing syntax is word[start:stop:step]
    # We iterate through the last (i+1) letters of the word
    # in reversed order with step = -1, and add them to the
    # front of the word to generate new palindromes
    for i in range(len(word)):
        temp = word[:-i-1:-1]+word
        if temp == temp[::-1]:
            list_of_palindromes.append(temp)

    # Next we sort the list by the string values and return the 
    # first string entry which should give us the lexicographically
    # earliest palindrome, or the palindrome that is shortest.
    # We can use the sort() methods like this as they are 'stable'
    # sorts.
    list_of_palindromes.sort()
    list_of_palindromes.sort(key=len)
    return list_of_palindromes[0]

print(makepalindrome('quora'))
