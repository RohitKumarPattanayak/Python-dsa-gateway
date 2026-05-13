# Given an integer array nums and an integer k, return the total number of contigenious subarrays whose sum equals k.

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



nums = [1,1,1] 
k = 2

def getNoSubK(arr,k):
    hash_prefix_sum = {0:1}
    numSubArr = 0
    prefix_sum = 0
    
    for i in range(len(arr)):
        prefix_sum+=arr[i]
        diff = prefix_sum-k
        if diff in hash_prefix_sum:
            numSubArr+=1
        hash_prefix_sum[prefix_sum] = 1
    return numSubArr

print(getNoSubK(nums,k))
