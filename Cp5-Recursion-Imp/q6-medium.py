# 1) Question check if a string is a pallindrome using recursion

# attempt-1-start 
str = input('Enter a string : ')

def checkPallin(str,index=0):
    str_len = len(str)
    if(index >= str_len):
        return True
    if str[index] != str[str_len-index-1]:
        return False
    return checkPallin(str,index+1)
print(checkPallin(str))
# attempt-1-end 
# 1) Time complexity : O(n/2) => O(n)
# 2) Space complexity : O(n/2) => O(n) (STACK SPACE)