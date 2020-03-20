#tahmin oynu
from random import randint
tutlan_sayi = randint(1,100)
sayac = 0
while True:
    sayac += 1
    sayi = int(input("1 ile 100 Arasında Bir Sayı Giriniz....Çıkış için (0)...:"))
    if sayi == 0:
        print("Oyundan Çıkış Yaptınız....")
        break
    elif sayi < tutlan_sayi:
        print("Daha Büyük Sayı Giriniz....")
        continue
    elif sayi > tutlan_sayi:
        print("Daha Küçük Sayı Giriniz....")
        continue
    else:
        print("Rastgele Tutulan Sayı...:",tutlan_sayi)
        print(sayac,"Tahminde Doğru Bildiniz....")
    break

