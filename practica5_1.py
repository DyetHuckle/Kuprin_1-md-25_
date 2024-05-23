numbers = [3, 8, 15, 23, 42]

user_number = int(input("Введите число: "))

if user_number in numbers:
    print("Поздравляю, Вы угадали число!")
else:
    print("Нет такого числа!")


print(f"Исходный список: {numbers}")
print(f"Число пользователя: {user_number}")