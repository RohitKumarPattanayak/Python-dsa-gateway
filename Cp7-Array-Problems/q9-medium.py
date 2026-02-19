# find the missing number in the array
# example : [0,9,2,3,4,7,6,1,5]
# output : 8

numArr = [0,8,2,3,4,7,6,1,5]


# attempt-1-start : 
# def findMissingNumber(arr):
#     hashDict = {}
#     for i in range(len(numArr)+1):
#         hashDict[i] = hashDict.get(i,0)

#     for num in numArr:
#         hashDict[num] = 1

#     for key,value in hashDict.items():
#         if value == 0:
#             return key
# attempt-1-end : 

def findMissingNumber(arr):
    expectedSum=0
    for i in range(0,len(arr)+1):
        expectedSum+=i
    actualSum=0
    for num in arr:
        actualSum+=num
    return expectedSum - actualSum
print(findMissingNumber(numArr))
