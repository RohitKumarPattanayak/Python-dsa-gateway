# Remove duplicate from an sorted array

numbers = [
    int(item)
    for item in input("Enter comma sepoarated numbers :").split(',')
    if item.strip != ''
]
def removeDuplicate(arr) :
    heap = {}
    for i in arr:
        heap[i] = 1
    index = 0
    for h_value in heap:
        arr[index] = h_value
        index+=1
    return arr[:index]

def removeDuplicateOptimal(arr) :
    i = 0
    j = i+1
    n = len(arr)
    while ( j < n ):
        if(arr[j] != arr[i]):
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
        j+=1    
    return arr[:i+1]
        

print(removeDuplicateOptimal(numbers))