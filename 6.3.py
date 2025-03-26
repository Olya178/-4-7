def mag(dat):
    dat=dat.split(".")
    return int(dat[0]) * int(dat[1]) == int(dat[2][-2:])
print(mag(input("Введите дату :")))
