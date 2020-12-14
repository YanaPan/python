num = int(input("Введите целое положительное число: "))
imax = 0

while num > 0:
    if imax >= num % 10:
        num = num // 10
    else:
        imax = num % 10
print(imax)
