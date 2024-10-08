def tam_hafta(gun1: int, gun2: int) -> int:
    return int(abs(gun1 - gun2)/7)
deger = int(input('Gün Giriniz : '))
deger2 = int(input('2. Gün Giriniz : '))
print(tam_hafta(deger, deger2))