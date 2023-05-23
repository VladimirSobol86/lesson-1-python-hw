i = int(input("Введите трехзначное число:  "))
lengh = str(i)

if len(lengh) != 3:
    print("Вы ввели некорректное число")
else:
    t = i % 10
    s = ((i % 100) - t) // 10
    f = (i - i % 100) // 100
    j = f + s + t
    print(i, "->", j, "(", f, "+", s, "+", t, ")")