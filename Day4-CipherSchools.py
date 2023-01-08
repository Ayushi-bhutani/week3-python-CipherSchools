l1 =[1,3,5,7]
l2 =[2,4,6,8]
new_list = []

# l =[(1,2), (3,4), (5,6), (7,8)]
# *operator with zip

# l1, l2 = list(zip(*l))
# print(list(l1))
# print(list(l2))
for pair in zip(l1,l2):
    new_list.append(max(pair))

print(new_list)

# any , all function

numbers1 = [13,1,9,7,10]
numbers2 = [1,2,3,4,5,6]

print(any([num%2==0 for num in numbers1]))
print(all([num%2==0 for num in numbers1]))

# evens1 = []
# for num in numbers1:
    # evens1.append(num%2==0)

# print(all([True, False, True, True])) #----> False

#advabnce min() and max()

# numbers = [1,2,4,5,7]
# print(min(numbers))


names = ['Uttam aggarwal', 'Moihit', 'ab', 'z']
print(max(names,key = lambda item : len(item)))

students = {
    'Uttam' : {'score':50, 'age': 24},
    'mohit' : {'score':75, 'age': 19},
    'rohit' : {'score':76, 'age': 23}
}

print(max(students, key = lambda item : students[item]['age']))

# students2 = [
#     {'name':'Uttam','score':90, 'age': 24},
#     {'name':'mohit','score':70, 'age': 19},
#     {'name':'rohit','score':60, 'age': 23},
# ]
# print(max(students2,key = lambda item:item.get('age'))['name'])