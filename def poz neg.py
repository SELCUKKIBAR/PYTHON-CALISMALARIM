def poz_neg():
    sayi = int(input("Sayıyı Giriniz....:"))
    if sayi == 0:
        print("Girlen Sayı Sıfır...:",sayi)
    elif sayi > 0:
        print("Girilen Sayı Pozitif...:",sayi)
    else:
        print("Girilen Değer Negatif...:",sayi)
poz_neg()