# Given an integer array nums and an integer k, return the total number of continuous subarrays whose sum equals k.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Input:
# nums = [1,1,1]
# k = 2

# Output: [1,1] [1,1]
# 2 

# Input:
# nums = [1,2,3] 
# k = 3

# Output: [1,2] [3]
# 2



nums = [1,2,3] 
k = 3

def getNoSubK(arr,k):
    i=0
    prefix = arr[i]
    count_sub_arr = 0
    for j in range(1,len(arr)):
        prefix+=arr[j]
        print(i,j,prefix)
        if prefix == k:
            count_sub_arr+=1
        elif prefix > k:
            i=j-1
            prefix=arr[i] + arr[j]
            if prefix == k:
                count_sub_arr+=1
    return count_sub_arr

print(getNoSubK(nums,k))
