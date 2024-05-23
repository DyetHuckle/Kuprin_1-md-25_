def is_lucky_ticket(ticket_number):
    """
    Проверяет, является ли билет с заданным номером счастливым.

    :param ticket_number: Номер билета (строка).
    :return: True, если билет счастливый, иначе False.
    """
    if len(ticket_number) % 2 != 0:
        raise ValueError("Количество цифр в номере должно быть чётным.")

    half_length = len(ticket_number) // 2
    first_half = ticket_number[:half_length]
    second_half = ticket_number[half_length:]

    sum_first_half = sum(int(digit) for digit in first_half)
    sum_second_half = sum(int(digit) for digit in second_half)

    return sum_first_half == sum_second_half

# Пример использования функции
ticket_number = input("Введите номер билета: ")

try:
    if is_lucky_ticket(ticket_number):
        print("Билет счастливый!")
    else:
        print("Билет не является счастливым.")
except ValueError as e:
    print(f"Ошибка: {e}")