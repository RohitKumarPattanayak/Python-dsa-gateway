# Insertion sort (insert the wrong one at the right place):  is a simple sorting algorithm that builds a final sorted array (or list) one item at a time. 
# It is considered an in-place sorting algorithm and is efficient for small data sets or data sets that are already substantially sorted.

# ASC ORDER
# attempt-1-start : 
# arr = [
#     int(item)
#     for item in input('Enter comma separated values : ').split(',')
#     if item.strip() != ''
# ]
# def insertionSort(arr):
#     arr_len=len(arr)
#     for i in range(1,arr_len):
#         if arr[i] < arr[i-1]:
#             for j in range(i,0,-1):
#                 if arr[j] < arr[j-1]:
#                     arr[j],arr[j-1]=arr[j-1],arr[j]                            
#     return arr
# print(insertionSort(arr))
# attempt-1-end :


# ASC ORDER and using whle loop
# attempt-2-start : 
# arr = [
#     int(item)
#     for item in input('Enter comma separated values : ').split(',')
#     if item.strip() != ''
# ]
# def insertionSort(arr):
#     arr_len=len(arr)
#     for i in range(1,arr_len):
#         value=arr[i]
#         j = i-1
#         while j >= 0 and arr[j] > value:
#             arr[j+1] = arr[j]
#             j-=1
#         arr[j+1] = value
#     return arr
# print(insertionSort(arr))
# attempt-2-end : 


# DESC ORDER and using whle loop
# attempt-3-start : 
arr = [
    int(item)
    for item in input('Enter comma separated values : ').split(',')
    if item.strip() != ''
]
def insertionSort(arr):
    arr_len=len(arr)
    for i in range(1,arr_len):
        value=arr[i]
        j=i-1
        while j>=0 and arr[j] < value:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = value
    return arr
print(insertionSort(arr))
# attempt-2-end : 

# DO THIS AGAIN TO GET A HANG OF IT
# https://codeanddebug.in/blog/insertion-sort-algorithm-explained-in-python/