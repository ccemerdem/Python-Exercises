import random

def printOpen():
    global openCount
    print("(", end="")
    openCount += 1

def printClose():
    global closeCount
    print(")", end="")
    closeCount += 1

def printBrackets(length):
    # must start with open bracket
    printOpen()

    global openCount, closeCount

    for i in range(1, length):
        if openCount == length / 2:
            printClose()

        elif openCount <= closeCount:
            printOpen()

        else:
            random.choice(funcs)()
    print("\n")


# creating a list of functions
funcs = [printOpen, printClose]

# getting inputs
repetition, length = map(
    int, input("Input Repetition and Length with space seperated: ").split()
)

# blocking wrong inputs
length = max(2, (length + 1) // 2 * 2)
repetition = max(1, repetition)

for i in range(0, repetition):
    # Global variables
    openCount, closeCount = 0, 0

    printBrackets(length)
