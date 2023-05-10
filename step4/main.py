from random import randint

while True:
    print("Добро пожаловать в главное меню!")

    writers = ["Толстой Лев",
            "Пушкин Александр",
            "Есенин Сергей"]


    print(
"""МЕНЮ
1 Бросить кубик
2 Бросить несколько кубиков
3 Авторы
4 Выйти"""
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

    else:
        break
    
    print()

print("Программа завершена") 