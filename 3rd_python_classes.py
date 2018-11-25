# b = 10

# if b > 20:
#     print('yes')
# elif b <= 15:
#     print('elif hold')
# else:
#     print('no')

# b = 10
# c = 100
# if b > 50 and c < 70:
#     print ('first condition holds')
# elif b < 5 or c < 50:
#     print('second condition holds')
# else :
#     print('none holds')

# b = 5.7
# if isinstance(b, float):
#     print('yes')
# else:
#     print

# for x in range(2, 11):
#     print(x)

# my_list = []
# for x in 'banana':
#     my_list.append(x)
# print(*my_list)

# count = 0
# while count < 9:
#     print('the count is- ', count)
#     count = count + 1
# print('Goodbye!')

# NESTED LOOPS
# for x in range(1, 1000):
#     for y in range(1, 10000):
#         print(x * y)

# a = True
# while a:
#     print('Running')
#
# i = 1
# while i < 7:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# animals = ['cow', 'goat', 'dog']
# for x in animals:
#     print(x)
#     if x == 'goat':
#         break

# i = 1
# while i < 7:
#     i = i + 1
#     if i == 3:
#         continue
#     print(i)

# animals = ['cow', 'goat', 'dog']
# for x in animals:
#         if x == 'goat':
#             continue
#         print(x)

# my_list = [3, 5, 9]
# for i in range(1, 11):
#     if i in my_list:
#         continue
#     print(i)

# a = [3, 5, 9]
# i = 0
# while i < 10:
#     i += 1
#     if i in a:
#         continue
#     print(i)

# for letter in 'Python':
#     if letter == 'h':
#         pass
#         print('This is pass block')
#     print('Current letter: ', letter)
# print('Goodbye!')

# Exercise- Display output of squares between 1 and 20 and omit [9, 36 and 64]
# m = [9, 36, 64]
# a = 0
# while a <= 20:
#     a += 1
#     z = a**2
#     if z in m:
#         continue
#     print(z)

# a = [1, 4, 6, 4]
# a.append(4)
# a.remove(4)
# z = a.count(4)
# print(z)

# How to sort elements in a list
# a = [1, 2, 5, 9, 5]
# a.sort()
# print(a)


# a = ['b', 'e', '1', '24', 'mango']
# x = a[-len(a):]
# print(x)

# squares = []
# for x in range(10):
#     squares.append(x**2)
# print(squares)

# List comprehension
# squares = [x**2 for x in range(21)]
# print(squares)


# FOURTH PYTHON CLASSES
# a = [1, 2, 5, 9, 5]
# y = a[::-1]
# print(y)

# combs = []
# for x in [1, 2, 3]:
#     for y in [2, 1, 4]:
#         if x != y:
#             combs.append((x, y))
# print(combs)

# using a dictionary
# diction = {'name':'sam', 'age':'12', 'dob':'12th September, 1991'}
# print((diction['name']), diction['age'])

# cart = {
#          'name': 'muyiwa',
#          'item': {'pen': 500, 'book': 70},
#          'totalPrice': 550
#        }
# print(cart['item']['pen'])
# cart = {'name': 'ken', 'item': {'pen': 500, 'book': 70}, 'totalPrice': 550, 'address': '42, Montgomery Road'}
# cart['sizes']=['small', 'medium', 'large']
# print(cart['sizes'][1])
# cart = {'name': 'ken', 'item': {'pen': 500, 'book': 70}, 'totalPrice': 550, 'address': '42, Montgomery Road'}
# # del cart['name']
# j = cart.items()
# print(j)

# assignment factorial
# METHOD 1
#
# get the computer to identify and declare factorial values
# first get the user input values
# fac = 1
# user_input = int(input('Enter initial value and press enter -'))
# for x in range(1, user_input + 1):
#     fac = fac * x
#     #
#     # y = 1 * 1 = 1
#     #     1 * 2 = 2
#     #     2 * 3 = 6
#     #     6 * 4 = 24
#     #     24 * 5 = 120
#     #     120 * 6 = 720
# print(fac)
# METHOD 2
# user_input = int(input('Enter initial value and press enter -'))
# fac = 1
# while user_input > 0:
#     fac = fac * user_input
#     user_input = user_input - 1
# print(fac)


# Fifth Python Classes

# Writing a function
# def add_numbers(a, b):
#     """A function to add arguments a and b"""
#     c = a + b
#     return c
#
#
# print(add_numbers(800, 900))

