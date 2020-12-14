time = int(input("Введите время в секундах: "))

print(f'{time // 360:02d}:{time % 360 // 60:02d}:{time % 60:02d}')
