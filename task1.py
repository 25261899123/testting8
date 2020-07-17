"""Дан список. Разрежьте ее на две равные части (если длина списка — четная, а если длина строки
нечетная, то длина первой части должна быть на один символ больше). Переставьте эти две
части местами, результат запишите в новый список и выведите на экран."""

Spisok = ["1", "2", "3", "4", "5", "6", "7"] 
Dlinna = len(Spisok) #определили длинну списка
if Dlinna % 2 == 0:
    print (len(Spisok))
    half1 = Dlinna /2 # длинну списка разделили на 2 равняется 3
    half_ = int(half1)
    print(Spisok [:half_])
    lol = (Spisok [:half_])
    half2 = (Spisok[half_:])
    print (half2)
    Spisok2 = (half2 + lol)
    print (Spisok2)
else:
    print (len(Spisok))
    half1 = Dlinna /2 + 1 # 3.0
    half_ = int(half1)
    print(Spisok [:half_])
    lol = (Spisok [:half_])
    half2 = (Spisok[half_:])
    print (half2)
    Spisok2 = (half2 + lol)
    print (Spisok2)