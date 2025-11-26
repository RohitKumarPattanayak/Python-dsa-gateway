## question
## 1) print all the divisors of a given number

# TRICK : you dont have to check each and every number for eligible divisor.
# you only have to check for all the numbers for eligible divisor uptil half of the number
# example : no number greater than 5 can be a eligible divisor for 10.
# divisors of 10 are [1 , 2 , 5 , 10] 

# attempt-1-start :
# def getDivisors(number: int):
#     divisors = []
#     divisor = 1
#     while(divisor <= number//2):
#         if(number%divisor==0):
#             divisors.append(divisor)
#         divisor+=1
#     divisors.append(number)            
#     return divisors    
# number = int(input('enter the number : '))
# print(getDivisors(number))
# attempt-1-end : 



# NOTE : 
# 1) here the time complexity is O(n/2) -> O(n) as 1/2 is negligible
# 2) space complexity is not constant as the array(result) is proportional to number of divisors the input number has 
# - hence space complexity is O(k) where k = number of divisors 


# attempt-2-start :
# def getDivisors(number: int):
#     divisors = []
#     for divisor in range(1,(number//2)+1):
#         if(number%divisor==0):
#             divisors.append(divisor)
#     divisors.append(number)            
#     return divisors    
# number = int(input('enter the number : '))
# print(getDivisors(number))
# attempt-2-end : 


# This approach reduces some spaces/variable utilized and no need for manual incrementation for our iterator




# NOW FOR THE MOST OMTIMAL SOLLUTION
# example : number = 36

# 1   * 36
# 2   * 18
# 3   * 12
# 4   * 9 
# 5   * X  (5 is not a factor/divisor for 36)
# 6   * 6

# in the above example you have found all the factors of 36 with only 6 iteration.
# for better understanding one more example below 

# example number = 25 

# 1  * 25
# 2  * X  (is not a factor/divisor)
# 3  * X  (is not a factor/divisor)
# 4  * X  (is not a factor/divisor)
# 5  * 5  

# in the above example you have found all the factors of 25 with only 5 iteration.

# hence you only need sqroot(inputNumber) times iteration to find out all the factors/divisors



# attempt-3-start :
from math import *
def getDivisors(number: int):
    divisors = []
    for divisor in range(1, int(sqrt(number))+1):
        if(number%divisor==0):
            divisors.append(divisor) # append the divisor
            # if the divisor is equal multiple we end up adding same number twice (example : 5 * 5 while fetching divisors of 25)
            if divisor != number//divisor:
                divisors.append(number//divisor) # append the multiple as well
        divisors.sort()
    return divisors    
number = int(input('enter the number : '))
print(getDivisors(number))
# attempt-3-end : 

# NOTE : 
# 1) here the time complexity is O(sqrt(n))
# 2) space complexity is not constant as the array(result) is proportional to number of divisors the input number has 
# - hence space complexity is O(k) where k = number of divisors  