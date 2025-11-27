# 1) Question : find the factorial of given number N

# attempt-1-start : 
# def _factorial(N):
#     if(N==1):
#         return 1
#     return N * _factorial(N-1)
# print(_factorial(9))
# attempt-1-end : 

# 1) Time complexity - O(n)
# 2) Space complexity - O(n) - STACK SPACE


# 2) Question : reverse an array using recursion

# attempt-1-start : 
# arr = [
#     item
#     for item in input('Enter comma separated values : ').split(',')
#     if item.strip() != ''
# ]
# def reverse(arr,rev=[]):
#     if(arr == []):
#         return rev
#     rev.append(arr.pop())
#     return reverse(arr,rev)
# arr = reverse(arr)
# print (arr)
# attempt-1-end : 

# attempt-2-start : 
arr = [
    item
    for item in input('Enter comma separated values : ').split(',')
    if item.strip() != ''
]
def reverse(arr,index=0):
    arr_len = len(arr)
    if index >= arr_len//2:
        return arr
    tmp = arr[index]
    arr[index] = arr[arr_len-index-1]
    arr[arr_len-index-1] = tmp
    return reverse(arr,index+1)
arr = reverse(arr)
print (arr)
# attempt-2-end :

# approach 2 using a single parameter index not a separate array
# 1) Time complexity : O(n/2) => O(n)
# 2) Space complexity : O(n/2) => O(n) (STACK SPACE)

