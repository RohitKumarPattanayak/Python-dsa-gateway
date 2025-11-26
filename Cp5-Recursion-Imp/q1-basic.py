# A function calling itself is called recursion
# It is neccessary to have a condition which will determine the end of recursion or it will lead to STACK OVERFLOW.
# Recusion uses "stack space" to keep all the function call until each is resolved
# There are types of recusion : HEAD RECUSRION , TAIL RECUSRION (Backtracking)
# example : 
# def recur():
#     -------
#     -------
#     if condition:
#         return
#     recur()

# 1) Question print 'your name' 4 times using recursion

# attempt-1-start (HEAD RECUSRION):
# def printfour(name, count = 0):
#     if count==4:
#         return
#     print(name) # job/logic
#     count+=1
#     printfour(name,count)
# printfour('rohit')
# attempt-1-end : 
# IN the above i have used HEAD RECURSION as my job/logic is written before i call the recursive function


# attempt-1-start (TAIL RECUSRION):
# def printfour(name, count = 0):
#     if count==4:
#         return
#     count+=1
#     printfour(name,count)
#     print(name) # job/logic
# printfour('rohit')
# attempt-1-end : 
# IN the above i have used TAIL RECURSION as my job/logic is written after i call the recursive function


# 1) Time complexity of recursive function in the above example is O(n) where n is number of times the recursion happened
# 2) Space complexity of recursive function is O(n) as it fills the stack space number of times recusion happens but once the recusrion is resolve the stack space is empty


# Optional - in the below i take number of times the print should be done nothing being static
def _print(name, times=1):
    if(times == 0):
        return
    print(name)
    _print(name,times-1)

_print("rohit",5)