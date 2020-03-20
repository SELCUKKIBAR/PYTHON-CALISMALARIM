# fonksiyon ile girilen 2 sayının ortalamasını alma
def ortalama():
    sayi_1 = int(input("1.Sayıyı Giriniz...:"))
    sayi_2 = int(input("2.Sayıyı Giriniz...:"))
    ortalama = (sayi_1 + sayi_2)/2
    print("Girilen 2 sayının ortalaması...:",ortalama)
ortalama()