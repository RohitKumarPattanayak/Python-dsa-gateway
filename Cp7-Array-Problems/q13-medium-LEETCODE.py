# find the Max stock buy/sell profit via an array which represents each day what price was the stock
# [1,6,3] => meaning day one it was 1rs and respectively
# now find out the max profit you can make 
# the output is 5 -> that is if you buy on day one and sell on day 2

num_array = [
    int(num)
    for num in input('Enter a comma separated numbers : ').split(',')
    if num.strip() != ''
]

# attempt-1-start : 
# def findMaxProfit(arr):
#     least_price = float("inf") 
#     least_index = 0
#     profit = 0
#     arr_len = len(arr)
#     for i in range(arr_len):
#         if least_price > arr[i]:
#             least_price = arr[i]
#             least_index = i
#     if(least_index < arr_len-1):
#         for i in range(least_index+1,arr_len):
#             cur_profit = arr[i] - arr[least_index]
#             if cur_profit > profit:
#                 profit = cur_profit
#     else:
#         return profit
#     return profit  

# attempt-2-start : 
def findMaxProfit(arr):
    least_price = float("inf") 
    profit = 0
    arr_len = len(arr)
    for i in range(arr_len):
        if(least_price > arr[i]):
            least_price = arr[i]
        else:
            cur_profit = arr[i]-least_price
            if(cur_profit > profit):
                profit = cur_profit     
    return profit  

print(findMaxProfit(num_array))