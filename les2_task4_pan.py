message = input("введите сообщение: ")
my_list = message.split()

for n, i in enumerate(my_list, 1):
    print(n, i[:10])
