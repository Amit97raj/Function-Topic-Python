# Python Basics Chapter 4:
# ========================

# n 1. Functions Intro

# a, b are parameters
# 2, 4 are arguments

# def add_two(a, b):
#     return a + b

# total = add_two(2, 4)
# print(total)

# print(add_two(2, 4))

# print(add_two(2, 4))

# num1 = int(input("First number : "))
# num2 = int(input("Second number : "))

# str1 = input("First String : ")
# str2 = input("Second String : ")


# print(add_two(num1  num2))
 # print(add_two(str1, str2))

# 2. Print Vs Return

# # return 
# def add_three(a, b, c):
    # return a + b + c

# print(add_three(2, 4, 6))

# def add_five(a,b,c,d,e):
#     return (a+b+c+d+e)
# print(add_five(2,5,6,8,12))


# def add_three(a, b, c):
    # print(a + b + c)

# add_three(2, 4, 6)

# def add_six(a, b, c, d, e, f):
#     print(a+b+c+d+e+f)
# add_six(2,4,5,6,7,8  )

# 3. Function Practice
 
# def last_char(s):
#     return s[-1]

# print(last_char("Anshul"))

# name = input("Name : ")

# print(last_char(name))
# def last_char(s):
#     return s[-1]
# name = input("name :")
# print(last_char("Deepak shrivastva"))

# def odd_even(n):
#     if n % 2 == 0:
#         return "even"
#     else:
#         return "odd"
# def odd_even(n):
# if n % 2 == 0:
#     return "even"
# else:
#     return"odd"

# print(odd_even(3))

# num = int(input("Number : "))
# print(odd_even(num))

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     return False

# def is_even(n):
#     return n % 2 == 0

# print(is_even(2))

# def is_even(n):
#     if n % 2 == 0:
#         print(is_even(2))

# num = int(input("Number : "))
# print(is_even(num))

# def hello_world():
#     return "hello world"

# print(hello_world())

# 4. Exercise - 1

# Define a function which takes two numbers as a input and return
# greater of two numbers.

# 5. Exercise - 1 Solution

# def greater(a, b):
#     if a > b:
#         return a
#     else:
#         return b

# def greater(a, b):
#     if a > b:
#         return a
#     return b

# num1, num2 = input("Two numbers separated by space : ").split()
# print(f"{greater(int(num1), int(num2))} is greater")

# 6. Define Greatest

# def greatest(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c

# def greatest(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     return c

# num1, num2, num3 = input("Three numbers separated by space : ").split()
# print(greatest(int(num1), int(num2), int(num3)))

# 7. Function Inside Function

# def greater(a, b):
#     if a > b:
#         return a
#     return b

# # def greatest(a, b, c):
# #     bigger = greater(a, b)

# #     return greater(bigger, c)

# def greatest(a, b, c):
#     return greater(greater(a, b), c)

# num1, num2, num3 = input("Three numbers separated by space : ").split()
# print(greatest(int(num1), int(num2), int(num3)))

# Programming Principle -

# kiss -> keep it simple stupid

# 8. Exercise - 2

# Define is_palindrome function that take one word in string as input
# and return True if it is palindrome else return False

# palindrome - word that reads same backwards as forwards

# example - 
# madam, naman

# logic -
# step-1: reverse the string
# step-2: compare reversed string with original string 

# 9. Exercise - 2 Solution

# def is_palindrome(s):
#     if s == s[::-1]:
#         return True
#     else:
#         return False

# def is_palindrome(s):
#     if s == s[::-1]:
#         return True
#     return False

# def is_palindrome(s):
#     return s == s[::-1]

# string = input("String : ")

# print(is_palindrome(string))

# 10. Fibonacci Series

# fibonacci series
# 0 1 1 2 3 5 8 13 21 34

# for i in range(1, 11):
#     print(i)


# for i in range(1, 11):
    # print(i, end=" ")
# for i in range(1, 50):
#     print(i, end = " ")

# 1
# def fibonacci(n):
#     a = 0 # first number
#     b = 1 # second number

#     if n == 1:
#         print(a) # 0
    
#     elif n == 2:
#         print(a, b) # 0 1
    
#     else:

#         print(a, b, end=" ") # 0 1

#         for i in range(n - 2):
#             c = a + b # c = 0 + 1 = 1
#             a = b # a = 1
#             b = c # b = 1

#             print(b, end=" ") # 1

# fibonacci(10)

# num = int(input("Number : "))
# fibonacci(num)

# 11. Default Parameters

# def user_info(first_name, last_name, age):
#     print(f"Your first name is {first_name}")
#     print(f"Your last name is {last_name}")
#     print(f"Your age is {age}")

# user_info("Anshul", "Garg", 22)

# first, last, age = input("Your first and last name with age separated by space : ").split()

# user_info(first, last, int(age))

# def user_info(first_name, last_name, age=22):
#     print(f"Your first name is {first_name}")
#     print(f"Your last name is {last_name}")
#     print(f"Your age is {age}")

def user_info(first_name, last_name, age=None):
    print(f"Your first name is {first_name}")
    print(f"Your last name is {last_name}")
    print(f"Your age is {age}")

# def user_info(first_name, last_name='unknown', age=None):
#     print(f"Your first name is {first_name}")
#     print(f"Your last name is {last_name}")
#     print(f"Your age is {age}")

# def user_info(first_name='unknown', last_name='unknown', age=None):
#     print(f"Your first name is {first_name}")
#     print(f"Your last name is {last_name}")
#     print(f"Your age is {age}")

# user_info("Anshul", "Garg")
# user_info("Anshul", "Garg", 24)
# user_info()

#first, last = input("Your first and last name separated by space : ").split()

#user_info(first, last)

# first, last, age = input("Your first and last name with age separated by space : ").split()

# user_info(first, last, int(age))

# 12. Variable Scope

# A variable defined in a function is called as a local variable.

# global variable

# x = 5

# def func1():
#     x = 7
#     return x

# def func1():
#     global x
#     x = 7
#     return x

# def func2():
#     print(x)

# print(x)

# print(func1())
# print(x)

# print(x)
# print(func1())

# func2()
