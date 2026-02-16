seconds = int(input("seconds (0-8640000): "))
seconds_in_minute= 60
second_in_hour = 60 * 60
second_in_day = 24 * 60 * 60
days = seconds // second_in_day
seconds = seconds % second_in_day
hours = seconds // second_in_hour
seconds = seconds % second_in_hour
minutes = seconds // seconds_in_minute
seconds = seconds % seconds_in_minute
if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif days % 10 in [2, 3, 4] and days % 100 not in [12, 13, 14]:
    day_word = "дні"
else:
    day_word = "днів"
print(f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")