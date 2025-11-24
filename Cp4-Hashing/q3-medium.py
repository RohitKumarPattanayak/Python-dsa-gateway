# Question : given a string n and arry of chr m return number of existance of each chr of m in string n

# Constraints : 
# 1) 'a' <= s[i] <= 'z' 97-122 (ascii value)

# attempt-1-start : 
n = input("enter string N : ")
m = [
    item
    for item in input("enter multiple numbers separated by comma for array M (numbers you want to find occurance in array N) : ").split(',')
    if item.strip() != ''
]
def getfreqHashList(str):
    hashList = [0] * 123 # 'a' <= s[i] <= 'z'
    for i in str:
        hashList[ord(i)] = hashList[ord(i)] + 1
    return hashList
n_hash_list = getfreqHashList(n)
result_arr = []
for str in m:
    if ord(str) > 122 or ord(str) < 97:
        result_arr.append(0)
    else :
        result_arr.append(n_hash_list[ord(str)])
print(result_arr)
# attempt-1-end :


# Always check how to use constraints to your benefit. The constraint is the reason i used hash_list rather than hash_dict
# and as well i used ord() to convert charecters into ascii equicalent integers

# Time complexity and Space complexity are similar to the previous problem please reffer the same
