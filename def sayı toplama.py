# girilen sayıya kadar olan tek ve çift sayıları ayrı ayrı toplama
def tek_cift():
    tek_sayi = []
    cift_sayi = []
    tek_toplam = 0
    cift_toplam = 0
    sayi = int(input("Sayıyı Giriniz....:"))
    for i in range(1,sayi):
        if i% 2 == 0:
            cift_toplam += i
            cift_sayi.append(i)
        else:
            tek_toplam += i
            tek_sayi.append(i)
    print("Çift Sayılar...:",cift_sayi)
    print("Çift Sayıların Toplamı...:",cift_toplam)
    print("Tek Sayılar....:",tek_sayi)
    print("Tek Sayıların Toplamı...:",tek_toplam)
tek_cift()