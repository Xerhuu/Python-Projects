print('Bankamıza hoş geldiniz!')

dogru_kullanici = 'melih'
dogru_sifre = 4562

while True:
    try:
        ad = input('Lütfen kullanıcı adınızı giriniz: ')
        if len(ad) < 3:
            raise ValueError('Kullanıcı adı en az 3 karakter uzunluğunda olmalıdır!')
        if not ad.isalpha():
            raise ValueError('Kullanıcı adı yalnızca harflerden oluşmalıdır!')
        if ad.lower() == dogru_kullanici:
            print('Hoş geldiniz, Melih Bey!')
        else:
            print('Yanlış kullanıcı adı. Lütfen tekrar deneyiniz.')
            continue

        hak = 3
        while hak > 0:
            try:
                sifre = input('Lütfen 4 haneli şifrenizi giriniz: ')
                if len(sifre) != 4:
                    print('Şifre 4 haneli olmalıdır. Lütfen tekrar giriniz.')                    
                    continue
                sifre = int(sifre)
                if sifre == dogru_sifre:
                    print('Tekrardan hoş geldiniz, efendim!')
                    exit()
                else:
                    hak -= 1
                    if hak > 0:
                        print(f'Yanlış şifre girdiniz. {hak} hakkınız kaldı.')
                    else:
                        print('Deneme hakkınız bitti. Kullanıcı adını tekrar giriniz.')
            except ValueError:
                print('Lütfen sadece rakamlarla bir şifre giriniz!')
    except ValueError as e:
        print(f'Hata: {e}')
