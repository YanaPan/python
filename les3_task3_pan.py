# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
# возвращает сумму наибольших двух аргументов.

def my_fun(n_1, n_2, n_3):
    list_1 = sorted([n_1, n_2, n_3])
    list_2 = list_1[1:]
    return sum(list_2)


print(my_fun(float(input("n_1: ")), float(input("n_2: ")), float(input("n_3: "))))
