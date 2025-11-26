# Question : find the factorial of given number N

# attempt-1-start : 
def _factorial(N):
    if(N==1):
        return 1
    return N * _factorial(N-1)
print(_factorial(9))
# attempt-1-end : 