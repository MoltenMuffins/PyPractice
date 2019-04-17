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
    This function generates the nearest palindrome from a given string.
    If the string is already a palindrome, then the original string is returned.
    '''
    word = str(word)
    if ispalindrome(word) == True:
        return print('(no change) '+word)
    else:
        # First we reverse the string
        drow = ''
        for i in reversed(word):
            drow += i
        for i in range(len(drow)):
            temp = drow[:i]+word
            print(temp)
            if ispalindrome(temp) == True:
                return print('(result) '+temp)
        return print('(error) palindrome not found')

makepalindrome('racecar')