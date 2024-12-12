#Classwork 1: Create a function that adds two numbers and returns their sum.
#Classwork 2: Create a function that takes a name and returns a greeting that says "Hello" to that
#Classwork 3: Create a function that takes a number and returns "Even" if the number is even and "Odd" if it is odd.
#Classwork 4: Create a function that takes a number and returns double that number.
#Classwork 5: Create a function that takes a word and returns how many letters it has.
#1
def numbers(a,b):
    print(a+b)
numbers(50,51)
#2
def greet(hello):
    print("hello","ravaxar?!")
greet("hello")
#3
def even_or_odd(number):
    if number % 2 == 0:
        print("even")
    else:
        print("odd")

even_or_odd(2)

even_or_odd(5)
#4
def numbers2(number1):
    print(number1 * 2)
numbers2(4)
#5
def nam1(name):
    print(len(name))
nam1("sandro")
   