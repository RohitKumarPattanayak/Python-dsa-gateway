def binary_search_infinity(arr,item,batch=10000,lb=0,ub=0):
    if ub==0:
        ub=batch
    median = (lb+ub)//2
    if (arr[median]==item):
        return True, median
    if(lb>ub):
        return False
    if (arr[median] > item):
        return binary_search_infinity(arr,item,batch,lb,median-1)
    if (arr[median] < item):
        if (arr[ub] < item):
            return binary_search_infinity(arr,item,batch,ub+1,ub+batch+1)
        else:
            return binary_search_infinity(arr,item,batch,median+1,ub)        


# print(binary_search(arr,25))        

