# QuickSort is a sorting algorithm based on the (Divide and Conquer with pivot)
# that picks an element as a pivot and partitions the given array 
# around the picked pivot by placing the pivot in its correct position in the sorted array. .

# ASC order
# attempt-1-start : 
# the below is resposible to pick a pivot and keep it in the right place

# ASC order
def qs_partition_asc(arr,low,high):
    i = low
    j = high
    pivot = arr[low]
    while i < j:
        while arr[i] <= pivot and i < high:
            i+=1 
        while arr[j] >= pivot and j > low:
            j-=1
        if(i<j):
            arr[i],arr[j] = arr[j],arr[i]
    arr[low],arr[j] = arr[j],arr[low]    
    return j

# DESC order
def qs_partition_desc(arr,low,high):
    i = low
    j = high
    pivot = arr[low]
    while i < j:
        while arr[i] >= pivot and i < high:
            i+=1 
        while arr[j] <= pivot and j > low:
            j-=1
        if(i<j):
            arr[i],arr[j] = arr[j],arr[i]
    arr[low],arr[j] = arr[j],arr[low]    
    return j

def quickSort(nums,low,high,order = 'asc'):
    if (low < high):
        if (order == 'asc'):
            p_index=qs_partition_asc(nums,low,high)
        else:
            p_index=qs_partition_desc(nums,low,high)
        quickSort(nums,low,p_index-1,order)
        quickSort(nums,p_index+1,high,order) 

arr = [
    int(item)
    for item in input('Enter comma separated sorted values : ').split(',')
    if item.strip() != ''
]

quickSort(arr,0,len(arr)-1,'desc');
print(arr);
# attempt-1-end : 


# Note : 
# Time complexity : O(nlogN).
# Space complexity : stack space and not extrat space as we are sorting the same array. 