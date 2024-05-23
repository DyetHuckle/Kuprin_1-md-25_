countries_and_capitals = {
    "Россия": "Москва",
    "Франция": "Париж",
    "Германия": "Берлин",
    "Италия": "Рим",
    "Япония": "Токио",
    "Китай": "Пекин",
    "Индия": "Нью-Дели",
    "Бразилия": "Бразилиа",
    "США": "Вашингтон",
    "Канада": "Оттава"
}


print("Страны и их столицы:")
for country, capital in countries_and_capitals.items():
    print(f"{country}: {capital}")

country_to_find = input("\nВведите название страны, чтобы узнать её столицу: ")
capital = countries_and_capitals.get(country_to_find)
if capital:
    print(f"Столица {country_to_find}: {capital}")
else:
    print(f"Страна '{country_to_find}' не найдена в словаре.")


sorted_countries_and_capitals = dict(sorted(countries_and_capitals.items()))

print("\nСодержимое словаря, отсортированное в алфавитном порядке названий стран:")
for country, capital in sorted_countries_and_capitals.items():
    print(f"{country}: {capital}")