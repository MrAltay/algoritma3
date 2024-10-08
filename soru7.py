def ortalama(hepsi: int) -> int:
    return hepsi / 3
deger1 = int(input('1. Notu Girin : '))
deger2 = int(input('2. Notu Girin : '))
deger3 = int(input('3. Notu Girin : '))
deger4 = int(input('4. Notu Girin : '))
minbul = min(deger1, deger2, deger3, deger4)
toplam = deger1 + deger2 + deger3 + deger4 - minbul
sonuc = ortalama(toplam)
print(sonuc)