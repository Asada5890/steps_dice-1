# Шаг 7 - Параметры функции

Необходимо добавить возможность бросать кости разных типов (с 6-ю и 12-ю гранями)

Пример 

> МЕНЮ  
> 1 Бросить кубик (6 граней)  
> 2 Бросить кость (12 граней)  
> 3 Бросить 3 кубика  
> 4 Сыграть с компьютером   
> 5 Выйти  
> Сделайте выбор: **3**

_После ввода числа_ `1`:

> Происходит бросок кости ... Выпало число 3 из 6!  

_Далее вновь отображается меню_

_После ввода числа_ `2`:  

> Происходит бросок кости ... Выпало число 10 из 12!     

Пункты "Сыграть с компьютером" и "Бросить 3 кубика" пока остаются неизменными 

---

В реализованной на предыдущем шаге программе тело функции `roll_dice` выполняется всегда одинаково. Это бросок кубика - кости с 6-ю гранями, при этом число 6 жестко задано (англ. hard coded), оно не может быть изменено. В текущей реализации функции `roll_dice` мы не можем использовать её для решения изложенной выше задачи. 

Внесём изменения в объявление функции `roll_dice`. Добавим **параметр** - переменную, значение которой должно быть передано в функцию при её вызове (в скобках). Это значение будет использоваться в качестве максимального при броске:

```python
# faces (англ. грани) - переменная в скобках, параметр функции
def roll_dice(faces):
    number = randint(1, faces)
    print(f"Происходит бросок кости... Выпало число {number} из {faces}!")
```

Мы также изменили текст в теле функции, к отображению текущего результата добавили вывод максимально возможного (значение `faces`)

Теперь при каждом вызове функции мы можем (и должны) передавать **аргумент** (значение параметра). 

Это позволит "бросать кости" с разным количеством граней. Рассмотрим примеры вызова нового варианта `roll_dice`: 

Пример 1   

```python 
roll_dice(6)  # Бросок кубика (может выпасть от 1 до 6)
```
_Результат выполнения:_
```
Происходит бросок кости... Выпало число 2 из 6!
```
В этом примере функция `roll_dice` _принимает_ целое число `6` в качестве аргумента (значения параметра `faces`). Так как функция `roll_dice` содержит в объявлении параметр `faces`, при её вызове мы _должны передать_ ей соответствующий аргумент  

<br>

Пример 2

```python 
roll_dice(12)  # Бросок кости (может выпасть от 1 до 12)
```
_Результат выполнения:_
```
Происходит бросок кости... Выпало число 9 из 12!
```
Функция `roll_dice` _принимает_ целое число `12` в качестве аргумента.  
или:  
В функцию `roll_dice` при её вызове передается аргумент `12` (целое число)   

Значение 12 используется в теле функции в качестве максимума при генерации случайного числа и выводится в сообщении

<br>

Пример 3

```python
roll_dice()
```
_Результат выполнения:_
```
TypeError: roll_dice() missing 1 required positional argument: 'faces'
```

Вызов функции `roll_dice` с пустыми скобками (без передачи в неё обязательного аргумента) не может быть осуществлён. Возникает ошибка:  
"пропущен 1 обязательный позиционный аргумент faces"

---

Внесём изменения в текст написанной ранее программы:

```python
from random import randint

def roll_dice(faces):  # добавлен параметр (переменная faces в скобках)
    number = randint(1, faces)  # переменная faces используется в теле функции
    print(f"Происходит бросок кости... Выпало число {number} из {faces}!")


while True:
    print(
"""МЕНЮ
1 Бросить кубик
2 Бросить кость (12 граней)
3 Бросить 3 кубика
4 Сыграть с компьютером
5 Выйти"""
    )

    option = input("Сделайте выбор: ")

    if option == "1":
        roll_dice(6)  # вызов функции roll_dice с подходящим АРГУМЕНТОМ
    elif option == "2":
        roll_dice(12)  # еще один вызов (передаём другой аргумент)
    elif option == "3":
        for i in range(3):
            roll_dice(6)
    elif option == "4":
        print("Ход пользователя:")
        roll_dice(6)  
        print("Ход компьютера:")
        roll_dice(6)    
    else:
        break
    
    print()

print("\nПрограмма завершена")
```

## Задание

Ответьте на вопросы:
* Что такое функция? 
* Каких проблем использование функций позволяет избежать?
* Как в Python объявляются функции?
* Что такое параметр функции? 
* Чем аргумент отличается от параметра?
* Приведите примеры _встроенных_ функций в Python, которые могут быть вызваны без передачи аргументов (с пустыми скобками)
* Приведите пример _встроенной_ функции в Python, которая требует при её вызове передачи одного (или более) обязательного аргумента

Внесите изменения в написанную на предыдущем шаге программу для реализации бросков различных видов костей