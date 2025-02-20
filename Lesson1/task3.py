def sumNumbers(a, b):  # объявление функции
    print(a)
    print(b)
    sum = a+b

sumNumbers(5, 6) # вызов функции

def sum_numbers(): # объявление функции
    print("Меня вызвал 1")
#    print("Меня вызвал 2")
#    print("Меня вызвал 3")
#    print("Меня вызвал 4")
#    print("Меня вызвал 5")

sum_numbers()
print("Меня вызвал Х")

def greet(name):
    print("Привет, " + name)

greet("Алекс")
greet("Mark")

def sum_numbers1(num_1, num_2):
    print("Слагаемое 1 =", num_1)
    print("Слагаемое 2 =", num_2)
    print("Сумма =", num_1+num_2)

sum_numbers1(2, 5)
sum_numbers1(10, 0)
sum_numbers1(1, 7)

def sum_numbers1(num_1, num_2):
    print("Слагаемое 1 =", num_1)
    print("Слагаемое 2 =", num_2)
    result = num_1+num_2
    print("Сумма =", result)
    return result

x = sum_numbers1(2, 5)
print(x)

def multiply(x,y):
    return x*y

m = multiply(3, 4)
print(m)

def div(x,y):
    return x/y

d = div(30, 5)
print(d)

def sub(x,y):
    return x-y

b = sub(12, 7)
print(b)