# Question : Print 1 to N using recursion

# attempt-1-start : 
# def _printTill(num):
#     if(num==0):
#         return
#     _printTill(num-1)
#     print(num)
# _printTill(8)
# attempt-1-end

# In the above i used TAIL recursion as i had to print the number from 1 to N and not vice versa
# TRY BOTH OUT TO GET A HANG OF IT
# If i had to do it in a timer fashion i.e from N to 1 i will use HEAD recursion

# attempt-2-start : 
# def _printTill(num):
#     if(num==0):
#         return
#     print(num)
#     _printTill(num-1)
# _printTill(8)
# attempt-2-end : 



#  With two parameters using HEAD recursion

# attempt-3-start : 
def _printTill(i,num):
    if(i>num):
        return
    print(i)
    _printTill(i+1,num)
_printTill(1,8)
# attempt-3-end : 