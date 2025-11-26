## question
## 1) print each number in for given number n

# attempt-1-start : 
# number = int(input("enter a number : "))

# number_cpy = number
# while(number_cpy):
#     print(number_cpy%10)
#     number_cpy = int(number_cpy/10)
# attempt-1-end :


# NOTE
## the above code could be made better with the replacement of 'number_cpy = int(number_cpy/10)'
# 1) Create a float (slower, more memory)
# 2) Convert that float back to int.

# number_cpy = int(number_cpy/10) with number_cpy = number_cpy//10  
# '//' this is called floor division
# 1) floating-point creation (no float object),
# 2) type conversion (int(...)),
# 3) and is more efficient for integer operations.


# attempt-2-Start : 
number = int(input("enter a number : "))

number_cpy = number
while(number_cpy):
    print(number_cpy%10)
    number_cpy = number_cpy//10
# attempt-2-End :

# NOTE : 
# 1) make sure never to change/manipulate the initial input payload create a copy and proceed manipulating the copy.