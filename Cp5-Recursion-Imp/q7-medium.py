# 1) Question find the Nth value in the fibonnaci series using recursion.

# attempt-1-start 
# n=int(input('Enter the value of N : '))
# def nth_fibb(n,i=0,value=[]):
#     if(i>n):
#         return value[n]        
#     if i-1 <=0:
#         value.append(i)
#     else:        
#         value.append(value[i-1]+value[i-2])
#     return nth_fibb(n,i+1,value)          
# print(nth_fibb(n))
# attempt-1-end 


# if you observe 
# fibbonacci series : 0 1 1 2 3 5 8 ......
#                     0 1 2 3 4 5 6

# if you observe fib(5) = fib(3) + fib(4) = 2 + 3 = 5
# fib(6) = fib(4) + fib(5) = 3 + 5 = 8


# attempt-2-start 
n=int(input('Enter the value of N : '))
def nth_fibb(n):
    if(n==0 or n==1):
        return n
    return nth_fibb(n-2) + nth_fibb(n-1)              
print(nth_fibb(n))
# attempt-2-end 
