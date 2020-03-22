print("""1-ATEŞ, 2-YORGUNLUK,3-KURUÖKSÜRÜK,\n4-SOLUNUM ZORLUĞU,5-ÖKSÜRÜK,6-AĞRI,\n7-HAPŞIRMA,8-BURUN AKINTISI
,9-BURUN TIKANIKLIĞI,10-GÖZLERDE SULANMA,\n11-BOĞAZ AĞRISI,12-İSHAL""")
print()
soru = int(input("Yukarıdaki Belirtilerden Kaçtanesi Sizde Bulunuyor...:"))
while soru <=2 :
      if soru >= 3:
            print("Korona olma ihtimaliniz yüksek....184'ü arayarak sizi karantinaya almalarını bekleyiniz.... ")
      elif soru >= 5:
            print("Korona olma htimaliniz çok yüksek... Maskenizi takarak size en yakın hastaneye başvurunuz...")
      else:
            print("Korkmanıza Gerek Yok Turp Gibisiniz.... :):):)")
            break