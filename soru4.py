print('Mutlak Çıkarma İşlemi')
def mutlak(sayi: int, sayi2: int) -> int:
    return abs(sayi - sayi2)
deger = int(input('İlk Sayıyı Giriniz: '))
deger2 = int(input('İkinci Sayıyı Giriniz: '))
print(mutlak(deger, deger2))