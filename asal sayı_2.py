# Girilen 2 sayı arasındaki asal sayıları bulaun program
def asal():
    asal_liste = []
    ilk_sayi = int(input("Başlangıç Değerini Giriniz....:"))
    son_sayi = int(input("Son Değeri Giriniz............:"))
    for sayi in range(ilk_sayi,son_sayi+1):
        if sayi > 1:
            for i in range(2,sayi):
                if sayi % i == 0:
                    break
            else:
                asal_liste.append(sayi)
    print(asal_liste,sep="",end=" ")
asal()