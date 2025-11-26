## question
## 1) check if a given number is pallindrome

# attempt-1-start :
def checkPallim(number: int):
    num = number
    rev_num=0;
    while(num):
        rev_num *= 10 
        rev_num += num%10
        num //= 10
    return rev_num == number

number = int(input('enter the number : '))
if(checkPallim(number)):
    print('it is a pallindrome')        
else:
    print('it is not a pallindrome')
# attempt-1-end : 

# NOTE : 
# 1) Here time complexity will be o(log10(n)) as each iteration we are dividing the number by 10
# 2) Here Space complexity remains constant O(1)