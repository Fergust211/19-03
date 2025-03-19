city_codes = {
    495: {"city": "Москва", "rate": 6},
    383: {"city": "Новосибирск", "rate": 4},
    343: {"city": "Екатеринбург", "rate": 5},
    381: {"city": "Омск", "rate": 8},
    473: {"city": "Воронеж", "rate": 3}
}

code = int(input("Введите код города: "))
if code in city_codes:
    city_info = city_codes[code]
    cost = city_info["rate"]
    print(f"Стоимость одной минуты {city_info['city']} ({code}): {cost} руб.")

# duration = int(input("Введите количество минут: "))
# if code in city_codes:
#     city_info = city_codes[code]
#     cost = duration * city_info["rate"]
#     print(f"Стоимость {duration} минут {city_info['city']} ({code}): {cost} руб.")

else:
    print("Неверное значение)