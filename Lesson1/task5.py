def funcA():
    print("Начали делать A")
    funcB()
    print("Закончили делать A")

def funcB():
    print("Начали делать B")
    funcC()
    print("Закончили делать B")

def funcC():
    print("Начали делать C")
    funcD()
    print("Закончили делать C")

def funcD():
    print("Начали делать D")
    print("Закончили делать D")

print("Начали программу")
funcA()
print("Закончили программу")