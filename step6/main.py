from random import randint
from writers import writers
from defic import roll_dice


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
        roll_dice()
    elif us_answer == "2":
        us_num = int(input("Введите сколько кубиков хотите бросить: "))
        for i in range(us_num):
          roll_dice()

    elif us_answer == "3" or us_answer == "АВТОРЫ":
        print()
        for i in writers:
            print(i)

    elif us_answer == "4":
        print(f"\nХод игрока,{name}")
        roll_dice()
        print(f"\nХод игрока, Заяц")
        roll_dice()
        print(f"\nХод игрока, Волк")
        roll_dice()
        

        
    else:
        break

    print()


    

print("Программа завершена") 