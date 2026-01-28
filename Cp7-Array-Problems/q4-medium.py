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
    for i in range(0,len(arr)-1):
        j = i+1
        while(arr[i] == arr[j]):
            print(i,j)
            print(arr[i],arr[j])
            if(j < len(arr)):
                print('in here')
                j+=1
            else :
                break
        # if j != i+1:
        #     arr[i+1],arr[j] = arr[j],arr[i+1]
    return arr

print(removeDuplicateOptimal(numbers))