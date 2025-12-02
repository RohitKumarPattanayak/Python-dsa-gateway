# Merge sort (Divide and conquor) is a popular sorting algorithm known for its efficiency and stability. 
# It follows the Divide and Conquer approach. It works by recursively dividing the input array into two halves,
# recursively sorting the two halves and finally merging them back together to obtain the sorted array.


# ASC order
# attempt-1-start : 
def mergeSortedArray(leftArr,rightArr) : 
    left_len = len(leftArr)
    right_len = len(rightArr)

    left_i = right_i = 0
    merged_arr = []

    while left_i < left_len and right_i < right_len :
        if(leftArr[left_i] <= rightArr[right_i]):
            merged_arr.append(leftArr[left_i])
            left_i+=1
        else:
            merged_arr.append(rightArr[right_i])
            right_i+=1

    if left_i < left_len:
        for i in range(left_i,left_len):
            merged_arr.append(leftArr[i])

    if right_i < right_len:
        for i in range(right_i,right_len):
            merged_arr.append(rightArr[i])

    return merged_arr

def mergeSort(arr):
    if len(arr) == 1 :
        return arr
    
    mid = len(arr)//2

    left_division = arr[:mid]
    right_division = arr[mid:]

    left_arr = mergeSort(left_division)
    right_arr = mergeSort(right_division)

    return mergeSortedArray(left_arr,right_arr)

arr = [
    int(item)
    for item in input('Enter comma separated sorted values : ').split(',')
    if item.strip() != ''
]

print(mergeSort(arr))
# attempt-1-end : 
    



# 1) Time Complexity: Each time we split the list into two halves and then merge them. The depth of recursion is about log⁡n. At each level, merging all elements takes O(n).
# Overall time complexity: O(n.log⁡n).

# 2) Space Complexity: We allocate extra space for the sublists and for merging.
# Overall space complexity: O(n) in most implementations.

# https://codeanddebug.in/blog/merge-sort-algorithm-in-python/

    
