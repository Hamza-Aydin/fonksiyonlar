#iki basamaklı sayıların okunuşu bulan fonksiyon tanımlama

birler=["","bir","iki","üç","dört","beş",
        "altı","yedi","sekiz","dokuz"]
onlar=["","on","yirmi","otuz","kırk","elli",
       "altmış","yetmiş","seksen","doksan"]

def sayıokunuş(sayı):
    birinci=sayı%10
    ikinci=sayı//10
    print(onlar[ikinci],birler[birinci])

while True:
    sayı=int(input("lütfen bir sayı giriniz:"))
    print("sayınız okunuyor...")
    sayıokunuş(sayı)

