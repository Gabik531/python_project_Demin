while True:
    try:
        num = int(input("Введите двузначное число: "))
    except ValueError:
        print("Ошибка: введите целое число")
        continue
    if not 10 <= abs(num) <= 99:
        print("Ошибка: число должно быть двузначным")
        continue
    break
num = abs(num)
tens = num // 10
units = num % 10
print("Десятки", tens)
print("Еденицы", units)