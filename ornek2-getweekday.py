def get_weekday(current_weekday: int, days_ahead: int) -> int:
    return (current_weekday + days_ahead - 1) % 7 + 1
gun1 = int(input('1. Günü Giriniz : '))
gun2 = int(input('2. Günü Giriniz : '))

sonuc2 = get_weekday(gun1, gun2)
print(sonuc2)