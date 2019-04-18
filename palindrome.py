def makepalindrome(word):
    '''
    This function generates the nearest (least character additions required) 
    palindrome from a given string. If the string is already a palindrome, 
    then the original string is returned.
    '''
    word = str(word)
    if word == word[::-1]:
        return print('(no change) '+word)
    else:
        for i in range(len(word)):
            # Python slicing syntax is word[start:stop:step]
            # We iterate through the last (i+1) letters of the word
            # in reversed order with step = -1
            temp = word[:-i-1:-1]+word
            print(temp)
            # We check if temp is equal to itself reversed
            if temp == temp[::-1]:
                # If true, we return temp as it is a palindrome 
                return print('(result) '+temp)

        return print('(error) palindrome not found')

makepalindrome('race')
