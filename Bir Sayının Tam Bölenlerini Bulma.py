def tam_böleneleri_bulma(sayı):
    if sayı==0:
        print("tam bölenleri yoktur!")
    else:
        a=range(1,sayı)
        for i in a:
            if sayı%i==0 :
                print(i)
while True:
    print("çıkmak için 'q' ya basın ")
    sayı=input("lütfen bir sayı giriniz:")

    if sayı=="q":
        print("programdan çıkılıyor...")
        break
    else:
        sayı=int(sayı)
        tam_böleneleri_bulma(sayı)
