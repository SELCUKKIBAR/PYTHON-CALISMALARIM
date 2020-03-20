def alan():
    print("Dik Üçgen İçin (1),\nKare İçin (2),\nDikdörtgen İçin (3)")
    istek = int(input("Alanını Hesaplamak İstediğiniz Geometrik Şekli Seçiniz....:"))
    if istek == 1:
        ucgen_kısa = int(input("Üçgenin Kısa Kenar Uzunluğunu Giriniz....:"))
        ucgen_uzun = int(input("Üçgenin Uzun Kenar Uzunluğunu Giriniz....:"))
        alan = (ucgen_kısa*ucgen_uzun)/2
        print("Üçgenin Alanı....:",alan)
    elif istek == 2:
        kenar = int(input("Karenin Kenar Uzunluğunu Giriniz....:"))
        alan = kenar*kenar
        print("Karenin alanı....:",alan)
    elif istek == 3:
        dik_kısa = int(input("Dikdörtgenin Kısa Kenar Uzunluğunu Giriniz...:"))
        dik_uzun = int(input("Dikdörtgenin Uzun Kenar Uzunluğunu Giriniz...:"))
        alan= dik_kısa*dik_uzun
        print("Dikdörtgenin Alanı.....:",alan)
alan()