def tek_cift():
    ilk_deger = int(input("Başlangıç Değerini Giriniz....:"))
    son_deger = int(input("Bitiş Değerinin Giriniz.......:"))
    c_sayi = []
    t_sayi = []
    for sayi in range(ilk_deger,son_deger):
        if sayi % 2 == 0:
            c_sayi.append(sayi)
        else:
            t_sayi.append(sayi)
    print("Çift Sayılar....:",c_sayi)
    print("Tek Sayılar.....:",t_sayi)
tek_cift()

