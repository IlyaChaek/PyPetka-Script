import math
import sys
import random
import time
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import re
import ast
import sqlite3
import socket
import hashlib
import urllib.request
import urllib.error
import statistics
import wave
import struct
import inspect
import os
import json
import base64
import itertools
import collections
from collections import defaultdict, Counter, deque
from datetime import datetime, timedelta
from itertools import combinations, permutations, product
from functools import reduce, wraps, lru_cache
from decimal import Decimal, getcontext
from fractions import Fraction
import csv
import pickle
import secrets
import string
import subprocess
import webbrowser
import mimetypes
import pathlib
import hashlib
import zipfile
import tarfile
import tempfile
import shutil
import threading
import queue
import contextlib
import traceback
import dataclasses
from typing import Any, Union, List, Dict, Tuple, Optional, Callable
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

# ==========================================
# КОНСТАНТЫ И ПЕРЕМЕННЫЕ
# ==========================================

Истина = True
Ложь = False
число_пи = math.pi
число_е = math.e
золотое_сечение = (1 + math.sqrt(5)) / 2
ускорение_свободного_падения = 9.80665  # м/с²
скорость_света = 299792458  # м/с
постоянная_планка = 6.62607015e-34  # Дж·с
число_авогадро = 6.02214076e23  # моль⁻¹

# ==========================================
# ЯДРО PYPETKA (ОСНОВНЫЕ ФУНКЦИИ)
# ==========================================

def сумма(*числа: Union[int, float]) -> Union[int, float]:
    """Возвращает сумму переданных чисел."""
    return sum(числа)

def вычесть(*числа: Union[int, float]) -> Union[int, float]:
    """Возвращает разность первого числа и суммы остальных."""
    if not числа:
        return 0
    if len(числа) == 1:
        return -числа[0]
    return числа[0] - sum(числа[1:])

def умножить(*числа: Union[int, float]) -> Union[int, float]:
    """Возвращает произведение переданных чисел."""
    result = 1
    for num in числа:
        result *= num
    return result

def делить(число1: Union[int, float], число2: Union[int, float]) -> Union[float, None]:
    """Возвращает результат деления двух чисел."""
    if число2 == 0:
        вывод('Ошибка: деление на ноль!')
        return None
    return число1 / число2

def вывод(*аргументы: Any, sep: str = ' ', end: str = '\n', file=sys.stdout, flush: bool = False) -> None:
    """Выводит аргументы на экран или в файл."""
    print(*аргументы, sep=sep, end=end, file=file, flush=flush)

def вывод_без_переноса(*аргументы: Any, sep: str = ' ') -> None:
    """Выводит аргументы без переноса строки."""
    print(*аргументы, sep=sep, end='')

def вывод_на_экран(*аргументы: Any, sep: str = ' ', end: str = '\n') -> None:
    """Выводит аргументы на экран."""
    print(*аргументы, sep=sep, end=end)

def вывод_в_файл(*аргументы: Any, sep: str = ' ', end: str = '\n', file=sys.stdout) -> None:
    """Выводит аргументы в файл."""
    print(*аргументы, sep=sep, end=end, file=file)

def вывод_с_переносом_строки(*аргументы: Any, sep: str = ' ') -> None:
    """Выводит аргументы с переносом строки."""
    print(*аргументы, sep=sep)

def ввод(комментарий: Optional[str] = None) -> str:
    """Запрашивает ввод от пользователя."""
    return input(комментарий) if комментарий else input()

def если(условие: bool, действие_если_да: Any, действие_если_нет: Optional[Any] = None) -> Any:
    """Простейший тернарный оператор."""
    return действие_если_да if условие else действие_если_нет

def пока(условие: Callable[[], bool], действие: Callable[[], None]) -> None:
    """Цикл while."""
    while условие():
        действие()

def для_каждого(коллекция: List[Any], действие: Callable[[Any], None]) -> None:
    """Цикл for для коллекции."""
    for элемент in коллекция:
        действие(элемент)

def начало_кода() -> float:
    """Отмечает время начала выполнения кода."""
    return time.perf_counter()

def конец_кода(начало: float) -> None:
    """Вычисляет и выводит время выполнения кода."""
    print(f"Время выполнения: {time.perf_counter() - начало:.6f} секунд")

def валидация_типа(объект: Any, ожидаемый_тип: type) -> bool:
    """Проверяет, соответствует ли объект ожидаемому типу."""
    return isinstance(объект, ожидаемый_тип)

def вернуть_значение(значение: Any) -> Any:
    """Возвращает переданное значение."""
    return значение

def обычное_число(число: Union[str, float]) -> int:
    """Преобразует число в целое."""
    return int(число)

def строка(объект: Any) -> str:
    """Преобразует объект в строку."""
    return str(объект)

def список(коллекция: Any) -> List[Any]:
    """Преобразует объект в список."""
    return list(коллекция)

def привет_мир() -> None:
    """Выводит приветственное сообщение."""
    вывод('Привет, мир!')

# ==========================================
# УТИЛИТЫ И ДЕКОРАТОРЫ
# ==========================================

def мемоизация(func: Callable) -> Callable:
    """Декоратор для кэширования результатов (мемоизация)."""
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

def замер_времени(func: Callable) -> Callable:
    """Декоратор для замера времени выполнения функции."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"[{func.__name__}] выполнено за: {end_time - start_time:.6f} сек")
        return result
    return wrapper

def повторить(n: int = 1):
    """Декоратор для повторного выполнения функции."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for i in range(n):
                results.append(func(*args, **kwargs))
            return results if n > 1 else results[0]
        return wrapper
    return decorator

def обработка_ошибок(func: Callable) -> Callable:
    """Декоратор для обработки ошибок."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Ошибка в функции {func.__name__}: {e}")
            return None
    return wrapper

# ==========================================
# МАТЕМАТИКА: ОСНОВНЫЕ ФУНКЦИИ
# ==========================================

@мемоизация
def факториал(n: int) -> Optional[int]:
    """Вычисляет факториал числа."""
    if n < 0:
        вывод('Ошибка: факториал отрицательного числа не определен!')
        return None
    return math.factorial(n)

def квадратный_корень(число: Union[int, float]) -> Optional[float]:
    """Возвращает квадратный корень числа."""
    if число < 0:
        вывод('Ошибка: нельзя извлечь квадратный корень из отрицательного числа!')
        return None
    return math.sqrt(число)

def возвести_в_степень(основание: Union[int, float], степень: Union[int, float]) -> Union[int, float]:
    """Возвращает основание, возведенное в заданную степень."""
    return основание ** степень

def проверка_на_четность(число: int) -> str:
    """Проверяет, является ли число четным или нечетным."""
    if число % 2 == 0:
        вывод('Число четное')
    else:
        вывод('Число нечетное')
    return "четное" if число % 2 == 0 else "нечетное"

@мемоизация
def числа_фибоначчи(n: int) -> List[int]:
    """Возвращает список из n чисел Фибоначчи."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

@мемоизация
def НОД(a: int, b: int) -> int:
    """Находит наибольший общий делитель двух чисел."""
    return math.gcd(a, b)

@мемоизация
def НОК(a: int, b: int) -> int:
    """Находит наименьшее общее кратное двух чисел."""
    return abs(a * b) // math.gcd(a, b)

def НОД_список(числа: List[int]) -> int:
    """Находит наибольший общий делитель списка чисел."""
    if not числа:
        return 0
    return reduce(math.gcd, числа)

def НОК_список(числа: List[int]) -> int:
    """Находит наименьшее общее кратное списка чисел."""
    def lcm(a: int, b: int) -> int:
        return abs(a * b) // math.gcd(a, b) if a != 0 and b != 0 else 0
    
    if not числа:
        return 0
    return reduce(lcm, числа)

def разложить_на_множители(n: int) -> List[int]:
    """Разлагает число на простые множители."""
    factors = []
    d = 2
    temp = n
    while d * d <= temp:
        while temp % d == 0:
            factors.append(d)
            temp //= d
        d += 1
    if temp > 1:
        factors.append(temp)
    return factors

def конвертировать_систему(число_str: str, из_системы: int, в_систему: int) -> str:
    """Конвертирует число из одной системы счисления в другую (2-36)."""
    try:
        dec = int(str(число_str), из_системы)
        if в_систему == 10:
            return str(dec)
        
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res = ""
        while dec > 0:
            res = digits[dec % в_систему] + res
            dec //= в_системы
        return res if res else "0"
    except ValueError:
        return "Ошибка формата числа"

def проверка_простых_чисел(число: int) -> str:
    """Проверяет, является ли число простым."""
    if число <= 1:
        return "Число не является простым"
    if число <= 3:
        return "Число является простым"
    if число % 2 == 0 or число % 3 == 0:
        return "Число не является простым"
    
    i = 5
    while i * i <= число:
        if число % i == 0 or число % (i + 2) == 0:
            return "Число не является простым"
        i += 6
    return "Число является простым"

