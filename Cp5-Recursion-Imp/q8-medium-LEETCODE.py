def recurArr(arr,finalArr=[]):
    for i in arr:
        if isinstance(i,list):
            recurArr(i,finalArr)
        else:
            finalArr.append(i)
    return finalArr

def recurArrGen(arr):
    for i in arr:
        if isinstance(i,list):
            yield from recurArrGen(i)
        else:
            yield i


def recurObj(obj,newObj={},parent=''):
    for key, value in obj.items():
        key_name = f"{parent}->{key}" if parent else key
        if isinstance(value,dict):
            recurObj(value,newObj,key_name)
        else:
            newObj[key_name] = value
    return newObj           