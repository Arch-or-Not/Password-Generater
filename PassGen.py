import random
import string
print("""
By Coder: Arch or Not
""")
def rastgele_sifre_uret(uzunluk):
    harfler =  string.ascii_letters + string.digits + string.punctuation
    sonuc = ''.join(random.choice(harfler) for i in range(uzunluk))
    return sonuc
try :
    karakter_sayı = int(input("How many characters should there be? : "))
    print("Your password : " + rastgele_sifre_uret(karakter_sayı))
    print("Your password : " + rastgele_sifre_uret(karakter_sayı))
except ValueError:
    print("Please enter numbers only!")