# def print_info(name, age="unknown"):
#     """This function prints the info that is passed ino the function"""
#     print("Name:", name)
#     print("Age", age)
#     return
#
#
# print_info(age=70, name="Jules")
# print_info(name="Wiki")

# def print_info(arg1, *vartuple):
#     """This prints the passed arguments"""
#     print("Output is:")
#     print(arg1)
#     for var in vartuple:
#         print(var)
#     return
#
#
# """Now you can call print_info function"""
# print_info(10)
# print_info(10, 20, 30, 50)

# Using
# def add_multiples(a, b, *myvars):
#     c = a + b
#     for x in myvars:
#         c = c + x
#     return c
#
#
# print(add_multiples(7, 10, 20, 40))
# separator = ','
#
# my_vars = input("Enter your values here:")
# my_vars = [int(y) for y in my_vars.split(separator)]
#
# def add_multiples(*my_vars):
#     total = 0
#     for x in my_vars:
#         total = total + x
#     return total
#
#
# print(add_multiples(*my_vars))

# my_list = []
# for x in range(10):
#     user_input = input("Enter your numbers separated by comma:")
#     my_list.append(user_input)
# print(add_multiples(*my_list))

# RECURSION
# def factorial_sol(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial_sol(n - 1)
#
#
# print(factorial_sol(10))

# MADT RECURSION
# def open_item(mylist):
#     for item in mylist:
#         if type(item) == list:
#             open_item(item)
#         else:
#             print(item)
#
#
# items = ["dog", "ball", "tv", ["remote", "laptop", "phone"], ["cat", "pet", "dog", ["mtn", "Airtel"]], "man", ]
# open_item(items)

# OPTIMUS PRIME
# user_input = int(input("Enter your number: "))


# def optimus_prime(user_input):
#     two = user_input % 2
#     three = user_input % 3
#     five = user_input % 5
#     seven = user_input % 7
#     if two == 0 and user_input != 2 \
#             or three == 0 and user_input != 3 \
#             or five == 0 and user_input != 5 \
#             or user_input == 1 \
#             or seven == 0 and user_input != 7:
#         return "No!", user_input, "is not a prime number"
#     else:
#         return "Yes!", user_input, " is a prime number"
#
#
# print(optimus_prime(user_input))

# user_input = int(input("Enter your number: "))
# g = user_input
# # if user_input > 1:
# #     for i in range(2, user_input):
# #         if i * i != user_input:
# #             print("na prime")
# #         else:
# #             print("no be prime")
# # else:
# #     print("no be prime")
#
# if user_input > 1:
#     for i in range(2, user_input):
#         print(i * (i + 1))
# if i * i == g:
#         print("x")
# else:
#     print("prime")
#      if i * i == user_input:
#         print("h")
#     else:
#         print("jjj")
# else:
#     print("sss")

#     for x in range(2, user_input):
#         z = user_input / y
#         print(z)
# else:
#     print("where am I?")
#         if i / user_input == 1:
#             print("not")
# #             print(i, "times", user_input/i, "is", user_input)
# #             break
#         else:
#             print("is prime")
# else:
#     print("No,!", user_input, "is not a prime number")

# Memory Chopper
# user_input = int(input("Enter your number: "))
# list = []
# for i in range(2, user_input):
#     for j in range(2, user_input):
#         list.append(i*j)
# print(list)
# if user_input in list:
#     print(user_input, "is not prime")
# elif user_input == 1:
#     print("1 is not prime")
# else:
#     print(user_input, "na prime")

# Memory Not-chopper
# user_input = int(input("Enter your number: "))
# values = []
# for x in range(2, user_input):
#     values.append(user_input % x)
# print(values)
# if 0 in values:
#     print("not a prime")
# else:
#     print("its a prime")

# if user_input / x is not float:
#     print("prime")
# else:
#     print("not prime")

# Mayowa's code
# user_input = int(input("Enter your number: "))
# a = user_input**0.5
# b = range(2, int(a + 1))
# c = [user_input % x for x in b]
# if 0 in c:
#     print("not")
# else:
#     print("yes")

# Quadratic Equation

# a = int(input("Insert a: "))
# b = int(input("Insert b: "))
# c = int(input("Insert c: "))
# common = ((b * b) - (4 * a * c)) ** 0.5
# equation = (-b + common) / 2 * a
# equation_two = (-b - common) / 2 * a
# print("The factors are", equation, "and", equation_two)

