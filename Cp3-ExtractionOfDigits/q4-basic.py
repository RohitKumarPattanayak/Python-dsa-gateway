## question
## 1) check if a given number is armstrong number

# Note : how to check if 153 is a armstrong number. each digit to the power of length of the number sumed together is the same number then it is called armstring number
# (1)^3 + (5)^3 + (3)^3 = 1+ 124 + 27 = 153 
# hence 153 is a armstrong number

# attempt-1-start :
from math import *
def checkArmstrong(number: int):
    num = number
    num_len= int(log10(number)+1);
    sum = 0
    while(num):
        last_digit = num%10
        sum += last_digit**num_len
        num //=10
    return sum == number

number = int(input('enter the number : '))
if(checkArmstrong(number)):
    print('it is a armstrong')        
else:
    print('it is not a armstrong')
# attempt-1-end : 

# note : 
# 1) Here time complexity will be o(log10(n)) as each iteration we are dividing the number by 10
# 2) Here Space complexity remains constant O(1)
