bir_sayi = 0
iki_sayi = 0
üc_sayi = 0
dör_sayi = 0
bes_sayi = 0
bir_iki = 0
bir_üc = 0
iki_bir = 0
iki_üc = 0
üc_bir = 0
üc_iki = 0
bilgi = int(input("Kaç Basamaklı Sayı Gireceksiniz....:"))
if bilgi == 2:
    sayi = int(input("Sayıyı Giriniz...:"))
    iki_sayi = sayi % 10
    bir_sayi = (sayi-iki_sayi)/10
    if bir_sayi ** iki_sayi == sayi:
        print("Girilen Sayı Bir Friedman Sayısıdır.....")
    elif iki_sayi ** bir_sayi == sayi:
        print("Girilen Sayı Bir Friedman Sayısıdır.....)")
    elif bir_sayi ** iki_sayi != sayi:
        print("Sayınız Friedman Sayı Değildir")
    elif iki_sayi ** bir_sayi != sayi:
        print("Sayınız Friedman Sayı Değildir")
if bilgi == 3:
    sayi = int(input("Sayıyı Giriniz...:"))
    üc_sayi = sayi % 10
    iki_sayi = ((sayi - üc_sayi) / 10) % 10
    bir_sayi = (((sayi - üc_sayi) / 10 - iki_sayi) / 10)
    bir_iki = (str(int(bir_sayi))+str(int(iki_sayi)))
    bir_iki = int(bir_iki)
    bir_üc = (str(int(bir_sayi))+str(int(üc_sayi)))
    bir_üc = int(bir_üc)
    iki_bir = (str(int(iki_sayi))+str(int(bir_sayi)))
    iki_bir = int(iki_bir)
    iki_üc = (str(int(iki_sayi))+str(int(üc_sayi)))
    iki_üc = int(iki_üc)
    üc_bir = (str(int(üc_sayi))+str(int(bir_sayi)))
    üc_bir = int(üc_bir)
    üc_iki = (str(int(üc_sayi))+str(int(iki_sayi)))
    üc_iki = int(üc_iki)

    if bir_sayi**iki_sayi == sayi or bir_sayi**üc_sayi == sayi or bir_sayi**(iki_sayi+üc_sayi) == sayi or bir_sayi**(iki_sayi-üc_sayi) == sayi or bir_sayi**(üc_sayi-iki_sayi) == sayi or (bir_sayi**iki_sayi)-üc_sayi == sayi or (bir_sayi**üc_sayi)-iki_sayi == sayi or (bir_sayi**iki_sayi)+üc_sayi == sayi or (bir_sayi**üc_sayi)+iki_sayi==sayi or (bir_sayi+iki_sayi)**üc_sayi == sayi or (bir_sayi+üc_sayi)**iki_sayi==sayi or bir_iki**üc_sayi == sayi or bir_üc**iki_sayi == sayi or bir_sayi**iki_üc == sayi or bir_sayi**üc_iki == sayi:
        print("Girilen Sayı Bir Friedman Sayıdır....")
    elif iki_sayi**bir_sayi == sayi or iki_sayi**üc_sayi == sayi or iki_sayi**(bir_sayi+üc_sayi) == sayi or iki_sayi**(bir_sayi-üc_sayi) == sayi or iki_sayi**(üc_sayi-bir_sayi) == sayi or (iki_sayi**bir_sayi)-üc_sayi == sayi or (iki_sayi**üc_sayi)-bir_sayi == sayi or (iki_sayi**bir_sayi)+üc_sayi == sayi or (iki_sayi**üc_sayi)+bir_sayi==sayi or (iki_sayi+bir_sayi)**üc_sayi == sayi or (iki_sayi+üc_sayi)**bir_sayi==sayi or iki_bir**üc_sayi ==sayi or iki_üc**bir_sayi == sayi or iki_sayi**bir_üc== sayi or iki_sayi**üc_bir == sayi:
        print("Girilen Sayı Bir Friedman Sayıdır....")
    elif üc_sayi**iki_sayi == sayi or üc_sayi**bir_sayi == sayi or üc_sayi**(iki_sayi+bir_sayi) == sayi or üc_sayi**(iki_sayi-bir_sayi) == sayi or üc_sayi**(bir_sayi-iki_sayi) == sayi or (üc_sayi**iki_sayi)-bir_sayi == sayi or (üc_sayi**bir_sayi)-iki_sayi == sayi or (üc_sayi**iki_sayi)+bir_sayi == sayi or (üc_sayi**bir_sayi)+iki_sayi==sayi or (üc_sayi+bir_sayi)**iki_sayi == sayi or (üc_sayi+iki_sayi)**bir_sayi==sayi or üc_bir**iki_sayi == sayi or üc_iki**bir_sayi==sayi or üc_sayi**bir_iki == sayi or üc_sayi**iki_bir == sayi:
        print("Girilen Sayı Bir Friedman Sayıdır....")
    else:
        print("Girilen Sayı Bir Friedman Sayısı Değildir....")

