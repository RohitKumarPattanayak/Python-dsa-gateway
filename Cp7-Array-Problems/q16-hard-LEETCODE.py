# Find the largest concequetive array length from a given array

num_arr = [1,99,101,98,2,5,3,100,4]

# attempt-1
# def get_len(num,hashDict: dict):
#     if not hashDict.get(num,0):
#         return 0
#     del hashDict[num]
#     return 1 + get_len(num+1,hashDict) + get_len(num-1,hashDict)

# def find_L_c_arr(arr):
#     hash_dict = {}
#     for i in arr:
#         hash_dict[i]=1
#     longest = float("-inf")
#     for i in arr:
#         cur_long = get_len(i,hash_dict)
#         if longest < cur_long:
#             longest = cur_long
#     return longest


# attempt-2
# def find_L_c_arr(arr):
#     sorted_arr = sorted(arr)
#     longest = float("-inf")
#     last_num = float("-inf")
#     cur_count = 0
#     for i in range(len(sorted_arr)):
#         cur_num = sorted_arr[i]
#         if last_num != cur_num-1:
#             cur_count = 1
#             last_num = cur_num
#         elif last_num == cur_num-1:
#             cur_count+=1
#             last_num = cur_num

#         longest = max(longest,cur_count)
#     return longest

# attempt -3 
def find_L_c_arr(arr):
    hash_set = set(arr)
    longest = float("-inf")
    for i in hash_set:
        if i-1 in hash_set:
            continue
        
        count = 1
        num = i + 1
        while num in hash_set:
            count+=1
            num+=1
        
        longest = max(longest,count)
    return longest
print(find_L_c_arr(num_arr))


