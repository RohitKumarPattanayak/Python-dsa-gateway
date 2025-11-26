## question
## 1) print the number of digits for a given number n

# attempt-1-start :
# number = input('enter the number : ')
# print(len(number))
# attempt-1-end : 

# NOTE
# 1) i have user 'augmented statements' here feel free to research
# - count+=1 is count = count + 1
# - number_cpy//=10 is number_cpy = number_cpy//10
# Pros:
# 1) Very simple and short.
# 2) Easy to read and write, no loops needed.
# Cons:
# 1) Not a true numeric approach — you’re counting characters, not digits.
# 2) Fails for negative numbers and whitespace.
# 3) In interviews, it’s often seen as avoiding the algorithmic logic.

# attempt-2-start :
# number = int(input('enter the number : '))
# number_cpy = number
# count = 0 
# while (number_cpy):
#     count+=1
#     number_cpy//=10
# print(count)
# attempt-2-end : 

# NOTE 
# Attempt-2 (Mathematical approach using //)
# Pros:
# 1) True numeric logic — uses integer division and loops.
# 2) Works correctly for negatives (with abs()) and for zero.
# 3) Shows good understanding of loops, conditions, and augmented assignments.
# 4) Demonstrates algorithmic thinking, preferred in interviews.
# Cons:
# 1) Slightly longer code.
# 2) Requires careful handling for the zero case.


# attempt-3-start :
from math import *
number = int(input('enter the number : '))
print(int(log10(number)+1))
# attempt-3-end : 

# NOTE 
# Attempt-3 ( trick using log 10 approach )
# explore what log to the base 10 is - The term log 10 means the common logarithm of the number 10, which asks the question: "To what power must 10 be raised to get the number 10?". The answer is 1, because \(10^{1}=10\). 
# trick when get a log to bas 10 of any number adding one to it and rounding it of gives you number of digit the umber had
# example
# n = 5438, log10(5438) = 3.735 , 3.735 + 1 = 4.735 , int(4.735) = 4 hence the number of digits of n
# n = 177715, log10(177715) = 5.248 , 5.248 + 1 = 6.248 , int(6.248) = 6 hence the number of digits of n 

# Pros:
# 1) True numeric logic.
# 2) Very simple and short.
# Cons:
# 1) Not beginner friendly.



