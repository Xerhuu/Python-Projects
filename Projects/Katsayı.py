import math

def katsayı_bulma(a,b,c):
    disc =b**2-4*a*c
    if disc > 0:
        print("Denklemin iki farklı reel sayı kökü vardır.")    
        kök1 = (-b+ math.sqrt(disc))/2*a
        kök2 = (-b- math.sqrt(disc))/2*a
        print(f"Denkleminizin kökleri : ({kök1:.2f},{kök2:.2f})") 
    elif disc == 0:
        print("Denklemin tek bir reel kökü vardır.")
        kök = -b/2*a
        print(f"Denkleminizin tek reel kökü : ({kök:.2f})")
    if disc < 0:
        print("Denklemin iki karmaşık sayı kökü vardır.")    
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(disc)) / (2 * a)
        print(f"Denkleminizin kökleri : ({real_part:.2f} + {imaginary_part:.2f}i, {real_part:.2f} - {imaginary_part:.2f}i)")


print("---Katsayı Bulma Programına Hoşgeldiniz---")
print("///")
print("Katsayı bulmada kullanacağımız denklem = ax^2+bx+c")
print("///")
while True:
    try:
        katsayı1 = float(input("a katsayısını giriniz :  "))                
        break  
    except ValueError:
        print("Geçersiz giriş! Lütfen geçerli bir sayı giriniz.")  

while True:
    try:
        katsayı2 = float(input("b katsayısını giriniz :  "))                
        break  
    except ValueError:
        print("Geçersiz giriş! Lütfen geçerli bir sayı giriniz.")  

while True:
    try:
        katsayı3 = float(input("c katsayısını giriniz :  "))                
        break  
    except ValueError:
        print("Geçersiz giriş! Lütfen geçerli bir sayı giriniz.")  
print()
print(f"Yeni denklemimiz : {katsayı1}x^2+{katsayı2}x+{katsayı3}")
katsayı_bulma(katsayı1,katsayı2,katsayı3)