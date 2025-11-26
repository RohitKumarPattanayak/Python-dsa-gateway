# Question : given two array n and m return the number of existance of each value of m in n.
# example :
# n = [1,1,2,3]
# m = [1,11,3]

# result : [2,0,1] 
# as 1 exists 2 times in array n
# as 11 doenst exists in array n
# as 3 exists once in array n

# Constraints 
# 1) 1 <=n{i}<=10 
# 2) n can have 10^8 elements 
# 3) m can have 10^8 elements



# attempt-1-start : 
# n = [
#     int(item)
#     for item in input("enter multiple numbers separated by comma for array N : ").split(',')
#     if item.strip() != ''
# ]
# m = [
#     int(item)
#     for item in input("enter multiple numbers separated by comma for array M (numbers you want to find occurance in array N) : ").split(',')
#     if item.strip() != ''
# ]
# def getFreqMap(arr):
#     hashDict = {}
#     for i in arr:
#         hashDict[i] = hashDict.get(i,0) + 1
#     return hashDict
# n_hash_dict = getFreqMap(n)
# result_arr = [
#     n_hash_dict.get(item,0)
#     for item in m
# ]
# print(result_arr)
# attempt-1-end :

# NOTE in the above i have used list comprehension to a practical extent (please go through the documentation for python list comprehension) 
# I have used dictionary for hashing in the above

# 1) time complexity O(n) (for freq_map) + O(m) (for iterating through m and geting freq from freq_map) => O(n)
# 2) space complexity n_hash_dict can have max of 10 values i,e [1<=n{i}<=10] as we only store freq for values from 1-10
# so n_hash_dict = O(10) + result_arr  = O(length(m)) -> O(10^8) 
# O(10) + O(10^8) => O(10^8)


# attempt-2-start : 
n = [
    int(item)
    for item in input("enter multiple numbers separated by comma for array N : ").split(',')
    if item.strip() != ''
]
m = [
    int(item)
    for item in input("enter multiple numbers separated by comma for array M (numbers you want to find occurance in array N) : ").split(',')
    if item.strip() != ''
]
def getFreqMapList(arr):
    hash_list = [0] * 11 # 1 <=n{i}<=10
    for i in arr:
        hash_list[i] = hash_list[i] + 1
    return hash_list
n_hash_list = getFreqMapList(n)
result_arr=[]
for num in m:
    if num > 10 or num < 1:
        result_arr.append(0)
    else:
        result_arr.append(n_hash_list[num])
print(result_arr)
# attempt-2-end :

# This approach is the same as the approach 1 but i have used List for hashing 
# all the other metrics remain same
