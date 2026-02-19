# Move all zeroes to the end of the array


numbers = [int(num) for num in input("Enter multiple numbers separated by comma: ").split(',') if num.strip() != '']


def moveZerosToEnd(arr):
    arrlen = len(arr)
    i=0
    if arrlen == 1:
        return arr
    while i < arrlen:
        if(arr[i]==0):
            break
        i+=1    
    if i == arrlen:
        return arr
    j=i+1
    while j < arrlen:
        if(arr[j] != 0):
            arr[j],arr[i] = arr[i],arr[j]
            i+=1
        j+=1
    return arr

print(moveZerosToEnd(numbers))
