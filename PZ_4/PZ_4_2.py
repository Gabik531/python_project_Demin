#Вариант 11 Данно целое число N (> 1). Найти наименьшее целое число K, при которм выполняется неравенство 3^K > N.

def input_int_greater_than_one(promt):
    while True:
        try:
            value = int(input(promt))
        except ValueError:
            print("Неправельно ввели! Нужно целое число.")
            continue
        if value <= 1:
            print("Число должно быть больше 1!")
            continue
        return value

def main():
    n = input_int_greater_than_one(" Введите N (N > 1): ")

    k = 0
    power = 1
    while power <= n:
        power *= 3
        k += 1

    print(f"K = {k} (3^{k} = {power} > {n})")
if __name__ == "__main__":
    main()
