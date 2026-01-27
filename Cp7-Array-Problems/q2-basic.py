# Find the second largest in a array

numbers = [
    int(item)
    for item in input("enter multiple numbers separated by comma: ").split(',')
    if item.strip() != ''
] 

large = second_large = 0
for i in numbers:
    if i > large:
        second_large = large
        large = i
    elif i != large  and  second_large < i:
        second_large = i

print(large,second_large)



        
        

