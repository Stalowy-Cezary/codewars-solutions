def getCount(inputStr):
    num_vowels = 0
    for i in inputStr:
       if i in ('a','e','o','i','u'):
        num_vowels+=1
    
    return num_vowels
