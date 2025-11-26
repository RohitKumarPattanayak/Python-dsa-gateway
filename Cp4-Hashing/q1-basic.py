# Hashing (in the context of python) : Pre-storing processed data in certain datastructure (dict/set/list) so it could be fetched efficiaently.
# like in the below we will pre store the frequency/ occurances before hand so we could fetch later

## question
## 1) For numerical input array and an input number reurn a frequency of the given number in the array

# attempt-1-start : 
# numbers = [
#     int(item)
#     for item in input("enter multiple numbers separated by comma: ").split(',')
#     if item.strip() != ''
# ]
# number= int(input("Enter the number you want to check frequency in the abov list: "))
# freq_map = {}

# for i in numbers:
#     if i in freq_map:
#         freq_map[i] +=1
#     else:
#         freq_map[i] = 1

# if number in numbers:
#     print(freq_map[number])
# else:
#     print(0)
# attempt-1-end :


# NOTE
## 1) In the above code i have used "list comprehension" I have used it to handle inputs like 1,2,3, (extra trailing comma)
# new_list = [expression for item in iterable if condition]
# 'expression': This is the operation applied to each item that satisfies the condition. It determines what value is added to the new_list.
# 'item': This is a variable that takes on each value from the iterable during the iteration.
# 'iterable': This is the source sequence (e.g., a list, tuple, range) from which items are drawn.
# 'if condition' (optional): This is a filter that determines whether an item is processed by the expression and included in the new_list. Only items for which the condition evaluates to True are included.

# examples
    # numbers = [1, 2, 3, 4, 5]
    # squares = [n * n for n in numbers]
    # # squares will be [1, 4, 9, 16, 25]

    # numbers = [1, 2, 3, 4, 5, 6]
    # even_numbers = [n for n in numbers if n % 2 == 0]
    # # even_numbers will be [2, 4, 6]


# attempt-2-start : 
numbers = [
    int(item)
    for item in input("enter multiple numbers separated by comma: ").split(',')
    if item.strip() != ''
]
number= int(input("Enter the number you want to check frequency in the abov list: "))
freq_map = {}

for i in numbers:
    freq_map[i] = freq_map.get(i,0) + 1 
print(freq_map.get(number,0))
# attempt-2-end :

## 1) In the above code i have used python dictionary and its .get() method to make our code more optimized and readable please go through the concept once

# 1) Time complexity : as we are using a for it is O(n) and we are using .get() method of dictionary which is time complexity O(1) due to indexing please reffer below mentioned links in case of confusion
# 2) Space complexity : numbers -> O(n) for input and as our freq_map will have all the unique number so O(k) where k is unique numbers in n.
# so worst case if all the numbers in the array is unique the overall space complexity is O(n) 


# Please check the below link 
# - https://wiki.python.org/moin/TimeComplexity
# = https://www.youtube.com/watch?v=PLV0f4RAMvI&list=PLhR2IpV1b2FwWwviBHRrR118YAaSlyhTU&index=6