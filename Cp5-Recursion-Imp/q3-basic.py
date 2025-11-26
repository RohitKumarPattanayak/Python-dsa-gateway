# Question print sum from 1 to N using Recusrion
# NOTE: There are two types functional (function has a return value) and parameterized (void function or dunction does not return any value)

# attempt-1-start : 
# def _printSum(N,sum=0):
#     if(N==0):
#         print(sum)
#         return
#     sum +=N
#     _printSum(N-1,sum)
# _printSum(10)
# attempt-1-end : 

# In the above i used parameterized i just printed the sum but the function does not return any value.


# attempt-2-start : 
# def _returnSum(N,sum=0):
#     if(N == 0):
#         return sum
#     return _returnSum(N-1,sum+N)
# cummulative=_returnSum(10)
# print(cummulative)
# attempt-2-end : 

# In the above i used functional recursion where i returned the function itself so the value is returned.

# attempt-3-start : (OPTIMIZED FUNCTIONAL RECURSION FOR THE SAME PROBLEM) 
def _returnSum(num):
    if(num==1):
        return 1
    return num + _returnSum(num-1)
print(_returnSum(10))
# attempt-3-end : 