# 6th python class- FILE METHODS
# Creating and manipulating data in explorer files


# OS Module
# rename directory - os.rmdir(directory),make directory - os.mkdir("newdir")
# chdir( - change directory
# change working directory - os.getcwd()
# remove directory - os.remove(filename), os.rmdir(directory)
# rename - os.rename(current_file_name, new_file_name)
# if path exists or item is in file: - if os.path.exists("demofile.txt")/ if os.path.isfile(f):

#
# dirName = "/home/kuforiji/Desktop/Univel_City"
#
#
# def directory_access(folderDirectory):
#     folder = open(folderDirectory, 'r')
#     for fileItems in folder:
#         f = os.path.join(folder, fileItems)
#         f = os.path.isfile(f)
#         if os.path.isfile(f):
#             print(fileItems)
#         else:
#             directory_access(fileItems)
#
#
# directory_access(dirName)

# Printing the path, subdirs and file names in a folder

# dirName = "/home/kuforiji/Desktop/Univel_City"
#
#
# def directory_access(folder_directory):
#     for path, sub_dirs, files in os.walk(folder_directory):
#         for fileItems in files:
#             print(fileItems)
#
#
# directory_access(dirName)

# text_file = open("/home/kuforiji/Desktop/PYTHON/write_it.txt", "w")
# text_file.write("\nLine 1\n")
# text_file.write("This is Line 2\n")
# text_file.write("That makes this Line 3\n")
# lines = ["List_line 1\n"
#          "This is List_line 2\n"
#          "That makes this List_Line 3\n"
#          ]
# text_file.writelines(lines)
# text_file.close()
#
# text_file = open("/home/kuforiji/Desktop/PYTHON/write_it.txt", 'r')
# # text_file.__next__()
# # print(text_file.readline())
# print(text_file.read())
#
# text_file.close()

# TRY AND EXCEPT MESSAGES

# a = 'Ten'
# try:
#     b = int(a)
#     print("no error\t", b)
# except:
#     print("error handled\t", a)

# def addnum(a, b):
#     try:
#         print(a + b)
#     except:
#         print("error!", a, "is type", type(a), b, "is type", type(b))
#
#
# addnum('ten', 5)


# DATABASE MANAGEMENT

# 6th python class

# object oriented programming- instantiating, instance variables and method overriding

# class Animal:
#     def talk(self):
#         print("I have something to say")
#
#     def walk(self):
#         print("Hey I can walk")
#
#     def clothes(self):
#         print("I have clothes")
#
#
# class Dog(Animal):
#     def clothes(self):
#         print("I have a brown and white fur")
#
#
# class Duck(Animal):
#     def __init__(self, color="white"):
#         self.color = color
#
#     def quack(self):
#         print("Quaccccccck")
#
#     def walk(self):
#         print("Walks like a duck")
#
#     def get_color(self):
#         return self.color
#
#     def set_color(self, color):
#         self.color = color
#
#
# # myDuck = Duck('grey')
# # myDuck.quack()
# # myDuck.get_color()
# # myDuck.clothes()
# # print(myDuck.get_color())
# #
# # mydog = Dog()
# # mydog.clothes()
#
# def main():
#     donald = Duck()
#     print(donald.get_color())
#     donald.set_color("blue")
#     print(donald.get_color())
#     donald.walk()
#     donald.clothes()
#     fido = Dog()
#     fido.walk()
#     fido.clothes()
#
#
# # if __name__ == "__main__": main()  # OR main()
#
# class stringer:
#     def __init__(self, mystring='yellow'):
#         self.mystring = mystring
#
#     def string_len(self):
#         print(len(self.mystring))
#
#     def str_reverse(self):
#         new_string = ''
#         for x in range(1, len(self.mystring) + 1):
#             new_string = new_string + self.mystring[-x]
#         print(new_string)
#
#
# mystr = stringer('mayowa')
# mystr.string_len()
# mystr.str_reverse()

# count the length of a string without using len function
# OOP- the whole point is using multiple functions in a class and calling the class on an object

# class LenCounter:
#     def __init__(self, my_len=''):
#         self.my_len = my_len
#
#     def get_len(self):
#         y = 0
#         user_input = input("Input a string: ")
#         for i in user_input:
#             y = y + 1
#         print(y)
#
#
# test_len = LenCounter()
# test_len.get_len()

