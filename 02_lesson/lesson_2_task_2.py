# Високосный год

def is_year_leap(num):
    return "True" if num % 4 == 0 else "False"

num = int(input("Введите год: "))

result = is_year_leap(num)
print(f"Год {num} - {result}")