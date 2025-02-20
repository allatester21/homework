# Задачка с собеседования:
# Напишите функцию fizz_buzz, которая принимает один аргумент — n (число).
# Функция должна печатать числа от 1 до n. При этом:
# если число делится на 3, печатать Fizz;
# если число делится на 5, печатать Buzz;
# если число делится на 3 и на 5, печатать FizzBuzz.


def fizz_buzz(n):
    for x in range(1, n):
        if (x % 3 == 0):
            print("Fizz")
        elif (x % 5 == 0):
            print("Buzz")
        elif (x % 3 == 0) and (n % 5 == 0):
            print("FizzBuzz")
        else:
            print(x)

sq_num = int(input("Введите число: "))
sq = fizz_buzz(sq_num)
