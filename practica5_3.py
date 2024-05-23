
days_of_week = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")


num_weekends = int(input("Сколько выходных на неделе вы хотите? "))


if num_weekends < 0 or num_weekends > 7:
    print("Неверное количество выходных. Введите значение от 0 до 7.")
else:

    weekends = list(days_of_week[-num_weekends:])  # Последние num_weekends дней
    workdays = list(days_of_week[:-num_weekends])  # Все дни до выходных


    print(f"Ваши выходные дни: {', '.join(weekends)}")
    print(f"Ваши рабочие дни: {', '.join(workdays)}")
