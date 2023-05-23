s = int(input("Введите общее количество журавликов:  "))

if s % 6 != 0:
    print("Задача не имеет целочисленного ответа  ")
else:
    part = s // 6
    pet = part
    kate = part * 4
    ser = part
    print(s, "->", pet, kate, ser)