def проверка_трехзначных_чисел_на_убывающую_последовательность(число: int) -> str:
    """Проверяет, являются ли цифры трехзначного числа убывающей последовательностью."""
    if len(str(число)) != 3:
        return "Число не трехзначное"
    digits = sorted(str(число), reverse=True)
    return "Цифры образуют убывающую последовательность" if digits == list(str(число)) else "Цифры не образуют убывающую последовательность"

# ==========================================
# МАТЕМАТИКА: УРАВНЕНИЯ И СИСТЕМЫ
# ==========================================

@мемоизация
def решить_квадратное_уравнение(a: float, b: float, c: float) -> Union[str, Tuple[float, float]]:
    """Решает квадратное уравнение ax² + bx + c = 0."""
    if a == 0:
        return "Это не квадратное уравнение"
    
    D = b**2 - 4*a*c
    
    if D < 0:
        return f"Дискриминант D={D}. Действительных корней нет"
    elif D == 0:
        x = -b / (2*a)
        return f"Дискриминант D=0. Один корень: x={x}"
    else:
        sqrt_D = math.sqrt(D)
        x1 = (-b + sqrt_D) / (2*a)
        x2 = (-b - sqrt_D) / (2*a)
        return (x1, x2)

def решить_линейное_уравнение(a: float, b: float, c: float) -> float:
    """Решает линейное уравнение ax + b = c."""
    if a == 0:
        raise ValueError("Коэффициент a не может быть равен нулю")
    return (c - b) / a

def решить_систему_линейных_уравнений(a1: float, b1: float, c1: float, 
                                     a2: float, b2: float, c2: float) -> Tuple[float, float]:
    """Решает систему линейных уравнений:
    a1*x + b1*y = c1
    a2*x + b2*y = c2"""
    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        raise ValueError("Система не имеет единственного решения")
    
    x = (c1 * b2 - c2 * b1) / determinant
    y = (a1 * c2 - a2 * c1) / determinant
    return (x, y)

def решить_кубическое_уравнение(a: float, b: float, c: float, d: float) -> List[complex]:
    """Решает кубическое уравнение ax³ + bx² + cx + d = 0."""
    if a == 0:
        return [complex(-d/c)] if c != 0 else []
    
    # Приводим к виду x³ + px + q = 0
    p = (3*a*c - b**2) / (3*a**2)
    q = (2*b**3 - 9*a*b*c + 27*a**2*d) / (27*a**3)
    
    # Формула Кардано
    discriminant = (q/2)**2 + (p/3)**3
    
    if discriminant > 0:
        u = (-q/2 + math.sqrt(discriminant))**(1/3)
        v = (-q/2 - math.sqrt(discriminant))**(1/3)
        x1 = u + v - b/(3*a)
        return [complex(x1)]
    elif discriminant == 0:
        u = (-q/2)**(1/3)
        x1 = 2*u - b/(3*a)
        x2 = -u - b/(3*a)
        return [complex(x1), complex(x2)]
    else:
        r = math.sqrt(-(p/3)**3)
        phi = math.acos(-q/(2*r))
        x1 = 2*math.sqrt(-p/3)*math.cos(phi/3) - b/(3*a)
        x2 = 2*math.sqrt(-p/3)*math.cos((phi+2*math.pi)/3) - b/(3*a)
        x3 = 2*math.sqrt(-p/3)*math.cos((phi+4*math.pi)/3) - b/(3*a)
        return [complex(x1), complex(x2), complex(x3)]

def численное_дифференцирование(f: Callable[[float], float], x: float, h: float = 1e-5) -> float:
    """Вычисляет производную функции f в точке x."""
    return (f(x + h) - f(x - h)) / (2 * h)

def численное_интегрирование(f: Callable[[float], float], a: float, b: float, n: int = 1000) -> float:
    """Вычисляет интеграл функции f от a до b методом Симпсона."""
    if n % 2 == 1:
        n += 1
    
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [f(x_i) for x_i in x]
    
    result = y[0] + y[-1]
    
    for i in range(1, n, 2):
        result += 4 * y[i]
    
    for i in range(2, n-1, 2):
        result += 2 * y[i]
    
    return result * h / 3

# ==========================================
# ЛИНЕЙНАЯ АЛГЕБРА (МАТРИЦЫ)
# ==========================================

def создать_матрицу(строки: int, столбцы: int, заполнитель: Any = 0) -> List[List[Any]]:
    """Создает матрицу заданного размера."""
    return [[заполнитель] * столбцы for _ in range(строки)]

def матричное_умножение(A: List[List[float]], B: List[List[float]]) -> Union[List[List[float]], str]:
    """Умножает две матрицы (списки списков)."""
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        return "Несовместимые размерности матриц"

    C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C

@мемоизация
def транспонировать_матрицу(A: List[List[Any]]) -> List[List[Any]]:
    """Транспонирует матрицу."""
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

@мемоизация
def определитель(matrix: List[List[float]]) -> float:
    """Рекурсивно вычисляет определитель матрицы."""
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for c in range(n):
        sub_matrix = [row[:c] + row[c+1:] for row in matrix[1:]]
        det += ((-1) ** c) * matrix[0][c] * определитель(sub_matrix)
    return det

def найти_обратную_матрицу(matrix: List[List[float]]) -> Union[List[List[float]], str]:
    """Находит обратную матрицу."""
    n = len(matrix)
    det = определитель(matrix)
    
    if det == 0:
        return "Матрица вырожденная, обратной не существует"
    
    if n == 1:
        return [[1/det]]
    
    if n == 2:
        a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
        return [[d/det, -b/det], [-c/det, a/det]]
    
    # Для матриц большего порядка используем метод алгебраических дополнений
    cofactors = []
    for r in range(n):
        cofactor_row = []
        for c in range(n):
            minor = [row[:c] + row[c+1:] for row in (matrix[:r] + matrix[r+1:])]
            cofactor_row.append(((-1)**(r+c)) * определитель(minor))
        cofactors.append(cofactor_row)
    
    cofactors = транспонировать_матрицу(cofactors)
    for r in range(n):
        for c in range(n):
            cofactors[r][c] = cofactors[r][c] / det
    
    return cofactors

def найти_собственные_значения(matrix: List[List[float]]) -> List[complex]:
    """Находит собственные значения матрицы 2x2."""
    if len(matrix) != 2 or len(matrix[0]) != 2:
        raise ValueError("Функция работает только для матриц 2x2")
    
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    
    # Характеристическое уравнение: λ² - (a+d)λ + (ad - bc) = 0
    trace = a + d
    det = a * d - b * c
    
    discriminant = trace**2 - 4*det
    
    if discriminant >= 0:
        λ1 = (trace + math.sqrt(discriminant)) / 2
        λ2 = (trace - math.sqrt(discriminant)) / 2
        return [complex(λ1), complex(λ2)]
    else:
        real_part = trace / 2
        imag_part = math.sqrt(-discriminant) / 2
        return [complex(real_part, imag_part), complex(real_part, -imag_part)]

# ==========================================
# ГЕОМЕТРИЯ
# ==========================================

@мемоизация
def площадь_треугольника_герон(a: float, b: float, c: float) -> float:
    """Площадь треугольника по формуле Герона."""
    p = (a + b + c) / 2
    val = p * (p - a) * (p - b) * (p - c)
    return math.sqrt(val) if val > 0 else 0

def расстояние_между_точками(x1: float, y1: float, x2: float, y2: float) -> float:
    """Расстояние между двумя точками (2D)."""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def расстояние_между_точками_3d(x1: float, y1: float, z1: float, 
                               x2: float, y2: float, z2: float) -> float:
    """Расстояние между двумя точками (3D)."""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

def евклидово_расстояние(вектор1: List[float], вектор2: List[float]) -> Union[float, str]:
    """Евклидово расстояние между N-мерными векторами (списками)."""
    if len(вектор1) != len(вектор2):
        return "Векторы должны быть одинаковой длины"
    sum_sq = sum((x - y)**2 for x, y in zip(вектор1, вектор2))
    return math.sqrt(sum_sq)

def объем_сферы(r: float) -> float:
    """Объем сферы радиуса r."""
    return (4/3) * math.pi * r**3

def площадь_поверхности_сферы(r: float) -> float:
    """Площадь поверхности сферы радиуса r."""
    return 4 * math.pi * r**2

def объем_цилиндра(r: float, h: float) -> float:
    """Объем цилиндра."""
    return math.pi * r**2 * h

def площадь_поверхности_цилиндра(r: float, h: float) -> float:
    """Площадь поверхности цилиндра."""
    return 2 * math.pi * r * (r + h)

def теорема_пифагора(a: float, b: float, найти: str = "c") -> float:
    """Теорема Пифагора: находит недостающую сторону прямоугольного треугольника."""
    if найти == "c":
        return math.sqrt(a**2 + b**2)
    elif найти == "a":
        return math.sqrt(b**2 - a**2) if b > a else 0
    elif найти == "b":
        return math.sqrt(a**2 - b**2) if a > b else 0
    else:
        raise ValueError("Параметр 'найти' должен быть 'a', 'b' или 'c'")

