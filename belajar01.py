# Melakukan penjumlahan
def kelilingpersegi(panjang, lebar):
     return panjang * lebar

def luaspersegi(panjang, lebar):
     return panjang * lebar

p = int(input("masukkan panjang segitiga :  "))
l = int(input("masukkan lebar segitiga : "))


hasil_keliling = kelilingpersegi(p,l)
hasil_luas = luaspersegi(p,l)

print ("Keliling persegi adalah", hasil_keliling)
print ("Luas persegi adalah", hasil_luas)


