# Longest Subarray With Sum K

# Given an integer array nums and an integer k, return the length of the longest contiguous subarray whose sum equals k.

# If no such subarray exists, return 0.

# Input:
# nums = [1, -1, 5, -2, 3]
# k = 3

# Output:
# 4

# Explanation:
# The subarray [1, -1, 5, -2] has sum 3 and length 4.

# Input:
# nums = [-2, -1, 2, 1]
# k = 1

# Output:
# 2

# Explanation:
# The subarray [-1, 2] has sum 1.

nums = [1, -1, 5, -2, 3]
k = 3

def getLongSubArrLenOfK(arr,n):
    prefix_sum = 0
    hash_prefix_sum_index = {}
    longest_len = 0

    for i in range(len(arr)):
        prefix_sum+=arr[i]

        diff = prefix_sum - k

        if(prefix_sum == k):
            longest_len = i+1

        if diff in hash_prefix_sum_index:
            # f_occur = hash_prefix_sum_index[diff] + 1
            # cur_subArr_len = (i - f_occur) + 1
            cur_subArr_len = i - hash_prefix_sum_index[diff]
            longest_len = max(longest_len,cur_subArr_len)

        if prefix_sum not in hash_prefix_sum_index:
            hash_prefix_sum_index[prefix_sum] = i

    return longest_len

print(getLongSubArrLenOfK(nums,k))
