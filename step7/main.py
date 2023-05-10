from random import randint
from writers import *
from defic import *


name = input("Введите имя игрока: ")
print("\nДобро пожаловать в главное меню!")


while True:


    menu()

    us_answer = input("Сделайте выбор: ").upper()


    if us_answer == "1":
        roll_dice(6)
    elif us_answer == "2":
        roll_dice(12)

    elif us_answer == "3":
        dice_count()
        
    elif us_answer == "4" or us_answer == "АВТОРЫ":
        print()
        for i in writers:
            print(i)

    elif us_answer == "5":
        facet = input("Выберите кубиук: 6 или 12 граней? ")
        if facet != "6" or facet != "12":
            while facet != "6" or facet != "12":
                facet = input("Выберите кубиук из предложенных: 6 или 12 граней? ")
                if facet == "6" or facet == "12":
                    break
        
        print(f"\nХод игрока,{name}")
        roll_dice(6)
        print(f"\nХод игрока, Заяц")
        roll_dice(6)
        print(f"\nХод игрока, Волк")
        roll_dice(6)
        

        
    else:
        break

    print()


    

print("Программа завершена") 