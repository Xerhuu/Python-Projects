#kök bulmayı ekleme
import math   

def toplama(a,b):
    c = a+b
    return c 

def çıkarma(a,b):
    c = a-b
    return c 

def bölme(a,b):
    c = a/b
    return c 

def çarpma(a,b):
    c = a*b
    return c 

def faktoriyel(a):
    return math.factorial(a)
    
def üs_alma(a,b):
    return math.pow(a,b)

def mod(a,b):
    return a%b

is_running = True

while is_running:

    print("---- Hesap makinesi ----")
    print('************************')
    print("1 - Toplama")
    print("2 - Çıkarma")
    print("3 - Çarpma")
    print("4 - Bölme")
    print("5 - Faktoriyel")
    print("6 - Mod alma")
    print("7 - Üs alma")
    print('************************')
    
    while True:
        işlem = input("Yapmak istediğiniz işlemi seçiniz (1-8):  ")
        if işlem.isdigit() and 0 < float(işlem) < 8:
            break
        else:
            print("Lütfen sayı ve 1-7 arasında bir numara giriniz!")

    if işlem == '1' :
        while True:
            try:
                c = float(input("İlk sayıyı giriniz : "))                 
                break  
            except ValueError:
                print("Geçersiz giriş! Lütfen geçerli bir sayı giriniz.")  
        while True:
            try:
                d = float(input("İkinci sayıyı giriniz : "))                 
                break  
            except ValueError:
                print("Geçersiz giriş! Lütfen geçerli bir sayı giriniz.")  
        sonuc = toplama(c,d)
        print(f"Toplama işleminin sonucu : {sonuc}")

    elif işlem == '2':
        while True:
            try:
                c = float(input("İlk sayıyı giriniz : "))                 
                break  
            except ValueError:
                print("Geçersiz giriş! Lütfen geçerli bir sayı giriniz.")  
        while True:
            try:
                d = float(input("İkinci sayıyı giriniz : "))                 
                break  
            except ValueError:
                print("Geçersiz giriş! Lütfen geçerli bir sayı giriniz.") 
        sonuc = çıkarma(c,d)
        print(f"Çıkarma işleminin sonucu : {sonuc}")

    elif işlem == '3':
        while True:
            try:
                c = float(input("İlk sayıyı giriniz : "))                 
                break  
            except ValueError:
                print("Geçersiz giriş! Lütfen geçerli bir sayı giriniz.")  
        while True:
            try:
                d = float(input("İkinci sayıyı giriniz : "))                 
                break  
            except ValueError:
                print("Geçersiz giriş! Lütfen geçerli bir sayı giriniz.") 
        sonuc = çarpma(c,d)
        print(f"Çarpma işleminin sonucu : {sonuc}")

    elif işlem == '4':
       while True:
            try:
                c = float(input("İlk sayıyı giriniz : "))                 
                break  
            except ValueError:
                print("Geçersiz giriş! Lütfen geçerli bir sayı giriniz.")  
       while True:
            try:
                d = float(input("İkinci sayıyı giriniz : "))                 
                break  
            except ValueError:
                print("Geçersiz giriş! Lütfen geçerli bir sayı giriniz.") 
       sonuc = bölme(c,d)
       print(f"Bölme işleminin sonucu : {sonuc}")

    elif işlem == '5':
        while True:
            try:
                c = int(input("Faktoriyelinin almak istediğiniz sayıyı giriniz : "))                 
                break  
            except ValueError:
                print("Geçersiz giriş! Lütfen geçerli bir sayı giriniz.") 
        sonuc = faktoriyel(c)
        print(f"Faktoriyel alma işleminin sonucu : {sonuc}")

    elif işlem == '6':
        while True:
            try:
                c = float(input("İlk sayıyı giriniz : "))                 
                break  
            except ValueError:
                print("Geçersiz giriş! Lütfen geçerli bir sayı giriniz.")  
        while True:
            try:
                d = float(input("İkinci sayıyı giriniz : "))                 
                break  
            except ValueError:
                print("Geçersiz giriş! Lütfen geçerli bir sayı giriniz.") 
        sonuc = mod(c,d)
        print(f"Mod alma işleminin sonucu : {sonuc}")

    elif işlem == '7':
        while True:
            try:
                c = float(input("Üs almak istediğiniz sayıyı giriniz : "))                 
                break  
            except ValueError:
                print("Geçersiz giriş! Lütfen geçerli birs ayı giriniz.")  
        while True:
            try:
                d = float(input("Alınacak üs miktarını giriniz : "))                 
                break  
            except ValueError:
                print("Geçersiz giriş! Lütfen geçerli bir sayı giriniz.") 
        sonuc = üs_alma(c,d)
        print(f"Üs alma işleminin sonucu : {sonuc}")

    if not input("Tekrar işlem yapmak istiyor musunuz? (Y/N): ").lower() == 'y':
        is_running = False

print("----İyi günler!!----")

