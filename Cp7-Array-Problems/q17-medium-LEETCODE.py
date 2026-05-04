# Find maximum sum k-sub array [SLIDING WINDOW]

# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# arr = [-1, -2, -3, -4]
# arr = [0, -1, 2, 3, -5, 0]

arr=[1, 2, 3, 4, 5]
k = 2
# attempt 1
def maxKSubArr(arr,k=0):
    max_sum=float("-inf")
    cur_sum=0
    i=0
    j= i+k-1
    tmp=i
    while(j<len(arr)):
        if(tmp<=j):
            cur_sum+=arr[tmp]
            tmp+=1
        else:
            max_sum=max(cur_sum,max_sum)
            cur_sum=0
            i+=1
            j+=1
            tmp=i


    return max_sum

# attempt 2
def maxKSubArr(arr,k=0):
    window_size = sum(arr[:k])
    max_size = window_size

    for i in range(k,len(arr)):
        window_size += arr[i]
        window_size -= arr[i-k]
        max_size = max(window_size,max_size)
    return max_size

print(maxKSubArr(arr,k))



