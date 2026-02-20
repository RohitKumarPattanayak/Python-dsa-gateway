# v-35 : find the pair in a array whose sum is equal to given n in pair a single number can occur once

sum_number = int(input("provide a number to find a pair : "))
num_array = [
    int(num)
    for num in input('Enter a comma separated numbers : ').split(',')
    if num.strip() != ''
]

def findAPair(arr,sum_number):
    hashDict = {}
    pairArr = []
    for i in range(len(arr)):
        target = sum_number-arr[i]
        target_index = hashDict.get(target,-1)
        if target_index>0:
            pairArr.append([i,target_index])
        hashDict[arr[i]] = i
    print(hashDict)
    return pairArr

print(findAPair(num_array,sum_number))