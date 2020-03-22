# İKİ BASAMAKLI FRİEDMAN SAYI BULMA PROGRAMI
# ÜÇ BASAMAKLI FRİEDMAN SAYISINI BULMA PROGRAMINA ÇALIŞMALARIM DEVAM EDİYOR
son_rakam = 0
ilk_rakam = 0
sayi = int(input("Kontrol etmek istediğiniz sayıyı giriniz...:"))
son_rakam = sayi%10
ilk_rakam = (sayi-son_rakam)/10
if ilk_rakam**son_rakam == sayi:
    print("Sayınız Friedman Sayısıdır.....")
elif son_rakam**ilk_rakam == sayi:
        print("Sayınız Friedman Sayısıdır.....)")
elif ilk_rakam**son_rakam != sayi:
    print("Sayınız Friedman Sayı Değildir")
elif son_rakam**ilk_rakam != sayi:
    print("Sayınız Friedman Sayı Değildir")