# ==========================================
# ТРИГОНОМЕТРИЯ
# ==========================================

def градусы_в_радианы(градусы: float) -> float:
    """Преобразует градусы в радианы."""
    return градусы * math.pi / 180

def радианы_в_градусы(радианы: float) -> float:
    """Преобразует радианы в градусы."""
    return радианы * 180 / math.pi

def синус(угол: float, в_градусах: bool = True) -> float:
    """Вычисляет синус угла."""
    if в_градусах:
        угол = градусы_в_радианы(угол)
    return math.sin(угол)

def косинус(угол: float, в_градусах: bool = True) -> float:
    """Вычисляет косинус угла."""
    if в_градусах:
        угол = градусы_в_радианы(угол)
    return math.cos(угол)

def тангенс(угол: float, в_градусах: bool = True) -> float:
    """Вычисляет тангенс угла."""
    if в_градусах:
        угол = градусы_в_радианы(угол)
    return math.tan(угол)

def арксинус(значение: float, в_градусах: bool = True) -> float:
    """Вычисляет арксинус."""
    результат = math.asin(max(-1, min(1, значение)))
    return радианы_в_градусы(результат) if в_градусах else результат

def арккосинус(значение: float, в_градусах: bool = True) -> float:
    """Вычисляет арккосинус."""
    результат = math.acos(max(-1, min(1, значение)))
    return радианы_в_градусы(результат) if в_градусах else результат

def арктангенс(значение: float, в_градусах: bool = True) -> float:
    """Вычисляет арктангенс."""
    результат = math.atan(значение)
    return радианы_в_градусы(результат) if в_градусах else результат

def закон_синусов(a: float, A: float, b: float = None, B: float = None, 
                  c: float = None, C: float = None) -> Dict[str, float]:
    """Решает треугольник по закону синусов."""
    результаты = {}
    
    if a and A and b and not B:
        # Найти угол B
        B = math.asin(b * math.sin(A) / a)
        результаты['B'] = B
    elif a and A and B and not b:
        # Найти сторону b
        b = a * math.sin(B) / math.sin(A)
        результаты['b'] = b
    
    return результаты

def закон_косинусов(a: float = None, b: float = None, c: float = None, 
                    A: float = None, B: float = None, C: float = None) -> Dict[str, float]:
    """Решает треугольник по закону косинусов."""
    результаты = {}
    
    if a and b and c and not A:
        # Найти угол A
        A = math.acos((b**2 + c**2 - a**2) / (2*b*c))
        результаты['A'] = A
    elif a and b and C and not c:
        # Найти сторону c
        c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(C))
        результаты['c'] = c
    
    return результаты

# ==========================================
# РАБОТА СО СТРОКАМИ И ТЕКСТОМ
# ==========================================

def является_палиндромом(text: str) -> bool:
    """Проверяет, является ли строка палиндромом (без учета регистра и пробелов)."""
    clean_text = ''.join(filter(str.isalnum, text)).lower()
    return clean_text == clean_text[::-1]

def перевернуть_строку(text: str) -> str:
    """Переворачивает строку задом наперед."""
    return text[::-1]

def частота_слов(text: str) -> Dict[str, int]:
    """Считает частоту каждого слова в тексте, возвращает словарь."""
    words = re.findall(r'\b\w+\b', text.lower())
    return dict(Counter(words))

def санитайз_строки(text: str) -> str:
    """Очищает строку, оставляя только буквы, цифры и пробелы."""
    return re.sub(r'[^a-zA-Zа-яА-Я0-9\s]', '', text)

def проверка_баланса_скобок(text: str) -> bool:
    """Проверяет, сбалансированы ли скобки ({}, [], ()) в строке."""
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in text:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack

