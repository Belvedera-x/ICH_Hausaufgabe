1
b=0
while True :
    a = float(input("Введите число:"))
    if a == 0:
        print(b)
        break
    if a < 0:
        continue
    b += a