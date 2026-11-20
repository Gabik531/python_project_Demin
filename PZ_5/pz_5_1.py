# Составить функцию, которая напечатает сорок любых символов.

def print_forty_symbols(symbol):
    count = 0
    while count < 40:
        print(symbol, end="")
        count = count + 1
    print()

u = input("Введите один символ: ")
while len(u) != 1:
    print("Непрваельно ввели! Нужен ровно один символ. ")
    u = input("Введите один символ: ")

print_forty_symbols(u)
