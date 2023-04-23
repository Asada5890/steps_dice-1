# Шаг 1 - Бросок кубика

Необходимо реализовать программу, которая позволит пользователю "бросить кубик". Будем использовать функцию `randint` из стандартной библиотеки Python. Она не является встроенной, её необходимо импортировать из модуля `random`.

Пример 1
> Вы бросили кубик, выпало число 5  

Пример 2  
> Вы бросили кубик, выпало число 3

```python
from random import randint

number = randint(1, 6)

print("Вы бросили кубик, выпало число", number)
```
## Задание 

Напишите аналогичную программу, используйте для вывода f-строку, придумайте собственный текст. Измените количество граней (к примеру, бросок 12-гранной кости - додекаэдра)