# Problem: Minimum Size Subarray Sum
# Given an array of positive integers nums and a positive integer target, return the minimum length 
# of a contiguous subarray whose sum is greater than or equal to target.
# If there is no such subarray, return 0.

# Example 1
# Input:
# target = 7
# nums = [2,3,1,2,4,3]

# Output:
# 2

# Explanation:
# The subarray [4,3] has sum 7 and length 2, which is the minimum possible.

# Example 2
# Input:
# target = 4
# nums = [1,4,4]

# Output:
# 1


k = 7
nums = [2,3,1,2,4,3]

def getMinSubArrayLen(arr,k):
    prefix_sum = 0
    hash_prefix_sum_index = {}
    min_len = float("inf")

    for i in range(len(arr)):
        prefix_sum+=arr[i]

        diff = prefix_sum - k

        if(prefix_sum == k):
            min_len = i+1

        if diff in hash_prefix_sum_index:
            # f_occur = hash_prefix_sum_index[diff] + 1
            # cur_subArr_len = (i - f_occur) + 1
            cur_subArr_len = i - hash_prefix_sum_index[diff]
            min_len = min(min_len,cur_subArr_len)

        if prefix_sum not in hash_prefix_sum_index:
            hash_prefix_sum_index[prefix_sum] = i

    return min_len

print(getMinSubArrayLen(nums,k))    
