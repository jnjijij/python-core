# lksjdflksjfklj

"""
ljshflsjhdf
jkfhgjshfjsk
jkhsdfksjf

"""

'''
sdfsdfsdfsd
sdfsdfsdf
'''

# print('hello from python')

# print(1, 2, 3, sep='  ', end='')

# i = 3
# f = 1.3
# b = True  # False
# s = 'text'  # "text"
# n = None
#
# print(type(i))
# print(type(f))
# print(type(b))
# print(type(s))
# print(type(n))


# num = '2sdf'
#
# res = int(num)
#
# print(type(res))
# print(res)


# a=b=c=10
#
# print(a,b,c)


a = 13
b = 6
# a++
# a += 1

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(round(5/2))
# print(11%3)
# print(25**25)
#
# print(2525**2525)


a = 2
b = 3
#
# print(a < b)
# print(a <= b)
# print(a >= b)
# print(a == b)  # is
# print(a != b)  # is not

# print(isinstance('jhsgfjsf', str))


# if a ==b:
#     print()
#     print()
#     print()
#     print()
#     if a <b:
#         print()
#         print()
#         print()
#         print()
#     print()


# if a == b and a > b or a != b:
#     print('a==b')
# elif a==5:
#
# else:
#     print('a is not b')

# b = False
#
# if not b:


# res = input('Enter num: ')
# print(res)

# num = input('Enter num: ')
#
# res = 'yes' if num == '5' else 'no'
#
# print(res)


# list

# l = [1, 2, 3, 4, 5, 6]

# print(l[2])
# print(l[-2])
# # print(l[33]) # error
#
# l[0] = 555
# print(l)
#
# del l[1]
# # del l[11]
#
# print(l)
# print(len(l))
#
# l2 = l
#
# l2[0]=777
#
# print(l)
# print(l2)


# l = [1, 2, 3, 4, 5, 6, 2, 3, 3, 3]
# l = list()

# l.append(22)
# l.insert(2, 777)
# pop = l.pop()
# pop = l.pop(2)
# print(pop)
# print(l.index(2, 3))

# l.reverse()
# l.sort()
# l.sort(reverse=True)
# print(l.count(3))
# l2 = l.copy()
# l.remove(3)
# l.clear()
# print(l)

# l = [1, 2, 3, 4, 5, 6]
# # l.extend([99,88,77])
# l = [44, 55, 66] + [1, 2, 3]
# print(l)
#
# l2 = l[::-1]
#
# print(l2)


# my_tuple = (1, 2, 3, 4, 5, 6, 'www')
# print(my_tuple[3])
# # del  my_tuple[3]
# print(my_tuple)
#
# my_tuple.


# dictionary = {
#     'name': "max",
#     1: 25
# }
# dictionary = dict(name='max', house=25)
# dictionary['street'] = 'asd'
# print(dictionary)
# print(dictionary['name'])
# print(dictionary[1])
# print(dictionary['ddd'])
# dictionary['street'] = 'asd'
# print(dictionary)

# print(dictionary.get('name'))
# print(dictionary.get('name1'))
# print(dictionary.get('name1',555))

# dictionary.clear()
# dictionary.copy()
# print(dictionary.items())
# print(list(dictionary.values()))
# print(list(dictionary.keys()))

# pop = dictionary.pop('name')
#
# print(dictionary)
# print(pop)

# popitem = dictionary.popitem()
# print(dictionary)
# print(popitem)


# dictionary = dict(name='max', house=25)
# dictionary['street'] = 'asd'
#
# # dictionary.setdefault('namewww','Alex')
# # print(dictionary)
#
# dictionary.update({'city': 'Lviv'})
# dictionary|={'asd':55, 'fgh':'dfdsfsdf'}
#
# print(dictionary)

# l = [1, 2, 3, 4, 5, 3, 1, 2]
#
# s = set(l)
#
# print(s)

