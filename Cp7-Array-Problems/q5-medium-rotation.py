# Rotate a givem arr/list by one place


numbers = [
    int(item)
    for item in input("Enter number separated array : ").split(',')
    if item.strip != ''
]

def rotateOneViaSlicing(arr):
    n = len(arr)
    RightRotateNums = arr[1:] + [arr[0]]
    LeftRoatateNums = [arr[-1]] + arr[:n-1]
    return RightRotateNums , LeftRoatateNums

# left roatate
def rotateOneViaIteration(arr):
    n = len(arr)
    tmp = arr[n-1]
    for i in range(n-2,-1,-1):
        arr[i+1] = arr[i]
    arr[0] = tmp
    return arr;        

print(numbers)
print(rotateOneViaIteration(numbers))