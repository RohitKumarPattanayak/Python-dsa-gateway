# v-32 merge two sorted array as well remove dumplicates


arr1 = [int(num) for num in input("Enter multiple numbers separated by comma arr1 : ").split(',') if num.strip() != '']
arr2 = [int(num) for num in input("Enter multiple numbers separated by comma arr2 : ").split(',') if num.strip() != '']


def mergeSortedArray(arr1,arr2):
    i=j= 0
    finalArr = []
    arr1len = len(arr1)
    arr2len = len(arr2)
    
    while (i < arr1len and j< arr2len):
        if arr1[i] <= arr2[j]:
            if(len(finalArr) == 0 or finalArr[-1] != arr1[i]):
                finalArr.append(arr1[i])
            i+=1
        else :
            if(len(finalArr) == 0 or finalArr[-1] != arr2[j]):
                finalArr.append(arr2[j])
            j+=1

    if(i < arr1len-1):
        while(i < len(arr1)):
            if(finalArr[-1] != arr1[i]):
                finalArr.append(arr1[i])
            i+=1

    if(j < arr2len-1):
        while(j < len(arr2)):
            if(finalArr[-1] != arr2[j]):
                finalArr.append(arr2[j])
            j+=1
            
    return finalArr


print(mergeSortedArray(arr1,arr2))