import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
parola_uzunlugu = int(input("Parolanızın uzunluğunu giriniz: "))

parola = ""
if parola_uzunlugu <= 4:
    print("5 karakterden küçük parola güvenli değildir. Daha büyük bir sayı giriniz.")
else:    
    for i in range(parola_uzunlugu):
        parola += random.choice(karakterler)

    print(parola)
