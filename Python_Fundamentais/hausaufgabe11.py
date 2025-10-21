# 1     Звёздочки вместо чисел
# Напишите программу, которая заменяет все цифры в строке на звёздочки *.
# text = "My number is 123-456-789"
# Пример вывода:
# Строка: My number is 123-456-789
# Результат: My number is ***-***-***
from itertools import count

text = "My number is 123-456-789"
print("Строка: ", text)
res = text
for i in text:
    if  i.isdigit():
       res = res.replace(i, "*")
print("Результат: ", res)

#   2  Количество символов
# Напишите программу, которая подсчитывает количество вхождений всех символов в строке. Нужно вывести только символы, которые встречаются более 1 раза (игнорируя регистр), с указанием их количества.
# Выводите повторяющиеся символы только один раз.
# text = "Programming in python"
# Пример вывода:
# Строка: Programming in python
# Символ 'p' встречается 2 раз(а)
# Символ 'r' встречается 2 раз(а)
# Символ 'o' встречается 2 раз(а)
# Символ 'g' встречается 2 раз(а)
# Символ 'm' встречается 2 раз(а)
# Символ 'i' встречается 2 раз(а)
# Символ 'n' встречается 3 раз(а)
# Символ ' ' встречается 2 раз(а)

text = "Programming in python"
print("Строка: ", text)
text = text.lower()
res = ""
for i in text:
    if i not in res:
        res += i
        count_i =text.count(i)
        if count_i > 1:
            print("Символ '", i, "'встречается ", count_i, "раз")



#   3.Увеличение чисел
# Напишите программу, которая заменяет все числа в строке на их эквивалент, умноженный на 10.
# text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
# Пример вывода:
# I have 50.0 apples and 100.0 oranges, price is 5.0 each. Card number is ....3672.

text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
words = text.split()
for i in range(len(words)):
    if words[i].replace('.', '', 1).isdigit():
        words[i] = str(float(words[i]) * 10)
result = " ".join(words)
print(result)