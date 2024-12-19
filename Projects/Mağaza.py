import random
print ()
urun_listesi = ['Ceket','Hırka','Mont','Sweet','Hoodie','Pantalon','Tişört','Gömlek','Eşofman']

stok_miktarı = {urun: random.randint(5,30) for urun in urun_listesi}

is_running = True

print("----Hoşgeldiniz----")

while is_running:
    print()   
    print("1-Güncel stok listesi.")
    print("2-Stoğa ürün ekleme.")
    print("3-Stoktan ürün çıkarma.")
    print("4-Stok kontrol\n")

    
    while True:
     işlem = input("Yapmak istediğiniz işlemi seçiniz (1-4): ")
     if işlem.isdigit() and 1 <= int(işlem) <= 4:
        break
     else:
        print("Lütfen sadece 1 ile 4 arasında bir sayı giriniz.")
     print()

    if işlem =='1':
        print("Güncel Stok Listesi:\n")
        print("*************************")
        for urun, miktar in stok_miktarı.items():
            print(f"{urun.capitalize()} stokta {miktar} adet var.")
        print()    
        print("*************************")    

    elif işlem == '2':  
            print("1-Yeni ürün ekleme")
            print("2-Stoktaki ürüne ekleme.")
                 
            ekleme = input("Yapılacak işlemi seçiniz : ")  
            if ekleme == '1':  
                yeni_urun = input("Eklemek istediğiniz ürünü giriniz :  ").lower().capitalize() #sadece isim
                yeni_urun_stock = int(input("Yeni ürünün stoğa eklenecek miktarını yazınız :  ")) #sadece sayı
            
                stok_miktarı[yeni_urun] = yeni_urun_stock
                print(f"\nStoğa {yeni_urun_stock} adet {yeni_urun.capitalize()} eklendi.\n")

                print("Yenilenmiş Stok Listesi:\n")
                print("*************************")
                for urun, miktar in stok_miktarı.items():
                    print(f"{urun.capitalize()} stokta {miktar} adet var.")
                print()    
                print("*************************")
            elif ekleme == '2':
                 stok_ekleme = input("Ekleme yapmak istediğiniz ürünü yazınız : ").lower().capitalize()
                 if stok_ekleme not in urun_listesi:
                      print("Geçersiz ürün ismi.")
                 else:
                      ekleme_miktarı = int(input("Eklemek istediğiniz miktarı yazınız : ")) #sadec sayı
                      stok_miktarı[stok_ekleme]+=ekleme_miktarı
                      print()
                      print(f"Stoğa {ekleme_miktarı} adet {stok_ekleme.capitalize()} eklendi. Yeni stok adedi {stok_miktarı[stok_ekleme]}.\n")

                      print("Yenilenmiş Stok Listesi:\n")
                      print("*************************")
                      for urun, miktar in stok_miktarı.items():
                         print(f"{urun.capitalize()} stokta {miktar} adet var.")
                      print()    
                      print("*************************")     

    elif işlem =='3':
            çıkarılacak_urun = input("Çıkarmak istediğiniz ürünü giriniz :  ").lower().capitalize() #sadece harf girilebilir ve sotokta olmalı
            mevcut_stok = stok_miktarı[çıkarılacak_urun]
            print()

            print(f"Stokta {mevcut_stok} adet {çıkarılacak_urun.capitalize()} bulunuyor\n")   

            print("1-Ürünü tamamen çıkarmak için ")
            print("2-Stoktan adet ile çıkarmak için\n")
            while True:
               çıkarma = input("İşlemi seçiniz : ").lower() 
               if çıkarma.isdigit() and 1 <= int(çıkarma) <= 2:
                    break
               else:
                   print("Lütfen sadece 1 ile 2 arasında bir sayı giriniz.")
           
            if çıkarma == '1' :
                 del stok_miktarı[çıkarılacak_urun]
                 print("Yenilenmiş Stok Listesi:\n")
                 print("*************************")
                 for urun, miktar in stok_miktarı.items():
                    print(f"{urun.capitalize()} stokta {miktar} adet var.")
                 print()    
                 print("*************************")                  
            elif çıkarma =='2':
                 çık_miktar = int(input("Çıkarılacak miktarı yazınız : ")) #sadece sayı girilebilir
                 if çık_miktar <= stok_miktarı[çıkarılacak_urun]:
                      stok_miktarı[çıkarılacak_urun]-=çık_miktar
                      print(f"{çıkarılacak_urun.capitalize()} stoktan {çık_miktar} adet çıkarıldı. Kalan stok: {stok_miktarı[çıkarılacak_urun]} adet.\n")
                      print("Yenilenmiş Stok Listesi:\n")
                      print("*************************")
                      for urun, miktar in stok_miktarı.items():
                        print(f"{urun.capitalize()} stokta {miktar} adet var.")
                      print()    
                      print("*************************")
                 elif çık_miktar >= stok_miktarı[çıkarılacak_urun]:
                        del stok_miktarı[çıkarılacak_urun]
                        print("Yenilenmiş Stok Listesi:\n")
                        print("*************************")
                        for urun, miktar in stok_miktarı.items():
                            print(f"{urun.capitalize()} stokta {miktar} adet var.")
                        print()    
                        print("*************************") 
                                           
    elif işlem == '4':
            for urun , miktar in stok_miktarı.items() :
                 if miktar <= 10:                     
                    print(f"Stokta {miktar} adet {urun.capitalize()} kalmıştır.")
                 else:
                      pass
                                         
    print()        
    if not input("Başka bir işlem yapmak istiyor musunuz? (Y/N) = ").lower() == 'y':
         is_running = False      