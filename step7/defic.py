from random import randint

def roll_dice(self):
    number = randint(1, self)
    print(f"Происходит бросок кубика... Выпало число {number}!\n")

def menu():
        print(
"""\nМЕНЮ\n
1 Бросить кубик(6 граней)
2 Бросить кубик(12 граней)
3 Бросить несколько кубиков
4 Авторы
5 Сыграть с компьютером
6 Выйти"""
    )
        print()

def dice_count():
    facet = input("Выберите кубиук: 6 или 12 граней? ")
    if facet != "6" or facet != "12":
        while facet != "6" or facet != "12":
            facet = input("Выберите кубиук из предложенных: 6 или 12 граней? ")
            if facet == "6" or facet == "12":
                break
    if facet == "6":
            us_num = int(input("Введите сколько кубиков хотите бросить: "))
            for i in range(us_num):
                print()
                roll_dice(6)
    else:
        us_num = int(input("Введите сколько кубиков хотите бросить: "))
        for i in range(us_num):
            print()
            roll_dice(12)
