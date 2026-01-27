# Check if an array is sorted

numbers = [
    int(item)
    for item in input("enter comma separated numbers : ").split(',') 
    if item.strip() != ''
]

def isSorted(numbers):
    for i in range(0,len(numbers)-1):
        print(i,i+1)
        if numbers[i] > numbers[i+1]:
            return False
    return True

print("the array sort status is :",isSorted(numbers))