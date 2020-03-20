# girilen  sayını asal sayımı ?
def asal():
    sayac = 0
    deger = 1
    sayi = int(input("Sayıyı Giriniz....:"))
    for i in range(2,sayi):
        if sayi % i == 0:
            sayac +=1
            break
    if sayac != 0:
        print("Girilen Değer Asal Sayı Değil...")
    else:
        print("Girilen Değer Asal Sayı...")
asal()