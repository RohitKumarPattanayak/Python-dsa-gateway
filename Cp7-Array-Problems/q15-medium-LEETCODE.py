# pt-38 : Rearrange elements by sign

num_arr = [1,-1,-90,3,4,-5]

# attempt-1-start
# def rearrange_by_sign(arr):
#     new_list = []
#     sign = True
#     i=0
#     hash_dict = {}
#     while len(new_list) < len(arr):
#         if(sign):
#             if not hash_dict.get(arr[i],0) and arr[i] > 0:
#                 new_list.append(arr[i])
#                 hash_dict[arr[i]] = 1
#                 sign=False
#                 i=0
#             else :
#                 i+=1
#         else:
#             if not hash_dict.get(arr[i],0) and arr[i] < 0:
#                 new_list.append(arr[i])
#                 hash_dict[arr[i]] = 1
#                 sign=True
#                 i=0
#             else :
#                 i+=1
        
#     return new_list
# attempt-1-end


# attempt-3-start
# def rearrange_by_sign(arr):
#     new_arr = []
#     pos_arr = []
#     neg_arr = []

#     for i in arr:
#         if i >=0: 
#             pos_arr.append(i)

#     for i in arr:
#         if i < 0: 
#             neg_arr.append(i)
#     i=j=0
#     while len(new_arr) < len(arr):
#         if not len(new_arr):
#             new_arr.append(pos_arr[i])
#             i+=1
#         if new_arr[-1] >= 0:
#             new_arr.append(neg_arr[j])
#             j+=1
#         else:
#             new_arr.append(pos_arr[i])
#             i+=1
#     return new_arr
# attempt-3-end
            

# attempt-4-start -> Most optimized two pointer method
def rearrange_by_sign(arr):
    pos=0
    neg=pos+1
    new_arr = [0]*len(arr)
    for i in arr:
        if(i>=0):
            new_arr[pos]=i
            pos+=2
        else:
            new_arr[neg]=i
            neg+=2
    return new_arr
# attempt-4-end

print(rearrange_by_sign(num_arr))





