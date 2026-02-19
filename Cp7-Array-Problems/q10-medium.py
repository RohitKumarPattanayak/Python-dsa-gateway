# Find maximum consequetive 'n' Sum


numArr = [1,1,2,0,0,1,1,1,1,1,0,1,2,1,1,1,1,1,1,0,1]

def consequetiveSum(num,arr):
    i=0
    # j=1
    count = 0
    max_count = 0
    while i<len(arr):
        if arr[i]==num:
            count+=1
        else:
            if count > max_count:
                max_count = count
            count = 0
        i+=1
    return num*max_count

print(consequetiveSum(2,numArr))