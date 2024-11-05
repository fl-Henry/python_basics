"""
Задача: Создание списка
Напишите программу, которая запрашивает у пользователя 5 чисел и сохраняет их в список.
Затем выведите на экран все числа.
"""

numbers = []

num1 = input("Введите число: ")
num2 = input("Введите число: ")
num3 = input("Введите число: ")
num4 = input("Введите число: ")
num5 = input("Введите число: ")

numbers.append(num1)
numbers.append(num2)
numbers.append(num3)
numbers.append(num4)
numbers.append(num5)

print(numbers)

nn = [
    num1,
    num2,
    num3,
    num4,
    num5,
]

print(nn)

