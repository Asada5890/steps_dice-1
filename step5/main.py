from random import randint
from writers import writers

name = input("Введите имя игрока: ")

while True:
    print("Добро пожаловать в главное меню!")


    print(
"""МЕНЮ
1 Бросить кубик
2 Бросить несколько кубиков
3 Авторы
4 Сыграть с компьютером
5 Выйти"""
    )

    us_answer = input("Сделайте выбор: ").upper()


    if us_answer == "1":
        number = randint(1, 6)
        print(f"Происходит бросок кубика... Выпало число {number}!")
    elif us_answer == "2":
        us_num = int(input("Введите сколько кубиков хотите бросить: "))
        for i in range(us_num):
            number = randint(1, 6)
            print(f"Происходит бросок кубика... Выпало число {number}!")

    elif us_answer == "3" or us_answer == "АВТОРЫ":
        print()
        for i in writers:
            print(i)

    elif us_answer == "4":
        number = randint(1, 6)

        print(f"\nХод игрока,{name}")
        print(f"Происходит бросок кубика... Выпало число {number}!")
        number = randint(1, 6)
        print(f"\nХод игрока, Заяц")
        print(f"Происходит бросок кубика... Выпало число {number}!")
        number = randint(1, 6)
        print(f"\nХод игрока, Волк")
        print(f"Происходит бросок кубика... Выпало число {number}!")
        

        
    else:
        break

    print()


    

print("Программа завершена") 