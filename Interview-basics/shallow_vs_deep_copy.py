# 1) Reference Assignment

numList1 = [1,2,3]
numList1_ref = numList1

arrList1 = [[1,2,3],[4,5,6]]
arrList_ref = arrList1

# numList1_ref[2] = 4
# arrList_ref[1] = ['a','b','c']


# print(id(numList1) , numList1)
# print(id(numList1_ref), numList1_ref)

# print(id(arrList1) , arrList1)
# print(id(arrList_ref), arrList_ref)



# 2) Shallow copy : A shallow copy creates a new outer object, but inner objects are still shared.
import copy

# shallow types copy
# numList1_shallow = copy.copy(numList1)
# # numList1_shallow = numList1[:]
# # numList1_shallow = list(numList1)
# # numList1_shallow = numList1.copy()

# numList1_shallow[2] = 4

# print(id(numList1) , numList1)
# print(id(numList1_shallow), numList1_shallow)

# arrList_shallow = copy.copy(arrList1)
# # arrList_shallow = arrList1[:]
# # arrList_shallow = list(arrList1)

# # arrList_shallow[1] = ['a','b','c']
# arrList_shallow[1][1] = '2' # IMPORTANT

# print(id(arrList1) , arrList1)
# print(id(arrList_shallow), arrList_shallow)



# 3) Deep copy : A deep copy creates a new outer object and newer inner objects.

# shallow types copy
numList1_deep = copy.deepcopy(numList1)
numList1_deep[2] = 4

print(id(numList1) , numList1)
print(id(numList1_deep), numList1_deep)


arrList1_deep = copy.deepcopy(arrList1)
# arrList1_deep[1] = ['a','b','c']

arrList1_deep[1][1] = '2'

print(id(arrList1) , arrList1)
print(id(arrList1_deep), arrList1_deep)