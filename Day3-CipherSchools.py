# kwargs (keyword arguments)
# **kwargs (double star operator)

# kwargs as a parameter
def func(**kwargs):
    for k,v in kwargs.items():
        print(f'{k} : {v}')

# dictionary unpacking
d= {'name':'janvi', 'age':24}
func(**d)

# functions with all parameters
# very important to understand

# PADK

# parameters
# *args
# default parameters
# **kwargs

def func(name, *args, last_name = 'unknown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

func('Uttam', 1,2,3, a=1, b=2)

# function 
# list , reverse_str = True
# list

def func(l, **kwargs):
    if kwargs.get('reverse_str') == True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]


names = ['ayushi', 'sister']
print(func(names, reverse_str = True))

def add(a,b):
    return a+b

def new_add(*args):
    # 1,2,3,4
    # (1,2,3,4)
    total = 0
    for num in args:
        total+= num
    return total


# print(new_add(1,2,3))

# l=(1,2,3,4)
# print(new_add(*l))

# kwargs - keyword arguments , **
# def func(**kwargs):
    # print(kwargs) #gather as dictionary
    # print(type(kwargs))

# func(name = 'sanvi', age = 24)

# kwargs , args , normal, default
# PADK - parameter , args , default , kwargs

def func2(name, *args, last_name = 'unknown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

func2('ayushi', 1,2,3, a=1, b=2)

# functions with all parameters
# very important to understand

# PADK

# parameters
# *args
# default parameters
# **kwargs

def func(name, *args, last_name = 'unknown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

func('Uttam', 1,2,3, a=1, b=2)

# lambada expressions (anonymous function)

def add(a,b):
    return a+b

add2 = lambda a,b : a+b
print(add2(2,3))


multiply = lambda a,b : a*b
print(multiply(2,3))

print(add)
print(add2)
print(multiply)

# we use enumerate function with for loop to track position of our
# item in iterable


# How we can do this without enumerate function
names = ['abc', 'abcdef', 'aayush']
# # 0 -- 'abc'
# # 1 -- 'abcdef'
# pos = 0
# for name in names:
#     print(f"{pos} ---> {name}")
#     pos+=1


# with enumerate function

# for pos,name in enumerate(names):
    # print(f"{pos} ---> {name}")




# Define a function that take two arguments
# 1.) list containing string
# 2.) string that want to find in your list
# and this function will return the index of string in your list and
# if string is not present then return -1

def find_pos(l, target):
    for pos, name in enumerate(l):
        if name== target:
            return pos
    return -1

print(find_pos(names, 'ayushi'))

