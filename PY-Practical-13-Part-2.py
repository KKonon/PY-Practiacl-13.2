#Пользователь вводит число n. Нужно, вывести все простые числа до n.
chislo = input("Введите число: ")

for i in range(0, int(chislo)):
    if i > 1:
        if i % 1 == 0 and i % i == 0:
            if i == 2 or i == 3 or i == 5 or i == 7:
                print(i)
            if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                continue
        print(i)