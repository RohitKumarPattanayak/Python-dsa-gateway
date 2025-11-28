# Bubble sort (BLOW NEIGHBORS BUBBLE and send them back (Adjacent)): Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares "adjacent elements", and swaps them if they are in the wrong order. 
# This process is repeated until the list is sorted. Larger elements "bubble up" to the end of the list with each pass. 

# attempt-1-start : 
# arr = [
#     int(item)
#     for item in input('Enter comma separated values : ').split(',')
#     if item.strip() != ''
# ]
# def bubbleSort(arr):
#     arr_len = len(arr)
#     for index in range(arr_len-1):
#         for j_index in range(arr_len-1-index):  # notice the -index here give a thought
#             if(arr[j_index] > arr[j_index+1]):
#                 arr[j_index],arr[j_index+1] = arr[j_index+1],arr[j_index]
#     return arr
# print(bubbleSort(arr))
# attempt-1-end : 


# LETS TRY DESC ORDER NOW

# attempt-1-start : 
arr = [
    int(item)
    for item in input('Enter comma separated values : ').split(',')
    if item.strip() != ''
]
def bubbleSort(arr):
    arr_len = len(arr)
    for index in range(arr_len-1):
        for j_index in range(arr_len-1-index): # notice the -index here give a thought
            if(arr[j_index] < arr[j_index+1]):
                arr[j_index],arr[j_index+1] = arr[j_index+1],arr[j_index]
    return arr
print(bubbleSort(arr))
# attempt-1-end : 

# Time complexity : O(n^m) => O(n^2) because we are using a loop within a loop so n x m operations
# Space complexity : O(1) as the space here remains constant (arr)