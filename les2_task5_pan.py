my_list = [7, 5, 5, 3, 1]
new_score = float(input("введите ваши оценку от 0 до 9: "))
index = 0

for i in my_list:
    if new_score <= i:
        index += 1
my_list.insert(index, new_score)

print(my_list)
