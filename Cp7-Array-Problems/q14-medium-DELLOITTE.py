# Provided an array [1,2,3,4] return the an array where in each index consist of multiplied vali=ue of all the other index except for the current index
# (classic prefix product + suffix product technique).
# resukt = [24,12,8,6]


num_arr = [1,2,3,1]
# Attempt-1-start
# def pre_compute_arr(arr):
#     p_c_left_arr = []
#     p_c_right_arr = [] 
#     cur_product = 1
#     for i in arr :
#         p_c_left_arr.append(cur_product)
#         cur_product*=i 

#     cur_product = 1
#     for i in range(len(arr)-1,-1,-1):
#         # print(i,cur_product,arr[i])
#         p_c_right_arr.append(cur_product)
#         cur_product*=arr[i]
#     # print(p_c_left_arr , p_c_right_arr)
#     return p_c_left_arr , p_c_right_arr[::-1]

# def other_mutiply_arr(arr):
#     len_arr = len(arr)
#     left_arr,right_arr = pre_compute_arr(arr)
#     return [
#         left_arr[i] * right_arr[i] 
#         for i in range(len_arr)
#     ]
# Attempt-1-end

def other_mutiply_arr_optimized(arr):
    result = [1] * len(arr)
    prefix = 1
    for i in range(len(arr)):
        result[i] *= prefix
        prefix*=arr[i]
    
    suffix = 1
    for i in range(len(arr)-1, -1, -1):
        result[i] *= suffix
        suffix *= arr[i]

    return result


print(other_mutiply_arr_optimized(num_arr))