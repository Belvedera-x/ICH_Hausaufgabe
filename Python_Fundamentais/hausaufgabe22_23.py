# 1. Выбор заказов
# У вас есть список заказов. Каждый заказ содержит название продукта и его цену.
# Напишите функцию, которая:
#     Отбирает заказы дороже 500.
#     Создаёт список названий отобранных продуктов в алфавитном порядке.
#     Возвращает итоговый список названий.
# Данные:
# orders = [
#     {"product": "Laptop", "price": 1200},
#     {"product": "Mouse", "price": 50},
#     {"product": "Keyboard", "price": 100},
#     {"product": "Monitor", "price": 300},
#     {"product": "Chair", "price": 800},
#     {"product": "Desk", "price": 400}
# ]
# Пример вывода:
# ['Chair', 'Laptop']
from fnmatch import translate

# orders = [
#     {"product": "Laptop", "price": 1200},
#     {"product": "Mouse", "price": 50},
#     {"product": "Keyboard", "price": 100},
#     {"product": "Monitor", "price": 300},
#     {"product": "Chair", "price": 800},
#     {"product": "Desk", "price": 400}
# ]
#
# def select_orders (orders):
#     i = [order["product"] for order in orders if order ["price"] > 500]
#     return sorted(i)
#
# print(select_orders(orders))


# 2. Статистика продаж
# Дан список продаж в виде кортежей (товар, количество, цена).
# Напишите программу, которая:
#     Вычисляет общую выручку для каждого товара.
#     Возвращает словарь с товарами {товар: выручка}, отсортированный по убыванию выручки.
# Данные:
# sales = [
#     ("Laptop", 5, 1200),
#     ("Mouse", 50, 20),
#     ("Keyboard", 30, 50),
#     ("Monitor", 10, 300),
#     ("Chair", 20, 800)
# ]
# Пример вывода:
# {'Chair': 16000, 'Laptop': 6000, 'Monitor': 3000, 'Keyboard': 1500, 'Mouse': 1000}

# sales = [
#     ("Laptop", 5, 1200),
#     ("Mouse", 50, 20),
#     ("Keyboard", 30, 50),
#     ("Monitor", 10, 300),
#     ("Chair", 20, 800)
# ]
#
# def static_revenue(sales):
#     transleit = {}
#     for product, quantity, price in sales:
#         total = quantity * price
#         transleit[product] = total
#
#     sorted_1 = dict(sorted(transleit.items(), key=lambda x: x[1], reverse=True))
#     return sorted_1
# print(static_revenue(sales))



# 1. Объединение данных в строку
# Напишите функцию, которая принимает список любых данных (строки, числа, списки, словари) и возвращает их строковое представление, объединённое через " | ".
# Добавьте документацию и аннотации типов для всех параметров и возвращаемого значения.
# Данные:
# data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]
# Пример вывода:
# 42 | hello | [1, 2, 3] | {'a': 1, 'b': 2}
#
# 2. Сумма вложенных чисел
# Напишите функцию, которая принимает список словарей, где каждый словарь содержит имя пользователя и список баллов. Функция должна вернуть сумму всех чисел.
# Добавьте документацию и аннотации типов для всех параметров и возвращаемого значения.
# Данные:
# data = [
#     {"name": "Alice", "scores": [10, 20, 30]},
#     {"name": "Bob", "scores": [5, 15, 25]},
#     {"name": "Charlie", "scores": [7, 17, 27]}
# ]
# Пример вывода:
# Итоговый балл: 156

# from typing import Any
#
# data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]
#
# def join_data(data: list[Any]) -> str:
#     """
#     Соединить все данные в одну строку и обьединяет через пайп
#     :param  data: строки, числа, списки, словари
#     :return: str
#     """
#     return " | ".join(str(item) for item in data)
# print(join_data(data))

# 2

data = [
    {"name": "Alice", "scores": [10, 20, 30]},
    {"name": "Bob", "scores": [5, 15, 25]},
    {"name": "Charlie", "scores": [7, 17, 27]}
]

# def total_summ(data: list[dict[str, list[int]]]) -> int:
def total_summ(data: list[dict[str, int]]) -> int:

    """
    Принимает список словарей
    :param data: name, scores
    :param int: список баллов
    :return: сумма
    """
    total = 0
    for workers in data:
        total += sum(workers["scores"])
    return total

print(total_summ(data))


