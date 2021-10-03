def string_reverse(str2):
    rstr2 = ''
    index = len(str2)
    while index > 0:
        rstr2 += str2[ index - 1 ]
        index = index - 1
    return rstr2
str1=input("Enter String:")
print(string_reverse(str2))
