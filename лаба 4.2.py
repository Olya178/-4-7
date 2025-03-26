a=int(input ("Введите номер места:"))
if 1 < a <= 36 and a%2==0:
    print(str ("Верхнее купе"))
elif 37 <= a<=54 and a%2==0:
    print(str ("Боковушка верх"))
elif 1 <= a<=36 and a%2!=0:
    print(str ("Нижнее купе"))
elif 37 <= a<=54 and a%2!=0:
    print(str ("Боковушка низ"))