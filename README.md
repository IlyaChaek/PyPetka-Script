#### Проект для работы с Python проектами. Может помочь вам в реализации простых задач, и имеет некоторые готовые решения. ####


Строчка импорта в проект (ОБЯЗАТЕЛЬНО ДЛЯ ВЫПОЛНЕНИЯ КОМАНД PyPetka Script):
```python
from pypetka_script import *
```
после чего вводите команду для функции. 

В большинстве случаев код может ничего не выдать, в таком случае есть следующая команда - вывод(print), пример:

```python
вывод(генератор_паролей())
```


Полноценный пример использования:
```python
from pypetka_script import * #подключение PyPetka Script
вывод(генератор_паролей()) #функция + аргументы внутри скобок
```
#### Важно! ####
Большая часть команд имеет аргумент внутри скобок, внизу вы можете увидеть, что нужно указать


**Команды PyPetka Script:**

## Математические функции

1. **сумма(*числа)**: Возвращает сумму переданных чисел.
2. **вычесть(*числа)**: Возвращает разность, вычитая все переданные числа из нуля.
3. **деление(число1, число2)**: Возвращает результат деления двух чисел. Если деление на ноль, выводит ошибку.
4. **умножение(число1, число2)**: Возвращает произведение двух чисел.
5. **факториал(число)**: Возвращает факториал числа. Если число отрицательное, выводит ошибку.
6. **квадратный_корень(число)**: Возвращает квадратный корень числа. Если число отрицательное, выводит ошибку.
7. **возвести_в_степень(основание, степень)**: Возвращает основание, возведенное в заданную степень.

## Функции ввода/вывода

1. **вывод(*аргументы, sep=' ', end='\n', file=sys.stdout, flush=False)**: Выводит аргументы на экран или в файл.
2. **вывод_без_переноса(*аргументы, sep=' ')**: Выводит аргументы без переноса строки.
3. **вывод_на_экран(*аргументы, sep=' ', end='\n')**: Выводит аргументы на экран.
4. **вывод_в_файл(*аргументы, sep=' ', end='\n', file=sys.stdout)**: Выводит аргументы в файл.
5. **вывод_с_переносом_строки(*аргументы, sep=' ')**: Выводит аргументы с переносом строки.
6. **ввод(комментарий=None)**: Запрашивает ввод от пользователя с опциональным комментарием.
7. **привет_мир()**: Выводит приветственное сообщение.

## Преобразования

1. **обычное_число(число)**: Преобразует число в целое.
2. **строка(число)**: Преобразует число в строку.
3. **если(условие, действие_если_да, действие_если_нет=None)**: Возвращает результат в зависимости от условия.
4. **список(пользовательский_список)**: Преобразует переданный объект в список.

## Игры и циклы

1. **угадай_число()**: Игра "Угадай число".
2. **пока(условие, действие)**: Выполняет действие, пока условие истинно.

## Строковые функции

1. **перевернуть_строку(строка)**: Возвращает перевернутую строку.
2. **заменить_символы(строка, старый_символ, новый_символ)**: Заменяет старый символ на новый в строке.
3. **проверить_палиндром(строка)**: Проверяет, является ли строка палиндромом.
4. **удалить_символ(строка, символ)**: Удаляет все вхождения символа из строки.
5. **получить_подстроку(строка, начало, конец)**: Возвращает подстроку из строки.
6. **удалить_пробелы(строка)**: Удаляет все пробелы из строки.
7. **заменить_первое_вхождение(строка, старый_символ, новый_символ)**: Заменяет первое вхождение старого символа на новый в строке.

## Списковые функции

