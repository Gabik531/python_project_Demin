#Вариант 11 Данно целое  число N (>0).Найти произведение 1.1*1.2*1.3...(N сомножителей). 
while True:
    try:
        n = int(input("Введите целое число N (N > 0): "))
        if n >0:
            break 
        print("Число должно быть больше 0!")
    except ValueError:
        print("Неправельно ввели!")
        
product = 1.0
i = 1 

while i <= n:
    product = product * 1 + i / 10 
    i = i + 1 
print("Произвидение:", product)