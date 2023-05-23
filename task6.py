num = int(input("Введите шестизначный номер билета:  "))
lengh = str(num)

if len(lengh) != 6:
    print("Вы ввели некорректное число")
else:
    p1 = (num - (num % 1000)) // 1000
    p2 = num % 1000

    t1 = p1 % 10
    s1 = ((p1 % 100) - t1) // 10
    f1 = (p1 - p1 % 100) // 100
    j1 = f1 + s1 + t1

    t2 = p2 % 10
    s2 = ((p2 % 100) - t2) // 10
    f2 = (p2 - p2 % 100) // 100
    j2 = f2 + s2 + t2

    if j1 == j2:
        print("yes")
    else:
        print("no")