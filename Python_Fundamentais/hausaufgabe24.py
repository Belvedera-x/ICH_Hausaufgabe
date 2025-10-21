#  1   Сумма цифр числа
# Напишите рекурсивную функцию, которая находит сумму всех цифр числа.
# Данные:
# num = 43197
# Пример вывода:
# 24
#
# 2    Сумма вложенных чисел
# Напишите рекурсивную функцию, которая суммирует все числа во вложенных списках.
# Данные:
# nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
# Пример вывода:
# 28

num = 43197

def sum_num(num: int) -> int:
    if num == 0:
        return 0
    return num % 10 + sum_num(num // 10)

print(sum_num(num))

# nested_numbers = [1, [2, 3], [4, [5, 6]], 7]


# def sum_numbers(nested_numbers: list[int]) -> int:
#     total_sum = 0
#     for item in nested_numbers:
#         if isinstance(item, list):
#             total_sum += sum_numbers(item)
#         else:
#             total_sum += item
#     return total_sum

# print(sum_numbers(nested_numbers))
