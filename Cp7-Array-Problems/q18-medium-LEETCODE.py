# Longest Substring Without Repeating Characters [SLIDING WINDOW]

input_str = 'abba'

# attempt 1 - WIll fail a lot of cases
# def longestSubstring(input_str):
#     i = j = 0
#     cur_set_map = set()
#     max_len = float("-inf")
#     cur_len = 0

#     if len(input_str) == 0:
#         return 0

#     while(j<len(input_str)):
#         if input_str[j] not in cur_set_map:
#             cur_set_map.add(input_str[j])
#             cur_len+=1
#         else:
#             max_len = max(cur_len,max_len)
#             cur_set_map.clear()
#             cur_len = 1
#             cur_set_map.add(input_str[j])   
#         j+=1
#     max_len = max(cur_len,max_len)
#     return max_len


# attempt 2 - Using two pointers
def longestSubstring(io_str):
    i=j=0
    max_len = float("-inf")
    hash_dict = {}

    if len(io_str) == 0:
        return 0 

    while (j<len(io_str)):

        got_Dup_index = hash_dict.get(io_str[j],False)

        if(got_Dup_index):
            i = max(i,int(got_Dup_index) + 1)
            cur_len = j-i+1
            hash_dict[io_str[j]] = j
        else:
            cur_len = j-i+1
        print(hash_dict,j,i,cur_len)
        hash_dict[io_str[j]] = str(j)
        j+=1
        max_len = max(cur_len,max_len)
    return max_len


# Cleaner attempt 3 
def longestSubstring(io_str):
    i = 0
    max_len = -1
    seen = {}
    for j in range(len(io_str)):
        if io_str[j] in seen:
            i = max(i,seen[io_str[j]] + 1)
        
        seen[io_str[j]] = j
        max_len = max(max_len,j-i+1)
    return max_len




print(longestSubstring(input_str))