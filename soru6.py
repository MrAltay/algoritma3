def ortalama(not1: int, not2: int, not3: int) -> int:
    return (not1 + not2 + not3) / 3
deger1 = int(input('1. Notu Girin : '))
deger2 = int(input('2. Notu Girin : '))
deger3 = int(input('3. Notu Girin : '))
sonuc = ortalama(deger1, deger2, deger3)
print(sonuc)