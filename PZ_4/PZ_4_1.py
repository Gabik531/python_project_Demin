#Вариант 11 Данно целое число N (>0).Найти произведение 1.1*1.2*1.3...(N сомножителей).

def input_positive_int(promt):
    while True:
        try:
            value = int(input(promt))
        except ValueError:
            print("Неправельно ввели! Нужно целое число.")
            continue
        if value <= 0:
            print("Число должно быть больше 0!")
            continue
        return value

def main():
    n = input_positive_int("Введите N (N > 0):")

    product = 1.0
    for i in range(1, n + 1):
        factor = 1 + i / 10
        product *= factor
    print("Произведение:", product)
if __name__ == "__main__":
    main()