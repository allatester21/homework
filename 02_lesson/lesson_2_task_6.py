# Дан список
# lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20].
# Необходимо вывести элементы, которые одновременно:
# - меньше 30,
# - делятся на 3 без остатка.

lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

for x in lst:
    if (x < 30 ) and (x % 3 == 0):
        print(x)