# a = user_input[:]
# print(a)
#
# import sqlite3
# import _sqlite3
# #
# # # INSERT INTO DATABASE
# # # connect to database
# db = sqlite3.connect("localhost","root", "root", "python_class")
# # prepare cursor object using cursor()method
# cursor = db.cursor()
# # prep SQL query to INSERT a record into the database
# sql = "INSERT INTO students(name,price, style, stock, description) VALUES('Coke2', 1500, 11, 700, 'descrip2')"
# try:
#     # Execute the SQL command
#     cursor.execute(sql)
#     # Commit changes to database
#     db.commit()
# except:
#     # Rollback incase there is an error
#     db.rollback()
#
# # disconnect from server
# db.close()

# def welcome_menu():
#     # Display these on startup
#     """
#     It's a bright and sunny day!!!\n
#     Welcome to Kufco Stores\n
#     How may we be of assistance to you?
#     """
#
# a = input("test: ")
# if a == "1":
#     welcome_menu()
# else:
#     print("nada")

# print(tabulate([['Alice', 24], ['Bob', 19],], headers=['Names of participants', 'Ages of participants']))

# from prettytable import PrettyTable
# t = PrettyTable(['Name', 'Age'])
# t.add_row(['Alice', 24])
#
# t.add_row(['Bob', 19])
# print(t)

# while b > 5:
#     a.update(c)


import pymysql


def item_validation():
    # Connecting to the database
    db = pymysql.connect("localhost", "root", "root", "python_class")
    # Prepare cursor object using cursor()method
    cursor = db.cursor()
    # prep SQL query to Read a record from the database
    y = str(input("Enter name here: "))
    # CAll VALIDATION FUNCTION HERE TO BE SURE Y IS A VALID ITEM
    x = input(str("enter qty here: "))
    # z = {y: x}
    # a = z.keys()
    # b = []
    # for i in a:
    #     b.append(a)
    # print(b)
    # query = "SELECT name FROM kufco where name = 'coke'"
    # query = "SELECT * FROM kufco WHERE name LIKE '%coke%'"
    query = "SELECT * FROM kufco WHERE category = 'drinks'"
    cursor.execute(query)
    for name in cursor:
        print('{}'.format(name))

    # query = "SELECT * FROM kufco WHERE name = " + a
    # # Execute SQL command
    # cursor.execute(query)
    # # this makes a list of all the names of the items present in the inventory
    # items = []
    # for name in cursor:
    #     items.append(name)
    # print(items)
    # # print('{}'.format(name))
    # # query = "SELECT * FROM kufco WHERE name = coke "
    # # cursor.execute(query)
    # # print(cursor)
    #
    # # disconnect from server
    # db.close()


def qty_validation():
    # Connecting to the database
    db = pymysql.connect("localhost", "root", "root", "python_class")
    # Prepare cursor object using cursor()method
    cursor = db.cursor()
    # prep SQL query to Read a record from the database
    query = "SELECT * FROM kufco"
    # Execute SQL command
    cursor.execute(query)

    # fetch the name of item to be purchased and its price
    # for name in cursor:
    #     items.append(name[1])
    # print(items)
    # (Selectors: <, >, !=; combine multiple selectors with AND, OR)

    # items = []
    # items2 = []
    # y = ()
    # for name in cursor:
    #     items.append(name[1])
    #     items2.append(name[4])

    # roww = cursor.fetchall()
    # # for i in roww:
    # #     print(i)
    #
    #
    # for x in roww:
    #     print(x["category"])

    # print(y)
    # print(items)
    # print(items2)
    # k = list(zip(items, items2))

    # print(dict(zip([1, 2, 3, 4], ['a', 'b', 'c', 'c'])))

    # print(dict(zip([items], [items2])))

    # These are the items the user wants to buy from the inventory
    # a = {"coke": "150", "apple": "200", "baked_beans": "200", "cards": "800", "doughnut": "80"}
    # test_1 = input("enter item: ")
    # test_2 = input("enter qty: ")
    # test_3 = {test_1: test_2}
    # # print(int((test_3.get(test_1))))
    # if int(test_3.get(test_1)) > int(a.get(test_1)):
    #     print("We have only " + a.get(test_1) + " in stock")


item_validation()
