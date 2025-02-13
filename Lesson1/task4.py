globalVar = 1

def printGlobal():
    print(globalVar)


def printLocal():
    local = 2
    print(globalVar)
    print(local)

printGlobal()
printLocal()

print(globalVar)