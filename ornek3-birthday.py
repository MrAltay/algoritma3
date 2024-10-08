def days_difference(day1: int, day2: int) -> int:
    return day2 - day1
def get_weekday(current_weekday: int, days_ahead: int) -> int:
    return (current_weekday + days_ahead - 1) % 7 + 1
def get_birthday_weekday(current_weekday: int, current_day: int, birthday_day: int) -> int:
    days_diff = days_difference(current_day, birthday_day)
    return get_weekday(current_weekday, days_diff)

sonuc = get_birthday_weekday(5, 3, 4)
print(sonuc)
sonuc2 = get_birthday_weekday(6, 116, 3)
print(sonuc2)