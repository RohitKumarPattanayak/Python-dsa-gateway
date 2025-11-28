# Selection sort (SELECT THE WISE (MIN/MAX)): Start with the first element of the unsorted portion of the array and assume it is the minimum.
#  Then, iterate through the rest of the unsorted portion to find the actual minimum element and vice-versa for desc.

# attempt-1-start : 
# arr = [
#     int(item)
#     for item in input('Enter comma separated values : ').split(',')
#     if item.strip() != ''
# ]
# def selectionSort(arr):
#     arr_len = len(arr)
#     for index in range(arr_len):
#         min_index = index
#         for j_index in range(index,arr_len):
#             if(arr[min_index] > arr[j_index]):
#                 min_index = j_index
#         if index != min_index:
#             arr[index],arr[min_index] = arr[min_index],arr[index]
#     return arr
# print(selectionSort(arr))
# attempt-1-end : 


# attempt-2-start : 
# arr = [
#     int(item)
#     for item in input('Enter comma separated values : ').split(',')
#     if item.strip() != ''
# ]
# def selectionSort(arr):
#     for index,value in enumerate(arr):
#         min_index = index
#         for j_index,value2 in enumerate(arr[index:],start=index):
#             if(arr[min_index] > value2):
#                 min_index = j_index
#         if index != min_index:
#             arr[index]=arr[min_index]
#             arr[min_index] = value
#     return arr
# print(selectionSort(arr))
# attempt-2-end : 

# I have used two new topics enumerate() function and [index:] array/list slicing (please go through the concepts) for optimized code


# LETS TRY DESC ORDER NOW

# attempt-1-start : 
arr = [
    int(item)
    for item in input('Enter comma separated values : ').split(',')
    if item.strip() != ''
]
def selectionSort(arr):
    for index,value in enumerate(arr):
        max_index = index
        for j_index,value2 in enumerate(arr[index:],start=index):
            if(arr[max_index] < value2):
                max_index = j_index
        if index != max_index:
            arr[index]=arr[max_index]
            arr[max_index] = value
    return arr
print(selectionSort(arr))
# attempt-1-end : 

# Time complexity : O(n^m) => O(n^2) because we are using a loop within a loop so n x m operations
# Space complexity : O(1) as the space here remains constant (arr)