# s = {1,2,3,4,2,1,3,6}
#
# print(s)

# s = {}
# # print(type(s))
# d = dict()
#
# print(type(d))
# print(d)


# s = {1,2,3,4,2,1,3,6}
#
# s.add(55)
#
# print(s)

# s1 = {1,2,3,4,5}
# s2 = {6,9, 2,5}
#
# print(s1.issuperset(s2))
# print(s1.issubset(s2))
# print(s1.isdisjoint(s2))
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))
# print(s1.symmetric_difference(s2))
# s1.update(s2)
# # s1.remove(222)
# # s1.discard(222)
# pop = s1.pop()
# print(s1)

# print('*'*20)
name = 'Max'
age = 18
weight = 70.5

string = 'Hello, my name is Max, I`m 18 and my weight 70.5 kg'
string = 'Hello, my name is ' + name + ', I`m ' + str(age) + ' and my weight ' + str(weight) + ' kg'
string = 'Hello, my name is %s, I`m %d and my weight %f kg' % (name, age, weight)
string = 'Hello, my name is {}, I`m {} and my weight {} kg'.format(name, age, weight)
string = 'Hello, my name is {name}, I`m {age} and my weight {weight} kg'.format(age=age, weight=weight, name=name)
string = f'hello, my name is {name}, I`m {age} and my weight {weight} kg'

# print(string)

# print(string[2])
# print(string.index('l'))
# print(string.index('ll'))
# print(string.find('z'))
# print(string.count('l'))
# print(string.capitalize())
# print(string.upper())
# print(string.lower())

# print('111hhh'.isalnum())
# print('hhh'.isalpha())
# print('111'.isdigit())
# print('sdfsf'.islower())
# print('SSS'.isupper())
# print('     '.isspace())
# print('Dddd'.istitle())
#
# print('ddddd sdddd'.title())
# print('dSddd sDddd'.swapcase())
# print('dSddd sDddd'.startswith('dS'))
# print('dSddd sDddd'.endswith('d'))
# print('dSddd-dddd-dd'.split('-'))
# print('dSddd-dddd'.partition('-'))
#
# print(['        dddd    '.strip()])
# print(['        dddd    '.rstrip()])
# print(['        dddd    '.lstrip()])

# print('-'.join(['1', '2', '3']))
#
# print('hello world'.replace('l', 'WWW'))

# print(min([1,4,3,-1,5,7]))
# print(min(1,4,3,-1,5,7))
# print(max(1,4,3,-1,5,7))
# print(sum([1,4,3,-1,5,7]))
# print(sorted([7, 2, 3, 4, 5, 6]))
# print(sorted([7, 2, 3, 4, 5, 6], reverse=True))
# print(pow(2, 25))
# print(2 ** 25)


# def func(a=2,b=2,c=2):
#     print(a,b,c)
#
# func()


# def func(a, b, c, *args, **kwargs):
#     print(a, b, c)
#     print(args)
#     print(kwargs)
#
#
# func(2, 3, 4, 5,6,7,8, name='max',age=15)


i = 5

# while i>=0:
#     print(i)
#     i-=1
#     if i==3:
#         break
# else:
#     print('finish')

# l = [1,2,3,4]
#
# for i in l:
#     print(i)
# else:
#     print('finish')

# for i in range(4,15,3):
#     print(i)


# l = [1,2,3,4]
#
# for i, v in enumerate(l):
#     print(f'{i=}')
#     print(f'{v=}')

# l = [i for i in range(5)]
# print(l)


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# res = [i**2 for i in l]
# res = [i ** 2 for i in l if i % 2 == 0]
# res = [i ** 2 if i != 4 else i for i in l if i % 2 == 0]

# l = [1,2,3,4,2,3]
#
# print(33 in l)

dict1 = {
    'name':'max',
    'age':15
}

for k,v in dict1.items():
    print(f'{k=}')
    print(f'{v=}')
