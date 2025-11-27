# Question : reverse an array using functional Recursion you would be given left index, right index only the values within those index 
# should be reversed
# example : 

# arr = ['1', '2', '3', '4', '5', '6', '7', '8']
# left = 2
# right = 6

# result : ['1', '2', '7', '6', '5', '4', '3', '8']

# attempt-1-start 
# arr = [
#     item
#     for item in input('Enter comma separated values : ').split(',')
#     if item.strip() != ''
# ]
# left = int(input('Enter the left index : '))
# right = int(input('Enter the right index : '))
# def reverse(arr,left,right):
#     if(left>=right):
#         return arr
#     tmp = arr[left]
#     arr[left] = arr[right]
#     arr[right] = tmp
#     return reverse(arr,left+1,right-1)
# arr = reverse(arr,left,right)
# print (arr)
# attempt-1-end 


# attempt-2-start 
arr = [
    item
    for item in input('Enter comma separated values : ').split(',')
    if item.strip() != ''
]
left = int(input('Enter the left index : '))
right = int(input('Enter the right index : '))
def reverse(arr,left,right):
    if(left>=right):
        return arr
    arr[left],arr[right] = arr[right],arr[left] # MULTIPLE ASSIGNMENT IN PYTHON
    return reverse(arr,left+1,right-1)
arr = reverse(arr,left,right)
print (arr)
# attempt-2-end 

# The second appraoch is better as it radicates the use of an extra variable 'tmp' instead using multiple assignment in python