1. **сортировка(список)**: Сортирует переданный список.
2. **уникальные_значения(список)**: Возвращает уникальные значения из списка.
3. **объединить_списки(список1, список2)**: Объединяет два списка.
4. **найти_максимум(список)**: Возвращает максимальное значение из списка.
5. **найти_минимум(список)**: Возвращает минимальное значение из списка.
6. **среднее_значение(список)**: Возвращает среднее значение чисел в списке.
7. **фильтрация(список, условие)**: Возвращает элементы списка, которые соответствуют условию.
8. **замена_в_списке(список, старый_элемент, новый_элемент)**: Заменяет старый элемент на новый в списке.
9. **подсчет_элементов(список)**: Возвращает количество элементов в списке.
10. **объединение_слов(список_слов, разделитель=' ')**: Объединяет слова в строку с заданным разделителем.
11. **разделение_строки(строка, разделитель=' ')**: Разделяет строку на слова по заданному разделителю.
12. **проверка_вхождения(элемент, список)**: Проверяет, содержится ли элемент в списке.
13. **найти_индекс(список, элемент)**: Возвращает индекс элемента в списке, если он существует.
14. **найти_дубликаты(список)**: Возвращает список дубликатов из переданного списка.
15. **объединить_и_отсортировать(список1, список2)**: Объединяет два списка и сортирует результат.
16. **проверка_пустоты(список)**: Проверяет, является ли список пустым.
17. **получить_первый_элемент(список)**: Возвращает первый элемент списка, если он существует.
18. **получить_последний_элемент(список)**: Возвращает последний элемент списка, если он существует.

## Словарные функции

1. **создать_словарь(ключи, значения)**: Создает словарь из списков ключей и значений.
2. **получить_значение_из_словаря(словарь, ключ, значение_по_умолчанию=None)**: Возвращает значение по ключу из словаря, или значение по умолчанию.
3. **удалить_ключ(словарь, ключ)**: Удаляет ключ из словаря, если он существует.
4. **объединить_словари(словарь1, словарь2)**: Объединяет два словаря.
5. **сортировка_словаря(словарь, по_возрастанию=True)**: Сортирует словарь по ключам.
6. **получить_ключи(словарь)**: Возвращает список ключей из словаря.
7. **получить_значения(словарь)**: Возвращает список значений из словаря.
8. **проверка_пустоты_словаря(словарь)**: Проверяет, является ли словарь пустым.
9. **получить_первый_ключ(словарь)**: Возвращает первый ключ из словаря, если он существует.
10. **получить_первое_значение(словарь)**: Возвращает первое значение из словаря, если он существует.
11. **получить_последний_ключ(словарь)**: Возвращает последний ключ из словаря, если он существует.
12. **получить_последнее_значение(словарь)**: Возвращает последнее значение из словаря, если он существует.

## Генерация и случайные функции

1. **генератор_чисел(начало, конец)**: Генерирует список чисел от начала до конца.
2. **случайный_элемент(список)**: Возвращает случайный элемент из списка.
3. **генератор_паролей(Длина=12)**: Генерирует случайный пароль заданной длины из латинских букв и цифр.

## Группировка и агрегация

1. **сгруппировать_по_ключу(список, ключ)**: Группирует элементы списка по заданному ключу.
2. **получить_среднее_значение_по_ключу(список, ключ)**: Возвращает среднее значение по заданному ключу.
3. **найти_максимум_по_ключу(список, ключ)**: Возвращает элемент с максимальным значением по заданному ключу.
4. **найти_минимум_по_ключу(список, ключ)**: Возвращает элемент с минимальным значением по заданному ключу.
5. **получить_различия_по_ключу(список1, список2, ключ)**: Возвращает элементы, которые есть в первом списке, но отсутствуют во втором, по заданному ключу.
6. **получить_пересечение_по_ключу(список1, список2, ключ)**: Возвращает элементы, которые есть в обоих списках, по заданному ключу.
7. **получить_объединение_по_ключу(список1, список2, ключ)**: Возвращает объединение двух списков без дубликатов по заданному ключу.
8. **найти_дубликаты_по_ключу(список, ключ)**: Возвращает список дубликатов из переданного списка по заданному ключу.
9. **получить_первый_дубликат_по_ключу(список, ключ)**: Возвращает первый дубликат из списка по заданному ключу.
10. **получить_последний_дубликат_по_ключу(список, ключ)**: Возвращает последний дубликат из списка по заданному ключу.