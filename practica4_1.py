def is_divisible_by_3(number):
    """
    Проверяет, делится ли число на 3.

    Args:
    number (int): Число для проверки.

    Returns:
    bool: True, если число делится на 3, иначе False.
    """
    return number % 3 == 0

# Запрашиваем число у пользователя
try:
    user_input = int(input("Введите число: "))
    if is_divisible_by_3(user_input):
        print(f"Число {user_input} делится на 3.")
    else:
        print(f"Число {user_input} не делится на 3.")
except ValueError:
    print("Пожалуйста, введите корректное числовое значение.")