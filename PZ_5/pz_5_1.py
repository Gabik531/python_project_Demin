# Составить функцию, которая напечатает сорок любых символов.

def print_forty_symbols(symbol):
    count = 0
    while count < 40:
        print(symbol, end="")
        count = count + 1
    print()

user_symbol = input("Введите один символ: ")
while len(user_symbol) != 1:
    print("Непрваельно ввели! Нужен ровно один символ. ")
    user_symbol = input("Введите один символ: ")

print_forty_symbols(user_symbol)
