#asal sayılar bire ve kendisinden başka sayılara bölünemeyen sayılardı.


def asalsayı_mı(sayı):
    if sayı==1:
        return False
    elif sayı==2:
        return True
    else:
        a=range(2,sayı)
        for i in a:
            if sayı%i==0:
                return False
        return True
while True:
    sayı=input("lütfen bir sayı giriniz:")

    if sayı=="q":
            break
    else:
        sayı=int(sayı)
        if asalsayı_mı(sayı):
                print("bu sayı asal sayıdır.")
        else:
                print("bu sayı asal sayı değildir!!")

