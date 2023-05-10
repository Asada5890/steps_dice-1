from random import randint

number = randint(1, 12)

writers = ["Толстой Лев",
           "Пушкин Александр",
           "Есенин Сергей"]

print("Добро пожаловать в главное меню!")

print("""МЕНЮ
1 Бросить кубик
2 Выйти
3 Авторы""")

us_answer = input().upper()


if us_answer == "1":
    print(f"Происходит бросок кубика... Выпало число {number}!")

elif us_answer == "3" or us_answer == "АВТОРЫ":
    for i in writers:
        print(i)

else:
    print("программа завершена")




