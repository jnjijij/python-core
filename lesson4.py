# print('hello')
#
#
# def func():
#     for i in range(7):
#         print(i)
#
#
# func()

# try:
#     # hsgfjshdgfjsy
#     # print(6/0)
#     int('hhh')
# except NameError as err:
#     print('error', err)
# except ZeroDivisionError as err:
#     print('error', err)
# except Exception as err:
#     print(err)
# else:
#     print('success')
# finally:
#     print('finally')
#
# print('Hello World')


# l = [i for i in range(50_000_000)]
# input()

# g = (i for i in range(3))
# # input()
#
# print(next(g))
# print(next(g))
# print('hjsfghjsfgjsf')
# print(next(g))

# for i in g:
#     print(i)
#
# for i in g:
#     print(i)


# def gen(name):
#     for ch in name:
#         yield ch


# g = gen('Max')
# # print(type(g))
# print(next(g))
# print('d')
# print(next(g))


# def gen(name):
#     for ch in name:
#         yield ch
#         print('1')
#
#
# g = gen('Max')
#
# print(next(g))
# print(next(g))
# print(next(g))

# def gen():
#     yield 1
#     yield 2
#     yield 3
#     return '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1'
#
#
# g = gen()
#
#
# try:
#     print(next(g))
#     print(next(g))
#     print(next(g))
#     print(next(g))
# except StopIteration as err:
#     print(err)


from uuid import uuid1


# def gen_file_name():
#     while True:
#         yield f'{uuid1()}.jpg'
#
#
# g = gen_file_name()
#
# print(next(g))
#
# print('work')
# print(next(g))


# def team_1_gen(n):
#     for i in range(1, n + 1):
#         yield f'{i}-Team1'
#
#
# def team_2_gen(n):
#     for i in range(1, n + 1):
#         yield f'{i}-Team2'
#
#
# teams = [team_1_gen(8), team_2_gen(5)]
#
# while teams:
#     team = teams.pop(0)
#
#     try:
#         print(next(team))
#         teams.append(team)
#     except StopIteration:
#         pass


# class MyRange:
#     def __init__(self, length):
#         self.__length = length
#         self.__counter = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.__counter < self.__length:
#             res = self.__counter
#             self.__counter += 1
#             return res
#         raise StopIteration
#
#
# # g = MyRange(5)
# for i in MyRange(8):
#     print(i)

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


# def my_range(length):
#     count = 0
#     while count < length:
#         yield count
#         count += 1
#
# for i in my_range(5):
#     print(i)


# file = open('111.txt')
# res = file.read(3)
#
# print(res)


# try:
#     file = open('111.txt')
#     try:
#         print(file.read())
#     finally:
#         file.close()
# except Exception as err:
#     print(err)

# try:
#     with open('111.txt', 'r') as file:
# print([file.readline()])
# print(file.readline())
# file.seek(0)
# print(file.readline())
# for line in file:
#     print(line)
# print(file.readlines())
# except Exception as err:
#     print(err)

# try:
#     with open('111.txt', 'w') as file:
#         # file.write('Hello World!\n')
#         print('Hello!!!!!!!!!!!', file=file)
# except Exception as err:
#     print(err)

# try:
#     with open('111.txt', 'x') as file:
#         print(file.read())
#         file.seek(0)
#         file.write('end\n')
# except Exception as err:
#     print(err)

# import json
# import pickle


# from typing import TypedDict
#
# User = TypedDict("User", {"name": str, "age": int})

# users: list[User] = [
#     {"name": "Max", "age": 8},
#     {"name": "Alex", "age": 18}
# ]

# try:
#     with open('users.db', 'wb') as file:
#         pickle.dump(users, file)
# except Exception as err:
#     print(err)

# try:
#     with open('users.db', 'rb') as file:
#         users:list[User] = pickle.load(file)
#         print(users)
#         print(users[0]['name'])
# except Exception as err:
#     print(err)


# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# users: list[User] = [
#     User("John", 25),
#     User("Smith", 35)
# ]
#
# # try:
# #     with open('users.db', 'wb') as file:
# #         pickle.dump(users, file)
# # except Exception as err:
# #     print(err)
#
# try:
#     with open('users.db', 'rb') as file:
#         users: list[User] = pickle.load(file)
#         print(users)
#         print(users[0].name)
# except Exception as err:
#     print(err)

# choice = input('Enter num: ')
#
# match choice:
#     case '1':
#         print(1)
#     case '2':
#         print(2)
#     case _:
#         print('default')


# a = ('right', 200, 'sdfsdf', 'sdfsdfsdf')
#
# match a:
#     case 'top' | 'left' as action, value:
#         print(action, value)
#     case (a, ):
#         print('one', a)
#     case 'right', 200, *args:
#         print(args)
#     case _:
#         print('default')


class User:
    __match_args__ = ("name", "age")

    def __init__(self, name, age):
        self.name = name
        self.age = age


user_class = User('Max', 3)

user_dict = {'name': 'Kira', 'age': 25}


# def matcher(source: User | dict):
#     if isinstance(source, User):
#         print(source.name)
#     elif isinstance(source, dict):
#         print(source['name'])


# matcher(user_dict)

def matcher(source: User | dict):
    match source:
        case User(name, age=3):
            print(name)
        case {'name': 'Kira' as name, 'age': age}:
            print(name)


matcher(user_dict)
