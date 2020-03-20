def uc_bes():
    ilk_deger = int(input("Başlangıç Değerini Giriniz....:"))
    son_deger = int(input("Son Değeri Giriniz............:"))
    ıkı_bolen = []
    uc_bolen = []
    bes_bolen = []
    for sayi in range(ilk_deger,son_deger):
        if sayi % 2 == 0:
            ıkı_bolen.append(sayi)
        elif sayi % 3 == 0:
            uc_bolen.append(sayi)
        elif sayi % 5 == 0:
            bes_bolen.append(sayi)
    print("2 ile Bölünen Sayılar...:",ıkı_bolen)
    print("3 ile Bölğnen Sayılar...:",uc_bolen)
    print("5 ile Bölünen Sayılar...:",bes_bolen)
uc_bes()