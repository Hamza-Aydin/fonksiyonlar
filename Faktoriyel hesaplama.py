def faktoriyel(sayı):
    faktoriyel=1
    if sayı==0 or sayı==1:
        print("faktoriyeli:",faktoriyel)
    elif sayı<0:
        print("negatif sayıların faktoriyeli hesaplanamaz!")
    else:
        while sayı>1:
            faktoriyel*=sayı
            sayı-=1
        print("faktoriyeli:",faktoriyel)
while True:
    import time
    sayı=int(input("lütfen bir sayı giriniz:"))
    print("Hesaplanıyor...")
    time.sleep(1)
    faktoriyel(sayı)