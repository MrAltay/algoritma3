def days_difference(day1: int, day2: int) -> int:
    return day2 - day1
gun = int(input('1. Günü Giriniz : '))
gun2 = int(input('2. Günü Giriniz : '))

sonuc = days_difference(gun, gun2)
print(sonuc)