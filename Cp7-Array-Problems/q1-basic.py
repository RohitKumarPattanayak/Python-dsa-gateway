# find the largest number in the array
numbers = [
    int(item)
    for item in input("enter multiple numbers separated by comma: ").split(',')
    if item.strip() != ''
] 
large = 0
for i in numbers:
    if i > large:
        large = i
print(large) 

