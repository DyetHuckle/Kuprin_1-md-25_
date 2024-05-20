def check_password(password, confirm_password):
    if password == confirm_password:
        print("Пароль принят")
    else:
        print("Пароль не принят")

    # Ввод пароля и его подтверждения


password = input("Введите пароль: ")
confirm_password = input("Подтвердите пароль: ")

# Проверка пароля и вывод результата
check_password(password, confirm_password)