def валидация_email(email: str) -> bool:
    """Проверяет, соответствует ли строка формату email-адреса."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

def левенштейн(s1: str, s2: str) -> int:
    """Расстояние Левенштейна (похожесть строк)."""
    if len(s1) < len(s2):
        return левенштейн(s2, s1)
    if len(s2) == 0:
        return len(s1)
    
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

def jaro_расстояние(s1: str, s2: str) -> float:
    """Расстояние Джаро между двумя строками."""
    if s1 == s2:
        return 1.0
    
    len1, len2 = len(s1), len(s2)
    max_dist = max(len1, len2) // 2 - 1
    
    matches1 = [False] * len1
    matches2 = [False] * len2
    
    matches = 0
    transpositions = 0
    
    for i in range(len1):
        start = max(0, i - max_dist)
        end = min(i + max_dist + 1, len2)
        
        for j in range(start, end):
            if not matches2[j] and s1[i] == s2[j]:
                matches1[i] = True
                matches2[j] = True
                matches += 1
                break
    
    if matches == 0:
        return 0.0
    
    k = 0
    for i in range(len1):
        if matches1[i]:
            while not matches2[k]:
                k += 1
            if s1[i] != s2[k]:
                transpositions += 1
            k += 1
    
    transpositions //= 2
    
    return (matches/len1 + matches/len2 + (matches - transpositions)/matches) / 3

def звуковой_алгоритм(text: str) -> str:
    """Приводит слово к звуковому коду (алгоритм Soundex)."""
    if not text:
        return ""
    
    text = text.upper()
    
    # Первая буква
    first_letter = text[0]
    
    # Удаление букв A, E, I, O, U, H, W, Y
    text = text[1:]
    text = re.sub(r'[AEIOUHWY]', '', text)
    
    # Замена согласных цифрами
    replacements = [
        (r'[BFPV]', '1'),
        (r'[CGJKQSXYZ]', '2'),
        (r'[DT]', '3'),
        (r'[L]', '4'),
        (r'[MN]', '5'),
        (r'[R]', '6')
    ]
    
    for pattern, replacement in replacements:
        text = re.sub(pattern, replacement, text)
    
    # Удаление дубликатов
    text = re.sub(r'(\d)\1+', r'\1', text)
    
    # Сохранение первой буквы и добавление нулей
    result = first_letter + text
    result = result[:4].ljust(4, '0')
    
    return result

# ==========================================
# ШИФРОВАНИЕ И КРИПТОГРАФИЯ
# ==========================================

def шифр_цезаря(text: str, сдвиг: int, режим: str = 'шифрование') -> str:
    """Шифр Цезаря с поддержкой русского и английского алфавитов."""
    if режим == 'дешифрование':
        сдвиг = -сдвиг
    
    result = []
    
    for char in text:
        if 'а' <= char <= 'я':
            base = ord('а')
            size = 32
        elif 'А' <= char <= 'Я':
            base = ord('А')
            size = 32
        elif 'a' <= char <= 'z':
            base = ord('a')
            size = 26
        elif 'A' <= char <= 'Z':
            base = ord('A')
            size = 26
        else:
            result.append(char)
            continue
        
        pos = ord(char) - base
        new_pos = (pos + сдвиг) % size
        result.append(chr(base + new_pos))
    
    return ''.join(result)

def шифр_виженера(text: str, ключ: str, режим: str = 'шифрование') -> str:
    """Шифр Виженера с поддержкой русского и английского алфавитов."""
    ключ = ключ.lower()
    result = []
    ключ_индекс = 0
    
    for char in text:
        if 'а' <= char <= 'я':
            base = ord('а')
            size = 32
            ключ_символ = ключ[ключ_индекс % len(ключ)]
            сдвиг = ord(ключ_символ) - ord('а')
            if режим == 'дешифрование':
                сдвиг = -сдвиг
            
            pos = ord(char) - base
            new_pos = (pos + сдвиг) % size
            result.append(chr(base + new_pos))
            ключ_индекс += 1
            
        elif 'А' <= char <= 'Я':
            base = ord('А')
            size = 32
            ключ_символ = ключ[ключ_индекс % len(ключ)]
            сдвиг = ord(ключ_символ.lower()) - ord('а')
            if режим == 'дешифрование':
                сдвиг = -сдвиг
            
            pos = ord(char) - base
            new_pos = (pos + сдвиг) % size
            result.append(chr(base + new_pos))
            ключ_индекс += 1
            
        elif 'a' <= char <= 'z':
            base = ord('a')
            size = 26
            ключ_символ = ключ[ключ_индекс % len(ключ)]
            сдвиг = ord(ключ_символ) - ord('a')
            if режим == 'дешифрование':
                сдвиг = -сдвиг
            
            pos = ord(char) - base
            new_pos = (pos + сдвиг) % size
            result.append(chr(base + new_pos))
            ключ_индекс += 1
            
        elif 'A' <= char <= 'Z':
            base = ord('A')
            size = 26
            ключ_символ = ключ[ключ_индекс % len(ключ)]
            сдвиг = ord(ключ_символ.lower()) - ord('a')
            if режим == 'дешифрование':
                сдвиг = -сдвиг
            
            pos = ord(char) - base
            new_pos = (pos + сдвиг) % size
            result.append(chr(base + new_pos))
            ключ_индекс += 1
            
        else:
            result.append(char)
    
    return ''.join(result)

def шифр_атбаш(text: str) -> str:
    """Шифр Атбаш (зеркальный шифр)."""
    result = []
    
    for char in text:
        if 'а' <= char <= 'я':
            pos = ord(char) - ord('а')
            new_pos = 31 - pos
            result.append(chr(ord('а') + new_pos))
        elif 'А' <= char <= 'Я':
            pos = ord(char) - ord('А')
            new_pos = 31 - pos
            result.append(chr(ord('А') + new_pos))
        elif 'a' <= char <= 'z':
            pos = ord(char) - ord('a')
            new_pos = 25 - pos
            result.append(chr(ord('a') + new_pos))
        elif 'A' <= char <= 'Z':
            pos = ord(char) - ord('A')
            new_pos = 25 - pos
            result.append(chr(ord('A') + new_pos))
        else:
            result.append(char)
    
    return ''.join(result)

def шифр_плейфера(text: str, ключ: str) -> str:
    """Шифр Плейфера."""
    # Создание таблицы 5x5
    алфавит = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    ключ = ключ.lower().replace('ё', 'е').replace('й', 'и')
    
    # Удаление дубликатов из ключа
    seen = set()
    ключ_уникальный = []
    for char in ключ:
        if char in алфавит and char not in seen:
            ключ_уникальный.append(char)
            seen.add(char)
    
    # Добавление остальных букв
    for char in алфавит:
        if char not in seen:
            ключ_уникальный.append(char)
            seen.add(char)
    
    # Создание таблицы
    таблица = []
    for i in range(0, 25, 5):
        таблица.append(ключ_уникальный[i:i+5])
    
    # Шифрование
    text = text.lower().replace('ё', 'е').replace('й', 'и').replace(' ', '')
    
    # Добавление X если две одинаковые буквы подряд
    i = 0
    while i < len(text) - 1:
        if text[i] == text[i+1]:
            text = text[:i+1] + 'х' + text[i+1:]
        i += 2
    
    # Добавление X если нечетное количество букв
    if len(text) % 2 == 1:
        text += 'х'
    
    result = []
    
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        
        # Нахождение позиций в таблице
        pos_a = None
        pos_b = None
        
        for row in range(5):
            for col in range(5):
                if таблица[row][col] == a:
                    pos_a = (row, col)
                if таблица[row][col] == b:
                    pos_b = (row, col)
        
        if not pos_a or not pos_b:
            result.extend([a, b])
            continue
        
        row_a, col_a = pos_a
        row_b, col_b = pos_b
        
        if row_a == row_b:
            # Одна строка
            result.append(таблица[row_a][(col_a + 1) % 5])
            result.append(таблица[row_b][(col_b + 1) % 5])
        elif col_a == col_b:
            # Один столбец
            result.append(таблица[(row_a + 1) % 5][col_a])
            result.append(таблица[(row_b + 1) % 5][col_b])
        else:
            # Прямоугольник
            result.append(таблица[row_a][col_b])
            result.append(таблица[row_b][col_a])
    
    return ''.join(result)

def base64_кодирование(text: str) -> str:
    """Кодирование в Base64."""
    return base64.b64encode(text.encode()).decode()

def base64_декодирование(text: str) -> str:
    """Декодирование из Base64."""
    return base64.b64decode(text.encode()).decode()

def hex_кодирование(text: str) -> str:
    """Кодирование в HEX."""
    return text.encode().hex()

def hex_декодирование(text: str) -> str:
    """Декодирование из HEX."""
    return bytes.fromhex(text).decode()

def генератор_паролей(длина: int = 12, 
                      маленькие_буквы: bool = True,
                      большие_буквы: bool = True,
                      цифры: bool = True,
                      спец_символы: bool = True) -> str:
    """Генерирует случайный пароль заданной длины из возможных символов."""
    symbols = ''
    if маленькие_буквы:
        symbols += 'abcdefghijklmnopqrstuvwxyz'
    if большие_буквы:
        symbols += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if цифры:
        symbols += '0123456789'
    if спец_символы:
        symbols += '!@#$%^&*()_+-=[]{}|;:,.<>/?'
    
    if not symbols:
        raise ValueError("Должен быть выбран хотя бы один набор символов")
    
    return ''.join(secrets.choice(symbols) for _ in range(длина))

def генератор_сильной_соли(длина: int = 32) -> str:
    """Генерирует криптографически сильную соль (HEX)."""
    return secrets.token_hex(длина)

def md5_хеш(text: str) -> str:
    """Возвращает MD5 хеш строки."""
    return hashlib.md5(text.encode()).hexdigest()

def sha256_хеш(text: str) -> str:
    """Возвращает SHA256 хеш строки."""
    return hashlib.sha256(text.encode()).hexdigest()

def sha512_хеш(text: str) -> str:
    """Возвращает SHA512 хеш строки."""
    return hashlib.sha512(text.encode()).hexdigest()

def xor_шифрование(data: str, key: str) -> str:
    """Простое симметричное шифрование XOR."""
    key_bytes = key.encode()
    data_bytes = data.encode()
    encrypted = bytearray()
    for i in range(len(data_bytes)):
        encrypted.append(data_bytes[i] ^ key_bytes[i % len(key_bytes)])
    return encrypted.hex()

def xor_расшифровка(hex_data: str, key: str) -> str:
    """Расшифровка XOR из hex строки."""
    data_bytes = bytes.fromhex(hex_data)
    key_bytes = key.encode()
    decrypted = bytearray()
    for i in range(len(data_bytes)):
        decrypted.append(data_bytes[i] ^ key_bytes[i % len(key_bytes)])
    return decrypted.decode()

def проверка_пароля_на_надежность(пароль: str) -> str:
    """Проверяет надежность пароля."""
    if len(пароль) < 8:
        return "Пароль ненадежен, длина должна быть не менее 8 знаков"
    if not re.search(r"\d", пароль):
        return "Пароль ненадежен, должен содержать цифры"
    if not re.search(r"[a-z]", пароль):
        return "Пароль ненадежен, должен содержать строчные буквы"
    if not re.search(r"[A-Z]", пароль):
        return "Пароль ненадежен, должен содержать заглавные буквы"
    if not re.search(r"[!@#$%^&*()_+=\-{}\[\]:;'<>,.?/\\|]", пароль):
        return "Пароль ненадежен, должен содержать спецсимволы"
    return "Пароль надежен"

# ==========================================
# РАБОТА СО СПИСКАМИ И СТРУКТУРАМИ
# ==========================================

def удалить_дубликаты(input_list: List[Any]) -> List[Any]:
    """Удаляет дубликаты из списка, сохраняя порядок элементов."""
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def глубокое_сплющивание(nested_list: List[Any]) -> List[Any]:
    """Рекурсивно 'сплющивает' вложенный список (Flattening)."""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(глубокое_сплющивание(item))
        else:
            result.append(item)
    return result

def перестановки(input_list: List[Any]) -> List[Tuple[Any, ...]]:
    """Генерирует все возможные перестановки элементов списка."""
    return list(permutations(input_list))

def сочетания(input_list: List[Any], k: int) -> List[Tuple[Any, ...]]:
    """Генерирует все возможные сочетания из N по K элементов списка."""
    return list(combinations(input_list, k))

def декартово_произведение(*args: List[Any]) -> List[Tuple[Any, ...]]:
    """Декартово произведение множеств."""
    return list(product(*args))

def сгруппировать_по_ключу(list_of_dicts: List[Dict], key: str) -> Dict[Any, List[Dict]]:
    """Группирует список словарей по заданному ключу, возвращает defaultdict."""
    groups = defaultdict(list)
    for item in list_of_dicts:
        groups[item[key]].append(item)
    return groups

def группировка_по_значению(input_list: List[Any]) -> Dict[Any, List[int]]:
    """Группирует элементы списка по их значению, возвращает словарь {значение: [индексы]}."""
    groups = defaultdict(list)
    for index, value in enumerate(input_list):
        groups[value].append(index)
    return dict(groups)

def разбить_на_чанки(input_list: List[Any], chunk_size: int) -> List[List[Any]]:
    """Разбивает список на части (чанки) заданного размера."""
    return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]

def ротация_списка(input_list: List[Any], n: int) -> List[Any]:
    """Циклически сдвигает список на n позиций."""
    if not input_list:
        return []
    n %= len(input_list)
    return input_list[-n:] + input_list[:-n]

def сортировка_пузырьком(arr: List[Any]) -> List[Any]:
    """Сортировка пузырьком."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def сортировка_выбором(arr: List[Any]) -> List[Any]:
    """Сортировка выбором."""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def сортировка_вставками(arr: List[Any]) -> List[Any]:
    """Сортировка вставками."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def сортировка_слиянием(arr: List[Any]) -> List[Any]:
    """Сортировка слиянием."""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = сортировка_слиянием(arr[:mid])
    right = сортировка_слиянием(arr[mid:])
    
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def сортировка_подсчетом(arr: List[int]) -> List[int]:
    """Сортировка подсчетом для целых чисел."""
    if not arr:
        return []
    
    min_val = min(arr)
    max_val = max(arr)
    
    count = [0] * (max_val - min_val + 1)
    
    for num in arr:
        count[num - min_val] += 1
    
    result = []
    for i in range(len(count)):
        result.extend([i + min_val] * count[i])
    
    return result

def найти_медиану(arr: List[float]) -> float:
    """Находит медиану списка."""
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    if n % 2 == 1:
        return sorted_arr[n // 2]
    else:
        return (sorted_arr[n // 2 - 1] + sorted_arr[n // 2]) / 2

def найти_моду(arr: List[Any]) -> List[Any]:
    """Находит моду (самые частые значения) списка."""
    if not arr:
        return []
    
    count = Counter(arr)
    max_count = max(count.values())
    return [item for item, cnt in count.items() if cnt == max_count]

def найти_квантиль(arr: List[float], q: float) -> float:
    """Находит квантиль q (0 <= q <= 1) списка."""
    if not arr:
        return 0.0
    
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    
    if q <= 0:
        return sorted_arr[0]
    if q >= 1:
        return sorted_arr[-1]
    
    pos = q * (n - 1)
    lower = int(pos)
    upper = lower + 1
    weight = pos - lower
    
    if upper >= n:
        return sorted_arr[lower]
    
    return sorted_arr[lower] * (1 - weight) + sorted_arr[upper] * weight

def гистограмма(arr: List[float], bins: int = 10) -> Dict[str, List[float]]:
    """Строит гистограмму для списка чисел."""
    if not arr:
        return {"edges": [], "counts": []}
    
    min_val = min(arr)
    max_val = max(arr)
    
    if min_val == max_val:
        return {"edges": [min_val, max_val], "counts": [len(arr)]}
    
    bin_width = (max_val - min_val) / bins
    edges = [min_val + i * bin_width for i in range(bins + 1)]
    counts = [0] * bins
    
    for num in arr:
        bin_idx = min(int((num - min_val) / bin_width), bins - 1)
        counts[bin_idx] += 1
    
    return {"edges": edges, "counts": counts}

# ==========================================
# ФИНАНСОВЫЕ РАСЧЕТЫ
# ==========================================

def сложный_процент(сумма: float, ставка: float, лет: int) -> float:
    """Расчет итоговой суммы со сложным процентом."""
    return сумма * ((1 + ставка/100) ** лет)

def аннуитетный_платеж(кредит: float, ставка: float, лет: int) -> float:
    """Расчет ежемесячного платежа по кредиту."""
    i = (ставка / 100) / 12
    n = лет * 12
    if i == 0:
        return кредит / n
    return кредит * (i * (1 + i)**n) / ((1 + i)**n - 1)

def дифференцированный_платеж(кредит: float, ставка: float, лет: int, месяц: int) -> float:
    """Расчет дифференцированного платежа по кредиту."""
    i = (ставка / 100) / 12
    n = лет * 12
    основной_платеж = кредит / n
    остаток = кредит - основной_платеж * (месяц - 1)
    процентный_платеж = остаток * i
    return основной_платеж + процентный_платеж

def чистая_приведенная_стоимость(денежные_потоки: List[float], ставка: float) -> float:
    """Расчет чистой приведенной стоимости (NPV)."""
    npv = 0
    for t, поток in enumerate(денежные_потоки):
        npv += поток / ((1 + ставка/100) ** t)
    return npv

def внутренняя_норма_доходности(денежные_потоки: List[float]) -> float:
    """Расчет внутренней нормы доходности (IRR)."""
    def npv_func(ставка: float) -> float:
        return чистая_приведенная_стоимость(денежные_потоки, ставка)
    
    # Метод Ньютона-Рафсона для нахождения IRR
    x0 = 0.1  # Начальное приближение
    for _ in range(100):
        f = npv_func(x0)
        f_prime = (npv_func(x0 + 0.001) - npv_func(x0 - 0.001)) / 0.002
        if abs(f_prime) < 1e-12:
            break
        x1 = x0 - f / f_prime
        if abs(x1 - x0) < 1e-12:
            return x1
        x0 = x1
    
    return x0

def срок_окупаемости(денежные_потоки: List[float]) -> float:
    """Расчет срока окупаемости инвестиций."""
    накопленный_поток = 0
    for t, поток in enumerate(денежные_потоки):
        накопленный_поток += поток
        if накопленный_поток >= 0:
            if t == 0:
                return 0
            последний_отрицательный = денежные_потоки[t-1]
            return t - 1 + abs(последний_отрицательный) / поток
    
    return float('inf')  # Никогда не окупится

# ==========================================
# ГРАФЫ И АЛГОРИТМЫ
# ==========================================

class Граф:
    """Класс для работы с графами."""
    
    def __init__(self):
        self.граф = defaultdict(list)
    
    def добавить_ребро(self, u: Any, v: Any, вес: float = 1):
        """Добавляет ребро в граф."""
        self.граф[u].append((v, вес))
        self.граф[v].append((u, вес))  # Для неориентированного графа
    
    def bfs(self, начальная_вершина: Any) -> List[Any]:
        """Поиск в ширину (BFS)."""
        посещенные = set()
        очередь = deque([начальная_вершина])
        результат = []
        
        while очередь:
            вершина = очередь.popleft()
            if вершина not in посещенные:
                посещенные.add(вершина)
                результат.append(вершина)
                for сосед, _ in self.граф[вершина]:
                    if сосед not in посещенные:
                        очередь.append(сосед)
        
        return результат
    
    def dfs(self, начальная_вершина: Any) -> List[Any]:
        """Поиск в глубину (DFS)."""
        посещенные = set()
        результат = []
        
        def dfs_util(вершина):
            посещенные.add(вершина)
            результат.append(вершина)
            for сосед, _ in self.граф[вершина]:
                if сосед not in посещенные:
                    dfs_util(сосед)
        
        dfs_util(начальная_вершина)
        return результат
    
    def алгоритм_дейкстры(self, начальная_вершина: Any) -> Dict[Any, float]:
        """Алгоритм Дейкстры для поиска кратчайших путей."""
        расстояния = {вершина: float('inf') for вершина in self.граф}
        расстояния[начальная_вершина] = 0
        посещенные = set()
        
        while len(посещенные) < len(self.граф):
            текущая = None
            min_расстояние = float('inf')
            
            for вершина in self.граф:
                if вершина not in посещенные and расстояния[вершина] < min_расстояние:
                    текущая = вершина
                    min_расстояние = расстояния[вершина]
            
            if текущая is None:
                break
            
            посещенные.add(текущая)
            
            for сосед, вес in self.граф[текущая]:
                новое_расстояние = расстояния[текущая] + вес
                if новое_расстояние < расстояния[сосед]:
                    расстояния[сосед] = новое_расстояние
        
        return расстояния

def алгоритм_прима(граф: Dict[Any, List[Tuple[Any, float]]]) -> List[Tuple[Any, Any, float]]:
    """Алгоритм Прима для поиска минимального остовного дерева."""
    if not граф:
        return []
    
    вершины = list(граф.keys())
    начальная_вершина = вершины[0]
    
    посещенные = {начальная_вершина}
    ребра_дерева = []
    
    while len(посещенные) < len(вершины):
        min_ребро = None
        min_вес = float('inf')
        
        for вершина in посещенные:
            for сосед, вес in граф[вершина]:
                if сосед not in посещенные and вес < min_вес:
                    min_ребро = (вершина, сосед, вес)
                    min_вес = вес
        
        if min_ребро:
            u, v, вес = min_ребро
            ребра_дерева.append(min_ребро)
            посещенные.add(v)
    
    return ребра_дерева

def алгоритм_флойда_уоршелла(граф: Dict[Any, List[Tuple[Any, float]]]) -> Dict[Any, Dict[Any, float]]:
    """Алгоритм Флойда-Уоршелла для поиска кратчайших путей между всеми парами вершин."""
    вершины = list(граф.keys())
    n = len(вершины)
    индекс = {вершина: i for i, вершина in enumerate(вершины)}
    
    # Инициализация матрицы расстояний
    расстояния = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        расстояния[i][i] = 0
    
    for u in граф:
        for v, вес in граф[u]:
            i, j = индекс[u], индекс[v]
            расстояния[i][j] = вес
    
    # Алгоритм Флойда-Уоршелла
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if расстояния[i][j] > расстояния[i][k] + расстояния[k][j]:
                    расстояния[i][j] = расстояния[i][k] + расстояния[k][j]
    
    # Преобразование обратно в словарь
    результат = {}
    for i, u in enumerate(вершины):
        результат[u] = {}
        for j, v in enumerate(вершины):
            результат[u][v] = расстояния[i][j]
    
    return результат

# ==========================================
# ИГРЫ И РАЗВЛЕЧЕНИЯ
# ==========================================

def угадай_число(минимум: int = 1, максимум: int = 100) -> None:
    """Игра 'Угадай число'."""
    random_number = random.randint(минимум, максимум)
    попытки = 0
    максимальные_попытки = int(math.log2(максимум - минимум + 1)) + 1
    
    print(f"Я загадал число от {минимум} до {максимум}. У тебя {максимальные_попытки} попыток.")
    
    while попытки < максимальные_попытки:
        попытки += 1
        try:
            user_number = int(input(f'Попытка {попытки}. Введите число: '))
        except ValueError:
            print('Пожалуйста, введите действительное число.')
            continue
        
        if user_number < минимум or user_number > максимум:
            print(f'Число должно быть в диапазоне от {минимум} до {максимум}.')
            continue
        
        if user_number < random_number:
            print('Загаданное число больше.')
        elif user_number > random_number:
            print('Загаданное число меньше.')
        else:
            print(f'Поздравляю! Вы угадали число {random_number} за {попытки} попыток.')
            return
    
    print(f'К сожалению, вы проиграли. Я загадал число {random_number}.')

def камень_ножницы_бумага() -> None:
    """Игра 'Камень, ножницы, бумага'."""
    варианты = ['камень', 'ножницы', 'бумага']
    победа_над = {'камень': 'ножницы', 'ножницы': 'бумага', 'бумага': 'камень'}
    
    print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")
    print("Выберите: камень, ножницы или бумага")
    print("Для выхода введите 'выход'")
    
    счет_игрока = 0
    счет_компьютера = 0
    
    while True:
        выбор_игрока = input("Ваш выбор: ").lower()
        
        if выбор_игрока == 'выход':
            print(f"Итоговый счет: Игрок {счет_игрока} - {счет_компьютера} Компьютер")
            break
        
        if выбор_игрока not in варианты:
            print("Неверный выбор. Попробуйте снова.")
            continue
        
        выбор_компьютера = random.choice(варианты)
        print(f"Компьютер выбрал: {выбор_компьютера}")
        
        if выбор_игрока == выбор_компьютера:
            print("Ничья!")
        elif победа_над[выбор_игрока] == выбор_компьютера:
            print("Вы победили!")
            счет_игрока += 1
        else:
            print("Компьютер победил!")
            счет_компьютера += 1

def игра_в_кости() -> None:
    """Игра в кости."""
    print("Бросаем кости...")
    время_ожидания = 2
    
    for i in range(3):
        print(f"{3-i}...")
        time.sleep(1)
    
    кубик1 = random.randint(1, 6)
    кубик2 = random.randint(1, 6)
    сумма_очков = кубик1 + кубик2
    
    print(f"Выпало: {кубик1} и {кубик2}")
    print(f"Сумма очков: {сумма_очков}")
    
    if сумма_очков == 7 or сумма_очков == 11:
        print("Вы выиграли!")
    elif сумма_очков == 2 or сумма_очков == 3 or сумма_очков == 12:
        print("Вы проиграли!")
    else:
        print(f"Ваше число: {сумма_очков}. Бросайте еще раз.")

def симулятор_лотереи(количествоЧисел: int = 6, диапазон: int = 49) -> Dict[str, List[int]]:
    """Симулятор лотереи."""
    if количествоЧисел > диапазон:
        raise ValueError("Количество чисел не может превышать диапазон")
    
    числа_игрока = random.sample(range(1, диапазон + 1), количествоЧисел)
    числа_лотереи = random.sample(range(1, диапазон + 1), количествоЧисел)
    
    совпадения = [число for число in числа_игрока if число in числа_лотереи]
    
    return {
        "игрок": sorted(числа_игрока),
        "лотерея": sorted(числа_лотереи),
        "совпадения": sorted(совпадения),
        "количествоСовпадений": len(совпадения)
    }

# ==========================================
# УТИЛИТЫ ДЛЯ ФАЙЛОВ
# ==========================================

def добавить_задачу_в_файл(задача: str, файл: str = 'Tasks_manager_file.txt') -> None:
    """Добавляет задачу в файл."""
    with open(файл, 'a', encoding='utf-8') as file:
        file.write(f'{задача}\n')
    print(f'Задача "{задача}" добавлена в файл {файл}')

def удалить_все_задачи(файл: str = 'Tasks_manager_file.txt') -> None:
    """Удаляет все задачи из файла."""
    ответ = input('Вы действительно хотите очистить список задач? y (Yes/Да) или n (No/Нет)\nВвод: ')
    if ответ.lower() == 'y':
        with open(файл, 'w', encoding='utf-8') as file:
            file.write('')
        print('Задачи успешно удалены!')
    elif ответ.lower() == 'n':
        print('Отмена удаления списка задач')
    else:
        print('Некорректный ввод. Выберите y(Yes/Да) или n(No/Нет)')

def очистка_кода_от_дубликатов(путь: str) -> str:
    """Очищает код от дубликатов строк."""
    with open(путь, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    unique_lines = []
    seen_lines = set()

    for line in lines:
        stripped_line = line.strip()
        if stripped_line not in seen_lines:
            unique_lines.append(line)
            seen_lines.add(stripped_line)

    cleaned_file_path = путь.replace('.py', '_cleaned.py')
    with open(cleaned_file_path, 'w', encoding='utf-8') as file:
        file.writelines(unique_lines)
    
    return cleaned_file_path

def найти_дубликаты_файлов(директория: str) -> Dict[str, List[str]]:
    """Ищет файлы с одинаковым содержимым (по хешу) в папке."""
    hashes = defaultdict(list)
    for folder, _, files in os.walk(директория):
        for f in files:
            path = os.path.join(folder, f)
            try:
                with open(path, 'rb') as file:
                    file_hash = hashlib.md5(file.read()).hexdigest()
                    hashes[file_hash].append(path)
            except:
                pass
    return {k: v for k, v in hashes.items() if len(v) > 1}

def массовое_переименование(директория: str, шаблон: str, замена: str) -> int:
    """Переименовывает файлы в папке по паттерну (RegEx)."""
    count = 0
    for f in os.listdir(директория):
        новое_имя = re.sub(шаблон, замена, f)
        if новое_имя != f:
            старый_путь = os.path.join(директория, f)
            новый_путь = os.path.join(директория, новое_имя)
            os.rename(старый_путь, новый_путь)
            count += 1
    return count

def чтение_json(файл: str) -> Any:
    """Читает данные из JSON файла."""
    try:
        with open(файл, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        return f"Ошибка при чтении JSON: {e}"

def запись_json(файл: str, данные: Any) -> bool:
    """Записывает данные в JSON файл."""
    try:
        with open(файл, 'w', encoding='utf-8') as f:
            json.dump(данные, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print(f"Ошибка при записи JSON: {e}")
        return False

def чтение_csv(файл: str, разделитель: str = ',') -> List[List[str]]:
    """Читает данные из CSV файла."""
    данные = []
    with open(файл, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=разделитель)
        for row in reader:
            данные.append(row)
    return данные

def запись_csv(файл: str, данные: List[List[str]], заголовки: List[str] = None) -> bool:
    """Записывает данные в CSV файл."""
    try:
        with open(файл, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            if заголовки:
                writer.writerow(заголовки)
            writer.writerows(данные)
        return True
    except Exception as e:
        print(f"Ошибка при записи CSV: {e}")
        return False

# ==========================================
# КАЛЬКУЛЯТОРЫ И ИНТЕРФЕЙСЫ
# ==========================================

def калькулятор_консольный() -> None:
    """Запускает консольный калькулятор."""
    print("Калькулятор")
    print("Поддерживаемые операции: +, -, *, /, ^, sqrt, sin, cos, tan")
    print("Для выхода введите 'выход'")
    
    while True:
        выражение = input("Введите выражение: ").strip()
        
        if выражение.lower() == 'выход':
            print("До свидания!")
            break
        
        if not выражение:
            continue
        
        try:
            # Замена русских символов на английские
            выражение = выражение.replace('^', '**').replace('√', 'sqrt')
            
            # Проверка безопасности выражения
            разрешенные_символы = set('0123456789+-*/.() sqrtcionsaelrабвгдеёжзийклмнопрстуфхцчшщъыьэюя')
            if not все(set(выражение.lower()), lambda x: x in разрешенные_символы):
                print("Выражение содержит недопустимые символы")
                continue
            
            # Вычисление
            результат = eval(выражение, {"__builtins__": {}}, 
                           {"sqrt": math.sqrt, "sin": math.sin, "cos": math.cos, "tan": math.tan})
            print(f"Результат: {результат}")
        except Exception as e:
            print(f"Ошибка: {e}")

def калькулятор_с_интерфейсом() -> None:
    """Запускает интерфейсный калькулятор."""
    
    def calculate():
        выражение = entry.get()
        try:
            # Замена русских символов
            выражение = выражение.replace('^', '**').replace('√', 'math.sqrt')
            
            # Проверка безопасности
            разрешенные_символы = set('0123456789+-*/.() mathqrtcionsaelrабвгдеёжзийклмнопрстуфхцчшщъыьэюя')
            if not все(set(выражение.lower()), lambda x: x in разрешенные_символы):
                result_label.config(text="Ошибка: недопустимые символы")
                return
            
            результат = eval(выражение, {"__builtins__": {}, "math": math}, {})
            result_label.config(text=f"Результат: {результат}")
        except Exception as e:
            result_label.config(text=f"Ошибка: {e}")
    
    def нажать_кнопку(символ):
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current + символ)
    
    def очистить():
        entry.delete(0, tk.END)
        result_label.config(text="")
    
    root = tk.Tk()
    root.title("Калькулятор PyPetka")
    root.geometry("400x500")
    
    # Поле ввода
    entry = ttk.Entry(root, width=40, font=("Arial", 14))
    entry.pack(pady=10)
    
    # Фрейм для кнопок
    buttons_frame = ttk.Frame(root)
    buttons_frame.pack(pady=10)
    
    # Кнопки
    кнопки = [
        ['7', '8', '9', '/', 'C'],
        ['4', '5', '6', '*', '√'],
        ['1', '2', '3', '-', '^'],
        ['0', '.', '=', '+', 'sin']
    ]
    
    for i, row in enumerate(кнопки):
        button_row = ttk.Frame(buttons_frame)
        button_row.pack()
        for j, text in enumerate(row):
            if text == 'C':
                btn = ttk.Button(button_row, text=text, width=8, command=очистить)
            elif text == '=':
                btn = ttk.Button(button_row, text=text, width=8, command=calculate)
            elif text == '√':
                btn = ttk.Button(button_row, text=text, width=8, 
                               command=lambda t='sqrt()': нажать_кнопку(t))
            elif text == '^':
                btn = ttk.Button(button_row, text=text, width=8, 
                               command=lambda t='^': нажать_кнопку(t))
            elif text == 'sin':
                btn = ttk.Button(button_row, text=text, width=8, 
                               command=lambda t='sin()': нажать_кнопку(t))
            else:
                btn = ttk.Button(button_row, text=text, width=8, 
                               command=lambda t=text: нажать_кнопку(t))
            btn.grid(row=0, column=j, padx=2, pady=2)
    
    # Метка для результата
    result_label = ttk.Label(root, text="", font=("Arial", 12))
    result_label.pack(pady=10)
    
    root.mainloop()

# ==========================================
# ИИ-ПОМОЩНИК И УТИЛИТЫ ДЛЯ ПОИСКА
# ==========================================

def _generate_example(func_name: str, func_obj: Callable) -> str:
    """Генерирует пример использования функции на основе ее имени и сигнатуры."""
    
    примеры = {
        'решить_квадратное_уравнение': 'решить_квадратное_уравнение(1, -3, 2)  # Корни: 2.0, 1.0',
        'является_палиндромом': 'является_палиндромом("казак")  # True',
        'удалить_дубликаты': 'удалить_дубликаты([1, 2, 2, "a", 1, "a", 4])',
        'НОД_список': 'НОД_список([12, 18, 24])  # 6',
        'генератор_паролей': 'генератор_паролей(16)',
        'шифр_цезаря': 'шифр_цезаря("привет", 3)  # "тулзкх"',
        'шифр_виженера': 'шифр_виженера("текст", "ключ")',
        'факториал': 'факториал(5)  # 120',
        'числа_фибоначчи': 'числа_фибоначчи(10)',
        'сложный_процент': 'сложный_процент(1000, 5, 10)  # 1628.89',
        'аннуитетный_платеж': 'аннуитетный_платеж(1000000, 7, 20)',
        'угадай_число': 'угадай_число(1, 100)',
        'расстояние_между_точками': 'расстояние_между_точками(0, 0, 3, 4)  # 5.0',
        'теорема_пифагора': 'теорема_пифагора(3, 4, "c")  # 5.0',
        'синус': 'синус(30, в_градусах=True)  # 0.5',
        'косинус': 'косинус(60, в_градусах=True)  # 0.5',
        'тангенс': 'тангенс(45, в_градусах=True)  # 1.0',
        'арксинус': 'арксинус(0.5, в_градусах=True)  # 30.0',
        'арккосинус': 'арккосинус(0.5, в_градусах=True)  # 60.0',
        'арктангенс': 'арктангенс(1, в_градусах=True)  # 45.0',
        'левенштейн': 'левенштейн("кот", "код")  # 1',
        'jaro_расстояние': 'jaro_расстояние("марта", "марфа")  # 0.933',
        'звуковой_алгоритм': 'звуковой_алгоритм("Роберт")  # "R163"',
        'md5_хеш': 'md5_хеш("привет")',
        'sha256_хеш': 'sha256_хеш("привет")',
        'base64_кодирование': 'base64_кодирование("привет")',
        'hex_кодирование': 'hex_кодирование("привет")',
        'быстрая_сортировка': 'быстрая_сортировка([3, 1, 4, 1, 5, 9])',
        'бинарный_поиск': 'бинарный_поиск([1, 3, 5, 7, 9], 5)  # 2',
        'сортировка_пузырьком': 'сортировка_пузырьком([3, 1, 4, 1, 5])',
        'сортировка_слиянием': 'сортировка_слиянием([3, 1, 4, 1, 5])',
        'найти_медиану': 'найти_медиану([1, 3, 3, 6, 7, 8, 9])  # 6',
        'найти_моду': 'найти_моду([1, 2, 2, 3, 3, 3, 4])  # [3]',
        'найти_квантиль': 'найти_квантиль([1, 2, 3, 4, 5], 0.5)  # 3.0',
        'гистограмма': 'гистограмма([1, 2, 2, 3, 3, 3, 4, 4, 5], 5)',
        'чистая_приведенная_стоимость': 'чистая_приведенная_стоимость([-1000, 300, 300, 300, 300], 10)',
        'внутренняя_норма_доходности': 'внутренняя_норма_доходности([-1000, 300, 300, 300, 300])',
        'срок_окупаемости': 'срок_окупаемости([-1000, 300, 300, 300, 300])',
        'симулятор_лотереи': 'симулятор_лотереи(6, 49)',
        'камень_ножницы_бумага': 'камень_ножницы_бумага()',
        'игра_в_кости': 'игра_в_кости()',
        'добавить_задачу_в_файл': 'добавить_задачу_в_файл("Сделать домашку")',
        'очистка_кода_от_дубликатов': 'очистка_кода_от_дубликатов("script.py")',
        'найти_дубликаты_файлов': 'найти_дубликаты_файлов("папка")',
        'массовое_переименование': 'массовое_переименование("папка", "\\.txt$", "\\.bak")',
        'чтение_json': 'чтение_json("data.json")',
        'запись_json': 'запись_json("data.json", {"ключ": "значение"})',
        'чтение_csv': 'чтение_csv("data.csv")',
        'запись_csv': 'запись_csv("data.csv", [[1, 2], [3, 4]], ["A", "B"])',
        'калькулятор_консольный': 'калькулятор_консольный()',
        'калькулятор_с_интерфейсом': 'калькулятор_с_интерфейсом()',
    }
    
    if func_name in примеры:
        return примеры[func_name]
    
    try:
        sig = inspect.signature(func_obj)
        args = []
        
        for name, param in sig.parameters.items():
            if name.startswith('_'):
                continue
            
            if param.kind == inspect.Parameter.VAR_POSITIONAL:
                args.append('1, 2, 3')
                continue
            elif param.kind == inspect.Parameter.VAR_KEYWORD:
                continue
            
            if param.annotation is int or 'число' in name or 'n' == name:
                args.append('42')
            elif param.annotation is float or 'float' in str(param.annotation):
                args.append('3.14')
            elif param.annotation is str or 'строка' in name or 'text' in name:
                args.append(f'"пример"')
            elif param.annotation is list or 'список' in name or name == 'A':
                args.append('[1, 2, 3]')
            elif param.annotation is dict or 'словарь' in name:
                args.append('{"ключ": "значение"}')
            else:
                if param.default is not inspect.Parameter.empty:
                    args.append(f'{param.default}')
                else:
                    args.append('...')
        
        example_args = ', '.join(args)
        return f'{func_name}({example_args})'
    except:
        return f'{func_name}(...)'

def score_match(name: str, doc: str, query: str) -> int:
    """Улучшенная система скоринга с учетом токенов и основ слов."""
    score = 0
    
    name_normalized = name.lower().replace('_', ' ')
    doc_normalized = doc.lower() if doc else ''
    
    query_tokens = re.findall(r'\b\w+\b', query.lower())
    
    # Полное совпадение
    if query in name_normalized or query in doc_normalized:
        score += 50
    
    # Совпадение отдельных токенов
    for token in query_tokens:
        if token in name_normalized:
            score += 20
        if token in doc_normalized:
            score += 10
        
        # Проверка по основе слова
        if token.startswith('мат'):
            if 'мат' in name_normalized or 'мат' in doc_normalized:
                score += 15
        if token.startswith('шифр') or token.startswith('крипт'):
            if 'шифр' in name_normalized or 'крипт' in name_normalized:
                score += 15
        if token.startswith('уравн'):
            if 'уравн' in name_normalized or 'уравн' in doc_normalized:
                score += 15
        if token.startswith('сорт'):
            if 'сорт' in name_normalized or 'сорт' in doc_normalized:
                score += 15
        if token.startswith('поиск'):
            if 'поиск' in name_normalized or 'поиск' in doc_normalized:
                score += 15
        if token.startswith('файл'):
            if 'файл' in name_normalized or 'файл' in doc_normalized:
                score += 15
        if token.startswith('игр'):
            if 'игр' in name_normalized or 'игр' in doc_normalized:
                score += 15
    
    return score

def PyPetka_AI() -> None:
    """Ультимативный интерактивный помощник PyPetka."""
    
    # Сбор всех функций
    functions = {}
    current_module = sys.modules[__name__]
    
    for name, obj in inspect.getmembers(current_module):
        if inspect.isfunction(obj) and not name.startswith('_'):
            doc = inspect.getdoc(obj)
            if doc:
                functions[name] = {'doc': doc.lower(), 'obj': obj, 'score': 0}
    
    print("\n" + "="*80)
    print("🤖 PyPetka AI v4.0: Готов помочь с любой задачей!")
    print("Содержит более 150 функций для математики, шифрования, игр и утилит.")
    print("Просто скажи, что тебе надо (например: 'квадратное уравнение', 'шифр цезаря', 'сортировка').")
    print("Для выхода: 'выход'.")
    print("="*80 + "\n")
    
    while True:
        query = ввод("PyPetka > ").strip().lower()
        if query in ('выход', 'exit', 'quit', 'q', 'стоп'):
            print("До новых встреч! Удачи! ✨")
            break
        
        if not query:
            continue
        
        # Обработка специальных команд
        if query == 'список':
            print("\n📚 Доступные категории функций:")
            print("  • Математика (уравнения, геометрия, тригонометрия)")
            print("  • Шифрование (Цезарь, Виженер, хеши)")
            print("  • Алгоритмы (сортировки, поиск, графы)")
            print("  • Финансы (проценты, кредиты, инвестиции)")
            print("  • Игры (угадай число, кости, камень-ножницы-бумага)")
            print("  • Работа с файлами (JSON, CSV, переименование)")
            print("  • Утилиты (генераторы, конвертеры, калькуляторы)")
            continue
        
        # Поиск функций
        results = []
        
        for name, data in functions.items():
            data['score'] = score_match(name.lower(), data['doc'], query)
            if data['score'] > 0:
                results.append((name, data))
        
        results.sort(key=lambda x: x[1]['score'], reverse=True)
        
        if results:
            print(f"\n✅ Найдено {len(results)} функций по запросу '{query}':")
            
            for i, (name, result) in enumerate(results[:10]):
                try:
                    example_code = _generate_example(name, result['obj'])
                except Exception as e:
                    example_code = f"Не удалось сгенерировать пример. Ошибка: {e}"
                
                print(f"\n{'⭐' if i < 3 else '📌'} {i+1}. {name} (релевантность: {result['score']})")
                print(f"   📝 Описание: {result['doc'][:100]}...")
                print(f"   💻 Пример: {example_code}")
        else:
            print(f"🤔 По запросу '{query}' ничего не найдено. Попробуйте:")
            print("   • 'уравнение' - математические функции")
            print("   • 'шифр' - функции шифрования")
            print("   • 'сортировка' - алгоритмы сортировки")
            print("   • 'игра' - игровые функции")
            print("   • 'файл' - работа с файлами")
            print("   • 'список' - показать все категории")

# ==========================================
# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ==========================================

def все(коллекция: List[Any], условие: Callable[[Any], bool]) -> bool:
    """Проверяет, все ли элементы коллекции удовлетворяют условию."""
    return all(условие(элемент) for элемент in коллекция)

def любой(коллекция: List[Any], условие: Callable[[Any], bool]) -> bool:
    """Проверяет, хотя бы один элемент коллекции удовлетворяет условию."""
    return any(условие(элемент) for элемент in коллекция)

def фильтрация(список: List[Any], условие: Callable[[Any], bool]) -> List[Any]:
    """Возвращает элементы списка, которые соответствуют условию."""
    return [элемент for элемент in список if условие(элемент)]

def отображение(список: List[Any], функция: Callable[[Any], Any]) -> List[Any]:
    """Применяет функцию к каждому элементу списка."""
    return [функция(элемент) for элемент in список]

def свертка(список: List[Any], функция: Callable[[Any, Any], Any], начальное_значение: Any = None) -> Any:
    """Сворачивает список, применяя функцию к элементам."""
    if начальное_значение is None:
        return reduce(функция, список)
    else:
        return reduce(функция, список, начальное_значение)

def генератор_чисел(начало: int, конец: int, шаг: int = 1) -> List[int]:
    """Генерирует список чисел от начала до конца."""
    return list(range(начало, конец + 1, шаг))

def случайный_элемент(список: List[Any]) -> Optional[Any]:
    """Возвращает случайный элемент из списка."""
    return random.choice(список) if список else None

def случайное_число(минимум: int = 0, максимум: int = 100) -> int:
    """Возвращает случайное число в заданном диапазоне."""
    return random.randint(минимум, максимум)

def перемешать_список(список: List[Any]) -> List[Any]:
    """Перемешивает список случайным образом."""
    shuffled = список.copy()
    random.shuffle(shuffled)
    return shuffled

def выборка(список: List[Any], количество: int, уникальные: bool = True) -> List[Any]:
    """Выбирает случайную выборку из списка."""
    if уникальные:
        return random.sample(список, min(количество, len(список)))
    else:
        return [random.choice(список) for _ in range(количество)]

# ==========================================
# СТАТИСТИЧЕСКИЕ ФУНКЦИИ
# ==========================================

def среднее_арифметическое(данные: List[float]) -> float:
    """Среднее арифметическое."""
    return statistics.mean(данные) if данные else 0.0

def медиана_данных(данные: List[float]) -> float:
    """Медиана."""
    return statistics.median(данные) if данные else 0.0

def мода_данных(данные: List[Any]) -> List[Any]:
    """Мода (самые частые значения)."""
    try:
        return statistics.multimode(данные)
    except:
        return []

def дисперсия_данных(данные: List[float]) -> float:
    """Дисперсия выборки."""
    return statistics.variance(данные) if len(данные) > 1 else 0.0

def стандартное_отклонение_данных(данные: List[float]) -> float:
    """Среднеквадратичное отклонение."""
    return statistics.stdev(данные) if len(данные) > 1 else 0.0

def коэффициент_вариации(данные: List[float]) -> float:
    """Коэффициент вариации (в процентах)."""
    среднее = среднее_арифметическое(данные)
    if среднее == 0:
        return 0.0
    return (стандартное_отклонение_данных(данные) / среднее) * 100

def корреляция_пирсона(x: List[float], y: List[float]) -> float:
    """Коэффициент корреляции Пирсона."""
    if len(x) != len(y) or len(x) < 2:
        return 0.0
    
    n = len(x)
    сумма_x = sum(x)
    сумма_y = sum(y)
    сумма_xy = sum(xi * yi for xi, yi in zip(x, y))
    сумма_x2 = sum(xi**2 for xi in x)
    сумма_y2 = sum(yi**2 for yi in y)
    
    числитель = n * сумма_xy - сумма_x * сумма_y
    знаменатель = math.sqrt((n * сумма_x2 - сумма_x**2) * (n * сумма_y2 - сумма_y**2))
    
    if знаменатель == 0:
        return 0.0
    
    return числитель / знаменатель

def линейная_регрессия(x: List[float], y: List[float]) -> Tuple[float, float]:
    """Вычисляет коэффициенты k и b для y = kx + b."""
    n = len(x)
    if n < 2:
        return 0.0, 0.0
    
    сумма_x = sum(x)
    сумма_y = sum(y)
    сумма_xy = sum(xi * yi for xi, yi in zip(x, y))
    сумма_x2 = sum(xi**2 for xi in x)
    
    k = (n * сумма_xy - сумма_x * сумма_y) / (n * сумма_x2 - сумма_x**2)
    b = (сумма_y - k * сумма_x) / n
    
    return k, b

# ==========================================
# ОСНОВНОЙ БЛОК ЗАПУСКА
# ==========================================

if __name__ == "__main__":
    print("="*80)
    print("🎉 PyPetka Ultimate v4.0 загружен!")
    print(f"📊 Доступно функций: {len([name for name in dir() if not name.startswith('_') and callable(eval(name))])}")
    print("="*80)
    
    # Запуск AI-помощника
    PyPetka_AI()