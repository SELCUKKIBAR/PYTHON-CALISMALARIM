def not_hesaplama():
    print("Vize ve Final Notuna Göre Ders Geçme Hesaplama Programına Hoşgeldiniz")
    print("-"*50)
    vize = int(input("Vize Notunuzu Giriniz....:"))
    final = int(input("Final Notunuzu Giriniz..:"))
    ortalama = ((vize*30/100)+(final*70/100))
    if ortalama >= 85 and ortalama <= 100:
        print("Ders Geçme Notunuz AA")
    elif ortalama >= 70 and ortalama <= 84:
        print("Ders Geçme Notunuz BA")
    elif ortalama >= 60 and ortalama<= 69:
        print("Ders Geçme Notunuz BB")
    elif ortalama >= 50 and ortalama <= 59:
        print("Ders Geçme Notunuz CB")
    elif ortalama >= 45 and ortalama <= 49:
        print("Ders Geçme Notunuz CC")
    else:
        print("Ortalamanız Yetersiz Olduğu için Ders Tekarına Kaldınız...")

not_hesaplama()
