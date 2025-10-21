1
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
x = int(input("Введите третье число: "))

if a > b and a > x and b > x :
    print('Числа в порядке возрастания: ', x,",", b, ",", a, sep="")
elif a > b and a > x and b < x :
    print('Числа в порядке возрастания: ', b, ",", x, ",", a, sep="")
elif a > b and a < x and b < x :
    print('Числа в порядке возрастания: ', b, ",", a, ",", x, sep="")
elif a < b and a < x and b < x:
    print('Числа в порядке возрастания: ', a, ",", b, ",", x, sep="")
elif a < b and a < x and b > x :
    print('Числа в порядке возрастания: ', x, ",", a, ",", b, sep="")
elif a < b and a > x and b > x :
    print('Числа в порядке возрастания: ', a, ",", x, ",", b, sep="")
else:
    print("Какие-то из введенных чисел одинаковые -нужно вводить разные числа");

2
a = int(input("Введите год: "))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0 :
    print("Год является високосным.")
else:
    print("Год не является високосным.");





