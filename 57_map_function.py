# Map function with multiples list

list1 = [1, 2, 3]
list2 = [10, 20, 30]

result = map(lambda x,y: x-y, list2, list1 )

print(list(result))