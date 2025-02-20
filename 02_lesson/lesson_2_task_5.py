# Напишите функцию
# month_to_season(), которая принимает один аргумент — номер месяца — и
# возвращает название сезона, к которому относится этот месяц.
# Например, передаем 2, на выходе получаем «Зима».

def month_to_season(num):
    winter = [12, 1, 2]
    spring = [3, 4, 5]
    summer = [6, 7, 8]
    autumn = [9, 10, 11]
    if num in winter:
        return "Зима"
    elif num in spring:
        return "Весна"
    elif num in summer:
        return "Лето"
    elif num in autumn:
        return "Осень"
    else:
        return "Нет такого месяца в году"

num  = int(input("Введите число от 1 до 12: "))
season = month_to_season(num)
print(season)