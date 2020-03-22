
import random
secenek=["taş","kağıt","makas"]
taş=secenek[0]
kağıt=secenek[1]
makas=secenek[2]
print("Taş,Kağıt, Makas oyununa hoş geldiniz Oyunu bitirmek için q tuşuna basın")
while True:
    secim = input("Taş mı kağıt mı makas mı?......: ")
    bil_secim = random.choice(secenek)
    if secim==taş:
        if bil_secim==taş:
            print("Bilgisayarın seçimi: Taşn Sonuç: Berabere")
        elif bil_secim==kağıt:
            print("Bilgisayarın seçimi: Kağıtn Kaybettiniz")
        else:
            print("Bilgisayarın seçimi: makasn Sonuç:Kazandınız")
    if secim==kağıt:
        if bil_secim==taş:
            print("Bilgisayarın seçimi: Taşn Sonuç: Kazandınız")
        elif bil_secim==kağıt:
            print("Bilgisayarın seçimi: Kağıtn Sonuç: Berabere")
        else:
            print("Bilgisayarın seçimi: makasn Sonuç:Kaybettiniz")
    if secim==makas:
        if bil_secim==taş:
            print("Bilgisayarın seçimi: Taşn Sonuç: Kaybettiniz")
        elif bil_secim==kağıt:
            print("Bilgisayarın seçimi: Kağıtn Sonuç: Kazandınız")
        else:
            print("Bilgisayarın seçimi: makasn Sonuç:Berabere")
    if secim=='q':
        print("Çıkılıyor...")
        break