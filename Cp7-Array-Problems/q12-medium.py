# v-36 :find the maxium sum array from an array

# KADENCE ALGORITHEM

num_array = [
    int(num)
    for num in input('Enter a comma separated numbers : ').split(',')
    if num.strip() != ''
]

def findMaxSum(arr):
    maxi = float("-inf")
    total = 0
    for i in range(len(arr)):
        total += arr[i]
        if(maxi < total):
            maxi = total
        if total < 0:
            total = 0
    return maxi

print(findMaxSum(num_array))

