# Rotate the given list/arr by k rotations

numbers = [
    int(item)
    for item in input('Enter a comma sep numbers : ').split(',')
    if item.strip() != ''     
]
rotation = int(input('Enter how many rotations you want in the above array : '))

def kRotateViaSlicing(arr,k):
    n = len(arr)
    k = k%n   # because if the arr len is 6 and rotation is also 6 then there if no change in arr, as after 6 rotation it will be same as before.
    if k==0:  # similarly if there arr len is 6 and rotation is 8 then actualyy you have to rotate only 2 times hence (k%n)
        return arr
    return arr[n-k:] + arr[:n-k]

# No extra space taken in this method
def kRotateViaIterartion(arr, k):
    def reverse(start,stop) :
        while (start<stop):
            arr[start],arr[stop] = arr[stop],arr[start]
            start+=1
            stop-=1    
    n = len(arr)
    k = k%n
    if (k==0):
        return arr 
    reverse(k,n-1)
    reverse(0,k-1)

    # final reverse
    reverse(0,n-1)
    return arr

print(kRotateViaIterartion(numbers,rotation))

