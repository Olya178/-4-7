def num(dat):
    dat = [int(i) for i in dat]
    print(dat[:len(dat)//2])
    print(dat[len(dat) // 2:])

    return sum(dat[:len(dat)//2]) == sum(dat[len(dat)//2:])

print(num(input("Введите дату :")))