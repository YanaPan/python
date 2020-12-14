a = int(input("введите расстояние пробежки в первый день: "))
b = int(input("введите целевое: "))
day = 1

while b > a:
    a *= 1.1
    day += 1
print(day)
