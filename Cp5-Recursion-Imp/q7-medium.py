# 1) Question find the Nth value in the fibonnaci series using recursion.

# attempt-1-start 
n=int(input('Enter the value of N : '))
def nth_fibb(n,i=0,value=[]):
    if(i>n):
        return value[n]        
    if i-1 <=0:
        value.append(i)
    else:        
        value.append(value[i-1]+value[i-2])
    return nth_fibb(n,i+1,value)          
print(nth_fibb(n))
# attempt-1-end 