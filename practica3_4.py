import random

def math_game():
    correct_answers = 0
    incorrect_answers = 0

    while incorrect_answers < 3:
        # Генерация двух случайных чисел от 1 до 10
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)

        # Запрашиваем у пользователя ответ на выражение
        answer = input(f"{num1} + {num2} = ")

        # Проверяем, что введенное значение является числом
        if answer.isdigit():
            user_answer = int(answer)

            # Проверяем правильность ответа
            if user_answer == num1 + num2:
                print("Правильно!")
                correct_answers += 1
            else:
                print("Ответ неверный.")
                incorrect_answers += 1
        else:
            print("Пожалуйста, введите числовое значение.")

    # Игра окончена, выводим количество правильных ответов
    print(f"Игра окончена. Правильных ответов: {correct_answers}")

# Запуск игры
math_game()