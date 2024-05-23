def is_magic_date(day, month, year):
    """
    Проверяет, является ли дата магической.

    :param day: День.
    :param month: Месяц.
    :param year: Год.
    :return: True, если дата магическая, иначе False.
    """
    last_two_digits_of_year = year % 100
    return day * month == last_two_digits_of_year

# Запрашиваем дату у пользователя
try:
    day = int(input("Введите день: "))
    month = int(input("Введите месяц: "))
    year = int(input("Введите год: "))

    # Проверяем, является ли дата магической
    if is_magic_date(day, month, year):
        print("Дата является магической!")
    else:
        print("Дата не является магической.")
except ValueError:
    print("Ошибка: Введите числовые значения для дня, месяца и года.")